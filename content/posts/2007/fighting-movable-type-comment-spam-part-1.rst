fighting movable type comment spam - part 1
###########################################
:date: 2007-01-26 15:29
:author: admin
:category: tech
:slug: fighting-movable-type-comment-spam-part-1
:status: published
:save_as: 2007/01/26/fighting-movable-type-comment-spam-part-1/index.html
:url: 2007/01/26/fighting-movable-type-comment-spam-part-1/
:private: true

There's recently been a lot of discussion on the Gothamist tech list about fighting comment spam, and it's prompted me to revisit and further develop some thoughts I had about the problem. Since I regularly get approached by friends who are hoping to eliminate their comment spam woes, I thought I'd write up my thoughts.

I should be clear, though, that the methods I'll be outlining aren't endorsed or in use by the folks at Gothamist. They've got their own tech staff who are working on the problem. And because of the -ist sites' high profiles, high traffic and multi-server architecture, some of what I'll be discussing wouldn't really be relevant or appropriate for them anyway. But if you've got your own installation of Movable Type running on a webhost where you can run PHP (most can), read on...

So how do the spammers work, and what are they trying to accomplish? Let's start with the second question. More than anything, they're trying to bump up their rank in search engines. By publishing comments on well-respected sites (in terms of non-spamminess), they can bump up their ranking and make more money. The `nofollow <http://en.wikipedia.org/wiki/Nofollow>`__ tag was supposed to fix all of this, but, well, it didn't. Perhaps the direct profit to be gained by idiots following their links is enough to compel them to do what they do; maybe they just don't bother to see whether nofollow is in place on the blogs they target. Either way, they seem pretty keen to keep doing what they're doing.

So they submit fake comments to sites in droves. They do this using automated scripts — it's faster and easier than making a web browser automatically do this stuff. Libraries like `WWW::Mechanize <http://search.cpan.org/dist/WWW-Mechanize/>`__ make it pretty straightforward.

In truth, it can be even simpler than WWW::Mechanize makes it. That's because blogging software works in uniform ways. When you load up a page with a comment form, the form's HTML tells your browser where to send the text of your comment. When you hit submit, the browser sends a specially-formed request (called an HTTP POST) to that URL. The script sitting at that URL — which, in MT's case, is called mt-comments.cgi by default — processes the request to post a comment.

Spammers simply need to find that URL and send requests to it — generally speaking, they don't even need to load up the comment form beforehand. Unfortunately, it's pretty easy to find these URLs: `here's a google search <http://www.google.com/search?q=inurl%3A%22mt-comments.cgi%22>`__ that returns a bunch (see anybody you recognize?). Some spammers will just `look for Movable Type sites <http://www.google.com/search?q=%22powered%20by%20movable%20type%22>`__ and send requests to common places where mt-comments.cgi might live. That's why one of the first spam-fighting techniques recommended by Six Apart is to `rename mt-comments.cgi <http://www.sixapart.com/pronet/comment_spam#commentscript>`__.

Unfortunately, this doesn't last long. The new name of the script has to be available to your visitors' browsers in order for them to be able to leave comments, which means it's available to spammers, too. Here's how it's represented in the HTML:

   ::

      <form name="commentform" method="post" action="http://domain.com/url/to/renamed-commentscript.cgi">

It's not hard to write something to find blogs on Technorati, visit them, grab the *action* attribute from the form and then start spamming it.

One simple method for avoiding this is to obfuscate the form's action. Libraries like WWW::Mechanize don't generally have a Javascript interpreter built in, so if you use Javascript to set the form's action it'll be unavailable to many spammer scripts (although as Six Apart `notes <http://www.sixapart.com/pronet/comment_spam#obfuscation>`__, this method isn't foolproof). This means that your commenters will have to have at least a basic Javascript interpreter working in order to comment. But even my Sidekick's woefully crappy Javascript implementation can handle this sort of code:

   ::

      <form name="commentform" method="post" action="/">
      body of the form
      </form>
      <script type="text/javascript">
      document.commentform.action = 'http://domain.com/url/to/renamed-commentscript.cgi';
      </script>

Of course, this kind of code is pretty easy to scrape, too. Some Javascript obfuscation might be in order:

   ::

      document.commentform.action = 'http://dom' + 'ain.com/ur' + 'l/to/rena' + 'med-comme' + 'ntscrip' + 't.cgi';

But again, this is defeatible — and it doesn't even require a Javascript interpreter. Here's some Perl that'd do the trick, for example:

   ::

      #!/usr/bin/perl -w
      use LWP::Simple;
      my $html = get('http://some/poor/suckers/blog');
      if($html =~ /\.action\s*=\s*(.*)$/im)
      {
      my $url = $1;
      $url =~ s/['"]\s*\+\s*['"]//gx; # collapse the string
      $url =~ s/(^['"]\s*|['"]\s*;?$)//gx; # clean up leading and trailing quotes
      print "$url\n";
      }

It might return a few false positives, but it'd do the trick. Spammers don't care much about false positives, anyway. HTTP POSTs are cheap.

But there are better ways to obfuscate Javascript. I wrote this one last night. There are many like it, but this one is mine (and would go after the form tag, as before). It's fairly pointless — the next step in the arms race is for the spammers to use a JS interpreter, which would beat it — but I felt like writing it, so I did. I think it's a pretty good one, as these things go.

(As a sidenote, I *really* like doing this sort of `metaprogramming <http://en.wikipedia.org/wiki/Metaprogramming>`__ — writing one program through the use of another. I'm not the type of geek who gets very excited about unit tests or polymorphism, but these kinds of tasks scratch my nerd-itch (exactly disgusting as it sounds) better than anything else. Ask me to write a Perl script that makes some PHP which generates Javascript to write a block of CSS and I'll be a happy boy.)

   ::

      <?php
      function ObfuscateJS($string_to_obfuscate, $number_of_variables=5, $max_chars_per_chunk=3)
      {
      // create some random variables that will be used by JS later on
      $vars = array();
      for($i=0;$i<$number_of_variables;$i++)
      $vars[] = rand();
      // begin building the JS string
      $js = "if(typeof(Obfuscator)!='object')\n   var Obfuscator = new Object();\n";
      for($i=0;$i<sizeof($vars);$i++)
      $js .= "Obfuscator.v$i = " . $vars[$i] . ";\n";
      $js .= "eval(''";
      while(strlen($string_to_obfuscate))
      {
      // figure out how many characters we're going to encode this time
      $num_chars_this_time = rand(1,$max_chars_per_chunk);
      // grab that chunk of characters
      $this_chunk = str_replace("'","\\'",substr($string_to_obfuscate,0,$num_chars_this_time));
      // remove that chunk from the string we're working on
      $string_to_obfuscate = substr($string_to_obfuscate,$num_chars_this_time);
      // create a plausible-seeming alternate, garbage chunk
      $rotated_chunk = '';
      for($i=0;$i<strlen($this_chunk);$i++)
      {
      $thischar = substr($this_chunk,$i,1);
      if((($thischar>='A')&&($thischar<='Z'))||(($thischar>='a')&&($thischar<='z')))
      $thischar = chr(ord($thischar) + (((rand()%2)==1) ? 1 : -1));
      $rotated_chunk .= $thischar;
      }
      // figure out which of our random variables we're going to use
      $v1index = rand(0,sizeof($vars)-1);
      $v2index = rand(0,sizeof($vars)-1);
      // write out a short-form JS if-then that uses the random vars to decide its order
      $js .= " + ((Obfuscator.v$v1index > Obfuscator.v$v2index) ? " . (($vars[$v1index]>$vars[$v2index]) ? "'$this_chunk' : '$rotated_chunk')" : "'$rotated_chunk' : '$this_chunk')");
      }
      $js .= ");\n";
      return $js;
      }
      ?>
      <script type="text/javascript">
      <?php print ObfuscateJS("document.commentform.action = 'http://domain.com/url/to/renamed-commentscript.cgi';");?>
      </script>

I feel confident in saying that this can't be beaten with a mere regex (okay, `technically <http://books.slashdot.org/comments.pl?sid=143298&cid=12015194>`__ it could — but not a regex that a spammer is likely to bother writing). You'd really need a full-on Javascript interpreter to disentangle the logic that this function produces. Unfortunately, the bad guys have those.

And that might be a good place to leave this off. In the next part I'll describe a method for renaming your comment script on a recurring, automated basis. Will that be foolproof, either? Well, no. But I think it'll raise the bar to a level where a spammer would have to expend considerable effort to keep up with your site's constantly moving target — something that he's unlikely to do.

**UPDATE:** Parts `2 </2007/01/26/fighting-movable-type-comment-spam-part-1/>`__ and `3 </2007/01/26/fighting-movable-type-comment-spam-part-1/>`__ are now available.
