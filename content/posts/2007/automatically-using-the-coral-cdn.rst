automatically using the coral cdn
#################################
:date: 2007-02-04 17:16
:author: admin
:category: tech
:slug: automatically-using-the-coral-cdn
:status: published
:save_as: 2007/02/04/automatically-using-the-coral-cdn/index.html
:url: 2007/02/04/automatically-using-the-coral-cdn/

You might've noticed that I hotlinked those mp3s, providing URLs that point directly at someone else's blog. This is normally considered pretty poor form — you're using up someone else's bandwidth without giving them any associated (and salable) web traffic. But in this case it's not quite so bad: I used the Coral CDN to make the links. That reduces the bandwidth that my visitors will be consuming from the other sites to a negligible amount. NYU picks up most of the bill (and is presumably happy to do so). I wrote a bit more about the Coral CDN `here <http://www.zunta.org/blog/archives/2005/03/29/ourmedia_sux0rs/>`__; you can find their explanation `here <http://www.coralcdn.org/>`__. It's an extremely useful tool, and not just for excusing normally boorish behavior — if you have a large file on your own server, it can come in handy there, too.

The only downside is that it requires that users be able to send web traffic out on port [STRIKEOUT:8090] 8080, which is a slightly unusual requirement. It shouldn't be a problem for most people, but if someone's behind a restrictive corporate firewall, the Coral-ified link might make it impossible for them to get the file.

So to fix that I whipped up this Javascript. It attempts to load a small image (originating on this domain) over the Coral CDN. If it manages to, we know that the visitor can use port [STRIKEOUT:8090] 8080 and access the Coral system. If that condition is met, the script then replaces all the links on the page that go to big-seeming files with ones that use Coral ("big-seeming" is determined by the extension — mp3, mp4, mpg and avi are what the script looks for right now, but it's easy to adjust that). If the image doesn't load, the original link is left alone and will presumably still work for the poor firewalled visitor.

Here's the script:

   ::

      <script type="text/javascript">
      function CoralizeLinks()
      {
      // modify the following line to adjust the extensions used by the function
      var EXTENSION_MATCH_RE = new RegExp('\.(mp3|avi|mpg|mp4)$','i');
      var x = new Image();
      x.src = 'http://www.manifestdensity.net.nyud.net:8080/coral-test.gif';
      x.onload = function()
      {
      var domain = location.href.replace(/http:\/\//i,'').replace(/\/.*$/,'');
      var links = document.getElementsByTagName('a')
      for(var i=0;i<links.length;i++)
      {
      if((links[i].href.match(EXTENSION_MATCH_RE))&&(!(links[i].href.match(/\.nyud\.net:80[89]0/i))))
      {
      if(links[i].href.match(/^http:\/\//i))
      links[i].href = links[i].href.replace(/http:\/\/(.*?)\/(.*)$/i,'http://$1.nyud.net:8080/$2');
      else if(links[i].href.match(/^\//))
      links[i].href = 'http://' + domain + '.nyud.net:8080' + links[i].href;
      else
      links[i].href = location.href.replace(/\/[^\/]+$/,'/').replace(domain,(domain+'.nyud.net:8080')) + links[i].href;
      }
      }
      };
      }
      </script>

To use it on your page just save the file as "coralize.js" and upload it to your webserver. Add this to your template's <head> section:

   ::

      <script type="text/javascript" src="/path/to/coralize.js"></script>

And modify your <body> tag like so:

   ::

      <body onload="CoralizeLinks()">

There you go.

And, on an unrelated note, Peyton Manning's dad just said he sent his son a pre-game text message saying how proud he was. It's the future, even for old people!

**UPDATE:** Looks like Coral switched to using port 8080 instead of 8090 a while ago (I have no idea why — they say they're going to `start using port 80 <http://wiki.coralcdn.org/wiki.php?n=Main.FAQ#highport>`__ "as soon as possible"). Port 8090 appears to still work, but I've updated the script anyway. Also, the Coral people appear to use the verb "coralize" instead of "coralify", and I've adjusted the script to reflect that, too.
