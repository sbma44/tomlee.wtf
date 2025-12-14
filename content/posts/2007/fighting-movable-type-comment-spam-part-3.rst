fighting movable type comment spam - part 3
###########################################
:date: 2007-01-29 00:16
:author: admin
:category: tech
:slug: fighting-movable-type-comment-spam-part-3
:status: published
:save_as: 2007/01/29/fighting-movable-type-comment-spam-part-3/index.html
:url: 2007/01/29/fighting-movable-type-comment-spam-part-3/

We've made some good progress. In `part one <http://www.manifestdensity.net/2007/01/26/fighting_movable_type_comment/>`__ I talked about how comment spammers operate and some theoretical ways to stop them. In `part two <http://www.manifestdensity.net/2007/01/27/fighting_movable_type_comment_1/>`__ I offered a little more practical advice, providing a walkthrough on how to convert an MT site from static HTML pages to PHP and offering more specific instructions on how to hide where your comment script lives. I know that at least one person has seen a reduction in comment spam as a result, which makes me pretty pleased.

Sadly, what we've covered so far isn't enough. Spammers will find your renamed mt-comments.cgi no matter how much Javascript you bury it under. If users can use the form, so can spammers. They'll find the new location of mt-comments.cgi sooner or later, and then we'll be back at square one.

But what if mt-comments kept changing its location? We can write a script that renames the file every time it runs, then set it to run at a regular interval. That way even when a spammer manages to find it they'll only be able to send spam until the next time the script runs. It'll be great! There are a couple of problems with this approach, though:

#. If the script runs while a user is composing a comment, when they hit submit the form will send its data to a version of mt-comments that no longer exists. That could be a major pain in the ass. Fortunately, there's a pretty simple solution: we'll just keep two copies of mt-comments around at a time, deleting old ones and adding new ones on a rolling basis. That way a user would have to keep their browser open for two script-intervals in order for their comment to be lost.

#. | The bigger problem is how to let the site's comment forms know about the changing location of mt-comments.cgi. You might recall that Movable Type sticks these values into its templates with code that looks like this:

      ::

         action="<$MTCGIPath$><$MTCommentScript$>"

   | That's fine in theory, but in practice it doesn't work out very well. That's because in order to update those values, Movable Type requires that you rebuild the site. That means we'd be recomposing every page on the blog every time the mt-comments script was renamed. Users wouldn't like the slowdown, and your webhost would get upset about the system resources that you'd end up hogging.
   | So instead we'll drop the <$MTCGIPath$><$MTCommentScript$> nonsense and just use some PHP. That'll let us keep track of the mt-comments script in a single PHP file. When a comment form is loaded it'll read the file and use whatever it finds there. It'll be plenty fast and it won't require that any pages be rebuilt.

So here's the script:

   ::

      <?php
      // CONFIGURATION
      $SECRET = 'mysecret';
      $MT_DIRECTORY = '/public_html/mt/';
      $WRITEABLE_DIRECTORY = '/tmp/';
      $ftp_info = array(
      'host' => 'ftp.yourwebhost.com',
      'user' => 'your_login',
      'password' => 'your_password',
      'port' => 21
      );
      // END CONFIGURATION
      if(isset($_GET[$SECRET])):
      // login, get mt-config.cgi
      $ftp = ftp_connect($ftp_info['host'],$ftp_info['port']) or die('Couldn\'t connect to FTP service.  Is your FTP info correct?');
      ftp_login($ftp,$ftp_info['user'],$ftp_info['password']);
      ftp_chdir($ftp,$MT_DIRECTORY);
      ftp_get($ftp,$WRITEABLE_DIRECTORY . 'mt-config.cgi','mt-config.cgi',FTP_ASCII);
      // retrieve the config file
      $handle = fopen($WRITEABLE_DIRECTORY . 'mt-config.cgi','r');
      $mt_config = fread($handle, filesize($WRITEABLE_DIRECTORY . 'mt-config.cgi'));
      fclose($handle);
      // split it up, process each line
      $mt_config = split("\n",$mt_config);
      $new_mt_config = '';
      $comment_script_current = 'mt-comments.cgi';
      $comment_script_old = 'mt-comments-old.cgi';
      $mt_cgipath = '';
      foreach($mt_config as $line)
      {
      $line = trim($line);
      if(preg_match('/^\s*CommentScript\s+(.*)/i',$line,$matches))
      $comment_script_current = $matches[1];
      elseif(preg_match('/^\s*#\s*OldCommentScript\s+(.*)/i',$line,$matches))
      $comment_script_old = $matches[1];
      elseif(!preg_match('/##### Added by mt\-rotate\.php #####/i',$line))
      {
      if(preg_match('/^\s*CGIPath\s+(.*)/i',$line,$matches))
      {
      $mt_cgipath = $matches[1];
      if(substr($mt_cgipath,-1)!='/')
      $mt_cgipath .= '/';
      }
      $new_mt_config .= $line . "\r\n";
      }
      }
      $new_mt_config = trim($new_mt_config); // get rid of trailing newline chars
      // get mt-comments.cgi
      ftp_get($ftp,$WRITEABLE_DIRECTORY . $comment_script_current,$comment_script_current,FTP_ASCII);
      // generate a new name for mt-comments.cgi (20 chars, a-z, upper & lower case)
      $comment_script_new = '';
      while(strlen($comment_script_new)<20)
      {
      $newchar = chr(ord('a') + rand(0,25));
      $comment_script_new .= (((rand()%2)==0) ? $newchar : strtoupper($newchar));
      }
      $comment_script_new .= '.cgi';
      // rename the current comment script
      rename($WRITEABLE_DIRECTORY . $comment_script_current, $WRITEABLE_DIRECTORY . $comment_script_new);
      // rewrite mt-config.cgi
      $new_mt_config .= "\r\n\r\n##### Added by mt-rotate.php #####\r\n";
      $new_mt_config .= "CommentScript $comment_script_new\r\n";
      $new_mt_config .= "# OldCommentScript $comment_script_current\r\n";
      $handle = fopen($WRITEABLE_DIRECTORY . 'mt-config.cgi', 'w');
      fwrite($handle,$new_mt_config);
      fclose($handle);
      // rewrite the PHP include
      $php_include = "<?php \$PATH_TO_MT_COMMENTS = '" . $mt_cgipath . $comment_script_new . "'; ?>";
      $handle = fopen($WRITEABLE_DIRECTORY . 'mt-comments-location.php','w');
      fwrite($handle,$php_include);
      fclose($handle);
      // upload the new mt-config.cgi
      ftp_put($ftp,'mt-config.cgi',$WRITEABLE_DIRECTORY . 'mt-config.cgi',FTP_ASCII);
      // upload the new comment script and set its permissions
      ftp_put($ftp,$comment_script_new,$WRITEABLE_DIRECTORY . $comment_script_new,FTP_ASCII);
      ftp_site($ftp,"CHMOD 0755 $comment_script_new");
      // delete the old comment script
      ftp_delete($ftp,$comment_script_old);
      // upload mt-comments-location.php
      ftp_put($ftp,'mt-comments-location.php',$WRITEABLE_DIRECTORY . 'mt-comments-location.php',FTP_ASCII);
      ftp_close($ftp);
      // clean up the temp directory
      unlink($WRITEABLE_DIRECTORY . $comment_script_new);
      unlink($WRITEABLE_DIRECTORY . 'mt-config.cgi');
      unlink($WRITEABLE_DIRECTORY . 'mt-comments-location.php');
      endif;
      ?>

You'll notice that there's a bunch of info to fill in at the top. Most of it should be pretty straightforward. You'll need the FTP info for your webhost account — even though we'll run the script on the same machine as your blog, it needs to connect to itself by FTP in order to make sure that the permissions on the files can be set correctly.

The $WRITEABLE_DIRECTORY value can probably be ignored — /tmp/ should work on pretty much every webhost out there. If it doesn't work, you can just create a directory with permissions set to 777 somewhere and point the script at it. But mostly, don't worry about it.

The $MT_DIRECTORY variable needs to point at the directory where Movable Type is installed, and needs to do so from an FTP client's perspective. Connect to your site with an FTP client and browse to your MT directory. You should be able to figure it out from there.

Finally, $SECRET should be set to a unique string. No weird characters or spaces, either — this needs to be able to be added to a URL, so stick to a simple alphanumeric password. This is necessary because running the script too often could constitute a denial-of-service attack on your blog, effectively making it impossible for anyone to comment. Putting a password in a querystring is generally a terrible idea, but since the requests for this script won't be going out over the internet (or outside the host machine at all) it should probably be okay.

Once you've set all of those values, save the script as **mt-rotate.php** and upload it to the directory where Movable Type is installed (i.e. the one where mt.cgi and mt-config.cgi live). Now it's ready to be tested. Fire up your browser and head to:

   http://www.yourdomain.com/mt/mt-rotate.php?mysecret

Of course, change the path so that you're pointing at the right domain and the correct directory. And change "mysecret" to match whatever you set the $SECRET variable to in the script. If all goes well you shouldn't see anything at all — FTP into the site, check the Movable Type directory and confirm that it now has a file called mt-comments-location.php in it, that there's a file with a gibberish name (but ending in .cgi) and that mt-config.cgi now has a line at the bottom mentioning mt-rotate.php. If instead of all of this you see error messages in your web browser, well, something's wrong. Leave a comment and we'll sort it out.

So we can now rotate our comment script's filename every time we call this particular URL. And the new, secret name of the file is kept in mt-comments-location.php in the MT directory. Now we just need to adjust our comment forms so that they can use that PHP file, then set the mt-rotate script to run on an automatic basis.

In order to use mt-comments-location.php, we'll need to know where it resides. Unfortunately, that might be a problem. The $MT_DIRECTORY value may or may not match up with the full path to this file; it all depends on your webhost. I've put together a little script to make it easier to figure out. Download `this <http://www.manifestdensity.net/2007/01/29/where-am-i.php.txt>`__, rename it to where-am-i.php (take the .txt off the end) and upload it to the MT directory on the server. Load it up in your web browser (http://www.yourserver.com/path/to/mt/where-am-i.php) and have a look at the output. It ought to tell you what the filesystem path to the MT directory is.

So! You now have the information necessary to rewrite your comment form's *action* property on the fly. If you didn't add the Javascript obfuscation from `part two <http://www.manifestdensity.net/2007/01/27/fighting_movable_type_comment_1/>`__, your comment form tag should still look something like this:

   ::

      <form method="post" action="<$MTCGIPath$><$MTCommentScript$>" name="comments_form" onsubmit="if (this.bakecookie.checked) rememberMe(this)">

You'll need to add a PHP include statement, then some code to use the variable that becomes available by virtue of the include. Use this, but replace the /path/to/mt/ with the correct filesystem path where Movable Type resides:

   ::


      <?php include('/path/to/mt/mt-comments-location.php');?>
      <form method="post" action="<php print $PATH_TO_MT_COMMENTS;$>" name="comments_form" onsubmit="if (this.bakecookie.checked) rememberMe(this)">

If you *did* implement the Javascript obfuscation, you'll just want to swap <$MTCGIPath$><$MTCommentScript$> and replace it with $PATH_TO_MT_COMMENTS. Like so:

   ::


      <?php include('/path/to/mt/mt-comments-location.php');?>
      <script type="text/javascript">
      <?php print ObfuscateJS("document.comments_form.action = '$PATH_TO_MT_COMMENTS';");?>
      </script>

Make this change in all the templates that have a comment form in them, then rebuild your site (or just open and re-save one entry, if you'd prefer to make sure things are working before rebuilding all of your site's comment forms). If your comment form seems to be working, you're in great shape. If you see PHP warning messages showing up on the page around where you added the *include()* statement, odds are that you got the path to mt-comments-location.php wrong.

But let's say that you didn't. You're pretty much all set — all you need to do is call the script on a regular basis.

The way to do this is with a cron job — these are tasks that can be scheduled to occur at regular intervals on a Unix-style system. You should be able to set up a cron job through your web host's control panel software. This is where you manage the domain's email addresses, among other things. It can vary between hosts, but if you look for "cron jobs" or "scheduled tasks" you should probably be able to find it.

cPanel is probably the most popular of these kinds of control panel software packages, and it happens to be what my webhost uses. So let's have a look at how to make it work:

| |finding the cron item in cPanel|
| |selecting the standard cron mode|
| |here's the punchline|

It ought to be relatively self-explanatory, particularly if you have a look at the above screenshots. But here's the punchline, the command that you want to run every time the cron does:

   ::

      wget http://manifestdensity.net/mt/mt-rotate.php?mysecret -O/dev/null

| "wget" is a program that fetches webpages. The first parameter specifies the URL we want it to fetch (be sure to replace
| "mysecret" with a real value). And the second says to send the retrieved HTML staight to the trash (otherwise it might generate a bunch of junk files in some directory or another). We don't need to hang onto the output, anyway — it's the incoming request that triggers the script's actions. The HTML it produces (or doesn't in this case — remember, there should be no output if it works right) is irrelevant except for debugging purposes.

And, with that somewhat anticlimactic final step, we should be done. The cron should fire however often you set it to (as you can see from the screenshot, I told it to fire once an hour — that seems like a good number to me). When it does, the necessary files will be renamed and updated, and your Movable Type installation should remain fairly spam-free. Hurrah!

**UPDATE:** Whoops! My mistake: I didn't realize that the comment preview template can't be made to use PHP — the filename will always end in .cgi, because it \*is\* the mt-comments script. You might have noticed this when you implemented part two and ended up with non-working Javascript.

The good news is that there's an easy workaround: **simply remove the action attribute from the comment preview template's form tag entirely**. This will make the form submit to itself. If someone's at the preview form, they already know the URL, which means they have the comment script name and there's no point in hiding it anyway.

.. |finding the cron item in cPanel| image:: http://farm1.static.flickr.com/129/372926381_a4cadcd99f_t.jpg
   :target: http://www.flickr.com/photo_zoom.gne?id=372926381&size=o
.. |selecting the standard cron mode| image:: http://farm1.static.flickr.com/127/372926312_c33ec4d09b_t.jpg
   :target: http://www.flickr.com/photo_zoom.gne?id=372926312&size=o
.. |here's the punchline| image:: http://farm1.static.flickr.com/156/372926431_64a05725d4_t.jpg
   :target: http://www.flickr.com/photo_zoom.gne?id=372926431&size=o
