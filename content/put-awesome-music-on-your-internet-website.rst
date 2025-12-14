put awesome music on your internet website
##########################################
:date: 2007-04-06 17:39
:author: admin
:category: tech
:slug: put-awesome-music-on-your-internet-website
:status: published
:save_as: 2007/04/06/put-awesome-music-on-your-internet-website/index.html
:url: 2007/04/06/put-awesome-music-on-your-internet-website/

It seems like everybody's been posting spring playlists:

- `Kriston <http://grammarpolice.net/archives/001271.php>`__
- `DCeiver <http://dceiver.blogspot.com/2007/04/march-top-20.html>`__
- `The Governess <http://pygmalioninablanket.blogspot.com/2007/04/private-life-of-rat.html>`__
- `Amanda <http://blogstretch.blogspot.com/2007/03/playlist-im-fairly-certain-will-improve.html>`__
- `Adrienne <http://www.clutchpearls.com/?p=720>`__

I did a little evangelizing for `playtagger <http://del.icio.us/help/playtagger>`__ over in Kriston's comments, and the PT bookmarklet I've got in my browser has made it easy enough to navigate through the mp3s that everyone's been linking to. But it occurred to me that folks might get some use out of an automatic flash player.

So! If you've got a webpage with a bunch of hyperlinks to mp3s and would like to add a nifty flash player to it, I've written up a handy tool to let you do just that. Simply put the permalink to your entry in the form field below and hit submit. That'll bring you to a page with some HTML. Copy that into your post and you'll have a player for all the mp3s you posted. Kinda neat, huh?

.. container::

   .. raw:: html

      <form action="http://www.metamonkey.net/easyxspf/" method="get">

   +-------------------------------------------------------------+-----------------------------------+
   | URL of page with MP3s                                       |                                   |
   |                                                             |                                   |
   | .. raw:: html                                               |                                   |
   |                                                             |                                   |
   |    <input type="checkbox" value="1" checked name="nocoral"> |                                   |
   |                                                             |                                   |
   |  Disable Coral?                                             |                                   |
   +-------------------------------------------------------------+-----------------------------------+

   .. raw:: html

      </form>

A word about that "disable coral" option — since this loads the flash player off of my webserver, and since you may not be paying for the bandwidth used to stream those mp3s, the polite thing to do is to use the Coral CDN. However, it seems to be broken today (for me, at least), so I've left it disabled by default for the time being.

Here are some sample players that work with the pages above (Amanda and the Governess didn't post mp3s, and DCeiver was too polite to link directly to them, so no links for those guys):

- `Kriston <http://www.metamonkey.net/easyxspf/?url=http%3A%2F%2Fgrammarpolice.net%2Farchives%2F001271.php&nocoral=1&html=2>`__
- `Adrienne <http://www.metamonkey.net/easyxspf/?url=http%3A%2F%2Fwww.clutchpearls.com%2F%3Fp%3D720&html=2&nocoral=1>`__
- and, for good measure, `Catherine's non-spring-specific but still useful-for-demonstration-purposes Washingtonian playlist <http://www.metamonkey.net/easyxspf/?url=http%3A%2F%2Fwww.washingtonian.com%2Fblogarticles%2F3861.html&nocoral=1&html=2>`__

**UPDATE (5/10/07):** Thanks to some jerk hacking a piece of third party software on this site, this script has been unavailable for the past few weeks. It should be all better now.

If anyone's interested, the source code is available behind the jump.

It's pretty straightforward. All you really need to realize is that this script handles both the generation of the code for the user to embed, *and* the XSPF playlist itself.

   ::

      <?php
      if($_GET['html']>0)
      {
      $url = $_GET['url'];
      print "<html><head></head><body>";
      $markup = "<object classid=\"clsid:d27cdb6e-ae6d-11cf-96b8-444553540000\"
      codebase=\"http://fpdownload.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=7,0,0,0\"
      width=\"400\" height=\"168\" >
      <param name=\"allowScriptAccess\" value=\"sameDomain\"/>
      <param name=\"movie\" value=\"http://www.metamonkey.net" . (($_GET['nocoral']==1) ? '' : '.nyud.net:8080') . "/easyxspf/xspf_player.swf\"/>
      <param name=\"quality\" value=\"high\"/>
      <param name=\"bgcolor\" value=\"#E6E6E6\"/>
      <embed src=\"http://www.metamonkey.net" . (($_GET['nocoral']==1) ? '' : '.nyud.net:8080') . "/easyxspf/xspf_player.swf?playlist_url=http://www.metamonkey.net/easyxspf/" . str_replace('?','-QUERY-/',$url) . (($_GET['nocoral']==1) ? '/nocoral' : '') . "\"
      quality=\"high\" bgcolor=\"#E6E6E6\" name=\"xspf_player\" allowscriptaccess=\"sameDomain\"
      type=\"application/x-shockwave-flash\"
      pluginspage=\"http://www.macromedia.com/go/getflashplayer\"
      align=\"center\" height=\"168\" width=\"400\"> </embed>
      </object>";
      if($_GET['html']==1)
      {
      print '<pre>' . str_replace('<','&lt;',str_replace('>','&gt;',$markup)) . '</pre>';
      print '<p><a href="http://www.metamonkey.net/easyxspf/?url=' . urlencode($url) . '&html=2'. (($_GET['nocoral']==1) ? '&nocoral=1' : '') . '">I don\'t want HTML; show me the player</a></p>';
      }
      else
      {
      print $markup;
      print '<p><a href="http://www.metamonkey.net/easyxspf/?url=' . urlencode($url) . '&html=1'. (($_GET['nocoral']==1) ? '&nocoral=1' : '') . '">I don\'t want the player; show me the HTML</a></p>';
      }
      print "</body></html>";
      }
      else
      {
      set_include_path(get_include_path() . PATH_SEPARATOR . '/home/metamon/public_html/PEAR' . PATH_SEPARATOR . '/home/metamon/public_html/PEAR/PEAR');
      require_once('PEAR/Cache.php');
      require_once('PEAR/Cache/Function.php');
      function CoralizeLink($link)
      {
      return preg_replace('/^http:\/\/([^\/]+)\/(.*)$/i','http://$1.nyud.net:8080/$2',$link);
      }
      function GetXSPF($url,$coralize)
      {
      $url = trim($url);
      $domainprefix = preg_replace('/\/.*$/','',$url);
      $coralizeddomainprefix = $domainprefix . '.nyud.net:8080';
      $urlprefix = preg_replace('/\/[^\/]+$/','/',$url);
      $html = file_get_contents($url);
      preg_match_all('/<a[^>]+href=[\'"](.*?\.mp3)[\'"][^>]*>(.*?)<\/a/i',$html,$matches,PREG_SET_ORDER);
      print "<?xml version=\"1.0\" encoding=\"UTF-8\"?>
      <playlist version=\"0\" xmlns = \"http://xspf.org/ns/0/\">
      <trackList>
      ";
      foreach($matches as $match)
      {
      print "   <track>
      <location>";
      if(preg_match('/^http:\/\//',$match[1]))
      print ($coralize) ? CoralizeLink($match[1]) : $match[1];
      else if(preg_match('/^\//',$match[1]))
      print ($coralize) ? CoralizeLink($domainprefix . $match[1]) : ($domainprefix . $match[1]);
      else
      print ($coralize) ? CoralizeLink($urlprefix . $match[1]) : ($urlprefix . $match[1]);
      print "</location>
      <annotation>" . preg_replace('/<[^>]*>/','',$match[2]) . "</annotation>
      </track>
      ";
      }
      print "   </track>
      </trackList>
      </playlist>";
      }
      $url = urldecode($_GET['url']);
      $coralize = true;
      if(preg_match('/\/nocoral$/i',$url))
      {
      $coralize = false;
      $url = preg_replace('/\/nocoral$/i','',$url);
      }
      $url = preg_replace('/\-QUERY\-\//','?',$url);
      $fcache = new Cache_Function($container = 'file', array('cache_dir' => '/tmp', 'filename_prefix' => 'xspfplayer_cache_' ), 900);
      //$fcache->call('GetXSPF',$url,$coralize);
      GetXSPF($url,$coralize);
      }
      ?>

You could strip out all of that PEAR function caching stuff if you wanted — it's just there to improve performance in case someone embeds a player and unexpectedly get an avalanche of traffic.

There is one complication, though. The URL of the playlist is passed in a querystring parameter to the XSPF player flash object. That's fine in most cases, but here the XSPF playlist *also* takes a querystring parameter. Making things worse, that parameter can also have its OWN querystring parameters (as in the case of Adrienne's Wordpress blog). Worst of all, the XSPF player doesn't handle URL-encoded strings very well. So we have to encode all of these parameters into a format that looks like a normal, parameter-less URL. It's a pain in the ass, but it can be done with an .htaccess file. Here's the one I'm using:

   ::


      <IfModule mod_rewrite.c>
      RewriteEngine on
      # Rewrite current-style URLs of the form 'index.php?url=x'.
      RewriteCond %{REQUEST_FILENAME} !-f
      RewriteCond %{REQUEST_FILENAME} !-d
      RewriteRule ^(.*)$ index.php?url=$1 [L,QSA]
      </IfModule>
