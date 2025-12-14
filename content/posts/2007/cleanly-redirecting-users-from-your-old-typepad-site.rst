cleanly redirecting users from your old Typepad site
####################################################
:date: 2007-08-26 15:40
:author: admin
:category: tech
:slug: cleanly-redirecting-users-from-your-old-typepad-site
:status: published
:save_as: 2007/08/26/cleanly-redirecting-users-from-your-old-typepad-site/index.html
:url: 2007/08/26/cleanly-redirecting-users-from-your-old-typepad-site/

Here's a sort-of-interesting problem I've been working on recently, and which might help prevent an internet stranger or two from pulling their hair out. When you're moving from one blog to another, how do you set things up so that folks stumbling across your old site are sent to the new one? This came up while Emily and I were working on `Brian's new site <http://brianbeutler.com>`__. His existing Typepad site had URLs like this:

   http://beutler.typepad.com/home/2007/08/rove-the-erudit.html

I knew that I wanted to clean up the formatting of these a little bit — for one thing, the .html would have to go, as I intended to use some PHP in the pages (on a web server with a standard configuration, only files ending in .php or .php5 are processed for PHP). And that "/home/" seemed extraneous, too.

I did try to make the two similar, though, to simplify things. By default Movable Type creates its URLs from the entry's title, transforming it into a unique identifier called the basename. I altered MT's default basename length so that it was 15 characters, matching the length of Typepad's basenames. I set up the new mapping in MT's Settings/Publishing area, and ended up with new URLs that looked like this:

   http://www.brianbeutler.com/2007/08/rove_the_erudit/index.php

The index.php on the end can be left off — if you ask a Linux web server for a directory, it'll look for "index.php" or "index.html" or "index.htm" and send it back if it finds it. This lets you have slightly tidier-looking URLs. So our new URL is actually:

   http://www.brianbeutler.com/2007/08/rove_the_erudit/

With the format settled upon I was able to write some code that sits on every page of Brian's Typepad site. When a user arrives the page looks at its URL, applies a set of transformations to rewrite it into the new format, and sends the user to the result. Normally you'd want to do this in a server-side script or .htaccess file, but as far as I can tell Typepad doesn't let its users have that level of control. So I had to put it in some Javascript that I added to Brian's Typepad template:

   ::

      <script type="text/javascript">
      location.href = location.href.replace(/beutler\.typepad\.com/,'www.brianbeutler.com').replace(/\/home\//,'/').replace(/\.html$/,'/').replace(/\-/g,'_');
      </script>

This looks complicated, but it really just does a few things to the URL (whatever the URL may be):

#. Replace "beutler.typepad.com" with "www.brianbeutler.com"
#. Replace "/home/" with "/"
#. Replace the ".html" at the end of the URL with "/"
#. Change all hyphens in the URL to underscores

It then sends the browser to the new URL.

Done! All I had to do now is deliver the website, lean back and adopt an attitude of extreme self-satisfaction.

Except... no. I wasn't done. Everything was actually much, much worse than I thought.

I was a little slow to catch on. Brian started receiving emails from readers who were getting 404 errors. The redirection script was sending people to the wrong places.

Brian's got a bunch of regular features with names that start similarly (or are identical). This creates a problem when trying to create unique basenames for each one. Movable Type and Typepad both have systems for dealing with these situations in a way that ensures each basename is distinct — if two entries are both called "xyz", the second one's basename will be "xyz_1", or something aong those lines. But these systems don't behave in quite the same way — or at least they don't when one system has its entries imported and the other has them authored over a period of time.

This resulted in situations like this:

   | **Typepad URL:** http://beutler.typepad.com/home/2007/08/almost-daily--4.html
   | **Rewritten URL:** http://www.brianbeutler.com/2007/08/almost_daily\__4/
   | **Actual New URL:** http://www.brianbeutler.com/2007/08/almost_daily_co_73/

The first one is the old URL. The second one is the rewritten URL, created using the code above. And the third is the *actual* URL — the one that we need to redirect to.

There's another problem, too. Typepad creates an entry's basename the first time you save it, even if you haven't yet published it. The basename is created from the title, as I mentioned. But if the title changes, the basename does not. However, when you import those entries into Movable Type, it recreates the basename from whatever the title ended up being. Which results in the following mess:

   | **Typepad URL:** http://beutler.typepad.com/home/2007/07/h20.html
   | **Rewritten URL:** http://www.brianbeutler.com/2007/07/h20/
   | **Actual New URL:** http://www.brianbeutler.com/2007/07/banal_observati_49/

So: the redirect is fine for a lot of URLs. It fails for some proportion of URLs. But it's impossible to tell which ones just by looking at the URL, and there's no way to figure out what the new URL ought to be on the basis of the old one.

First things first. Let's figure out which URLs are screwed up. We'll iterate through Brian's Typepad archive pages. For each one we'll grab all of the permalinks. Then we'll rewrite them using the rules implemented by the Javascript above. Finally, we'll test each rewritten URL. If it generates a "page not found" message, we'll spit out some code that'll help us with future analysis (more on that in a sec).

Here we go...

   ::

      #!/usr/bin/perl
      print "<?php
      \$typepad_entries = array();
      ";
      for(my $i=34;$i>=12;$i--)
      {
      my $url = 'http://beutler.typepad.com/home/2007/week' . $i . '/index.html';
      my $html = `curl -s $url`;
      my @matches = ($html =~ m/<a class="permalink" href="(.*?)">Permalink<\/a>/isg);
      for $match (@matches)
      {
      my $permalink = $match;
      my $rewritten_link = $permalink;
      $rewritten_link =~ s/beutler\.typepad\.com/www.brianbeutler.com/igx;
      $rewritten_link =~ s/\/home\//\//igx;
      $rewritten_link =~ s/\.html$/\//igx;
      $rewritten_link =~ s/\-/_/gx;
      my $new_html = `curl -s $rewritten_link`;
      if($new_html =~ /404 not found/is)
      {
      my $typepad_html = `curl -s $permalink`;
      my $date = '0';
      if($typepad_html =~ m/<h2 class="date-header">(.*?)<\/h2>/isg)
      {
      $date = $1;
      }
      my $body = '';
      if($typepad_html =~ m/<div class="entry-body">(.*?)<\/div>/isg)
      {
      $body = $1;
      }
      print "
      \$body = <<<EOBODY
      $body
      EOBODY;
      \$typepad_entries[] = array(
      'url' => '$permalink',
      'rewritten_url'  => '$rewritten_link',
      'date' => '$date',
      'body' => \$body,
      );
      \$body = '';
      ";
      }
      }
      }
      print "
      ?>";

This produces output like so:

   ::

      <?php
      $typepad_entries = array();
      $body = <<<EOBODY
      <p>As a physicist, I think this is sort of an <a href="http://www.slate.com/id/2171898/fr/rss/">interesting way to look</a> at economies and economic development. As a blogger, though, I think it confirms a pretty banal point: that regions of the world without diverse or fungible resources don't tend to have strong economies. </p>
      <p><a href="http://beutler.typepad.com/photos/uncategorized/2007/08/18/picture_1.png"><img border="0" src="http://beutler.typepad.com/photos/uncategorized/2007/08/18/picture_1.png" title="Picture_1" alt="Picture_1" class="image-full" style="margin: 0px 5px 5px 0px; float: left;" /></a>
      </p>
      EOBODY;
      $typepad_entries[] = array(
      'url' => 'http://beutler.typepad.com/home/2007/08/the-physics-of-.html',
      'rewritten_url'  => 'http://www.brianbeutler.com/2007/08/the_physics_of_/',
      'date' => 'August 18, 2007',
      'body' => $body,
      );
      $body = '';
      and so on, repeating the above block for each entry

So we've got the Typepad entries exported in an easily-processed format — one that includes the body, date, and information about the URL. Next we need to get the imported Movable Type entries into a similarly useful format. Then we'll write some code that goes through, compares the bodies of the entries and tries to match them up with one another (with the help of the date).

No fancy scripting is required for getting the Movable Type entries. We just need to make a new template in MT that spits out the entries in the format we want:

   .. code:: php

      <?php
      $mt_entries = array();
      <MTEntries lastn="9999">
      $body = <<<EOBODY
      <$MTEntryBody$>
      EOBODY;
      $mt_entries[] = array(
      'permalink' => '<$MTEntryPermalink$>',
      'date' => '<$MTEntryDate$>',
      'body' => $body,
      );
      $body = '';
      </MTEntries>
      ?>";?>

You might've noticed that despite our initial Perlishness, the entries are being stored in PHP. That's because PHP's got a handy `text-comparison function <http://www.php.net/similar_text>`__ that I want to use (as well as easy-to-use `date conversion functions <http://www.php.net/strtotime>`__).

Matching the entries up to one another goes like so:

   .. code:: php

      <?php
      require_once('mt_entries.php');
      require_once('typepad_entries.php');
      // pull out everything except lowercase letters -- simplify the comparisons
      function SimplifyString($x)
      {
      return preg_replace('/[^a-z]/x','',strtolower(strip_tags(trim($x))));
      }
      $sorted_mt_entries = array();
      // sort the entries by date -- we'll use this later
      foreach($mt_entries as $entry)
      $sorted_mt_entries[date('z',strtotime($entry['date']))][] = $entry;
      foreach($typepad_entries as $typepad_entry)
      {
      $most_similar_entry = NULL;
      // ensure that the body isn't empty -- otherwise it'll match everything equally
      if(strlen($typepad_entry['body'])>20)
      {
      $entries_to_examine = $mt_entries;
      // if we can get away with it, only examine the entries from the day in question
      // this both minimizes the set of possible wrong answers and improves
      // processing time
      if($typepad_entry['date']!='0')
      $entries_to_examine = $sorted_mt_entries[date('z',strtotime($typepad_entry['date']))];
      $max_similarity = 0;
      foreach($entries_to_examine as $mt_entry)
      {
      similar_text(SimplifyString($typepad_entry['body']),SimplifyString($mt_entry['body']),$similarity);
      if($similarity>$max_similarity)
      {
      $most_similar_entry = $mt_entry;
      $max_similarity = $similarity;
      }
      }
      if($max_similarity>95) // only use very similar entries
      {
      print "Redirect 301 " . preg_replace('/http:\/\/(.*?)\//','/',$typepad_entry['rewritten_url']) . " " . $most_similar_entry['permalink'] . "\n";
      }
      else
      {
      print "# !!! no good match found: " . $typepad_entry['url'] . "\n";
      }
      }
      else
      {
      print "# !!! entry too short: " . $typepad_entry['url'] . "\n";
      }
      }
      ?>

Run this from the command line and it'll print output like the following:

   ::

      Redirect 301 /2007/07/most_dangerous_/ http://www.brianbeutler.com/2007/07/most_dangerous/
      Redirect 301 /2007/07/wheres_all_the_/ http://www.brianbeutler.com/2007/07/wheres_all_the/
      Redirect 301 /2007/07/almost_daily__4/ http://www.brianbeutler.com/2007/07/almost_daily_co_63/
      Redirect 301 /2007/07/bias/ http://www.brianbeutler.com/2007/07/bias_1/

Which can be pasted directly into an .htaccess file. Now the Javascript on Typepad will still send users to the wrong URL, but once they arrive at that incorrect URL the server will catch their request and redirect it to the right location.

I've just put it online a moment ago, but it seems to work well. And there was only one entry for which the text-matching produced a score of less than 100% similarity. It was easy enough to catch it and manually set the URL.

Of course, it'd be nice of us to keep all of these redirects somewhere other than .htaccess — we're wasting the web server's resources by making it ponder all of them whenever it wants to serve a page. But as sysadmin sins go this is at least a common one. Given the limits of Typepad, the not-outrageous quantity of redirects and the nonexistent noticeable benefit to doing this 100% cleanly, I didn't bother.

But if you wanted to be really slick about it you could make a custom PHP script with all the redirects your 404 handler — that way the redirection overhead would only be incurred when a file wasn't found. There's probably an extremely slick way to do this conditionally with a RewriteRule, too, but I don't know it off the top of my head.

Anyway, there's complete the tale of my weekend's technical adventures (well, except for buying `one of these <http://www.kickgaming.com/supercard-sd-and-superkey-pr-83.html>`__). Hopefully a weary Typepad refugee will someday stumble across my post and get some use out of it.
