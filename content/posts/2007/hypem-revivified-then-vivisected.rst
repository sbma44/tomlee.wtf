hype/m: revivified, then vivisected
###################################
:date: 2007-10-16 14:49
:author: admin
:category: tech
:slug: hypem-revivified-then-vivisected
:status: published
:save_as: 2007/10/16/hypem-revivified-then-vivisected/index.html
:url: 2007/10/16/hypem-revivified-then-vivisected/

There's a new version of the Hy/pe Mac/hine! Cool. The mp3 blog aggregator's gotten a new coat of paint and a different flash player. It looks pretty nice, although I'm not entirely sure what substantive changes have been made. Nevertheless, it's at least much more t-shirt-compatible.

I decided to celebrate the occasion by digging into the workings of the site a bit more. Hype/m provides a lot of music but is understandably hesitant to provide direct downloads lest they be busted by The Man. But how do you go about providing an mp3 for listening but not for saving? It's as fundamentally unsolvable as any other DRM problem — more so, given the relatively open technologies that the site uses.

Still, they do their best. For instance, only requests from known web browsers are allowed — try to use a command-line tool like wget or curl to fetch content and you'll get an ACCESS DENIED message. But it's easy to fake user agent strings (or just to do the dirty work within your browser). Consequently, this isn't the only security that the site employs.

Let's have a look at the anatomy of playing a song on hypem:

#. You click the play button next to a track.

#. | An AJAX request is sent that looks something like this:

      http://hypem.com/inc/serve_nowplaying.php?id=\ **401678_1**

   The part in bold is an identifier that's unique to the song you requested.

#. | Some HTML is sent back and placed in the portion of the page where the play button used to live. It looks like this:

      ::

         <object class="play" classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=7,0,0,0" width="36" height="18">
         <param name="movie" value="http://hypem.com/h2p.swf?autoplay=true&url=N2NjZGZkYTJkMjc0ZTZmNGY3OTVmNmQ0Mzg4MTEzYTVjMTgyM2NhY2ZmYzI2ZTAyMzE2MGIwMDY1NjJmOTA5MTJlMzE1ODA5MzYyYzBjODJiYjdjODBhNGI0ZDIwODkyMDRhNTQ3M2U4OWQwOGE2Mjk5YjQ1MWRjMjk1ZjFkNTlmYmIyZWIwZmU5YThlMDU1">
         <param name="wmode" value="transparent">
         <param name="quality" value="high">
         <embed src="http://hypem.com/h2p.swf?autoplay=true&url=N2NjZGZkYTJkMjc0ZTZmNGY3OTVmNmQ0Mzg4MTEzYTVjMTgyM2NhY2ZmYzI2ZTAyMzE2MGIwMDY1NjJmOTA5MTJlMzE1ODA5MzYyYzBjODJiYjdjODBhNGI0ZDIwODkyMDRhNTQ3M2U4OWQwOGE2Mjk5YjQ1MWRjMjk1ZjFkNTlmYmIyZWIwZmU5YThlMDU1" quality="high" wmode="transparent" pluginspage="http://www.macromedia.com/go/getflashplayer" type="application/x-shockwave-flash" width="36" height="18"></embed>
         </object>

   This code tells the browser to load an Adobe Flash object called *h2p.swf* and pass it parameters telling it A) to start playing immediately (*autoplay=1*) and B) where to find the mp3 that it should play. This is accomplished via a mysterious *url* parameter, which I've highlighted in bold in the HTML above.

#. | Using the `LiveHTTPHeaders <http://livehttpheaders.mozdev.org/>`__ plugin for Firefox, we can see that the flash video then requests a file named something like:

      http://hypem.com/serve/f/509/401678/f48c7f07a821a8fc528842d0bd8d3029.mp3

   That's straightforward enough. But how does it get that long URL from the even-longer *url* querystring parameter that's passed to the Flash movie?

To find out, we've got to take a look inside the seemingly black box of the flash movie. Fortunately there's a great tool that lets us do that: `Flare <http://www.nowrap.de/flare.html>`__, which is free, cross-platform, and will happily extract the ActionScript from a Flash movie. I grabbed the h2p.swf file and passed it to Flare. Here's the interesting part of what I got back:

   ::

      this.m = new mp(this, com.meychi.ascrypt.RC4.decrypt(com.meychi.ascrypt.Base64.decode(_root.url), 'abcdef1234567890'));

Hello there... looks an awful lot like a decryption routine... and something that looks suspiciously like a decryption key! This line takes the aforementioned *url* querystring parameter, Base64-decodes it, then passes it to an RC4 decryption routine along with the decryption key *abcdef1234567890* (not the actual key). This turns the *url* parameter into a usable URL, which the flash player then fetches.

The meychi.ascrypt library's website is offline, but a little digging into its code (also returned by Flare) shows that, unlike most RC4 decryption libraries, it expects to receive a string of hexadecimal bytes which it first converts into a string of chars before applying the RC4 decryption algorithm. The need for this extra step had me scratching my head for a while, but eventually I figured out what was going on and cobbled together the following script to replicate the functionality. It's in Perl, since I couldn't find any RC4 routines in Ruby.

   ::

      #!/usr/bin/perl
      use MIME::Base64;
      use Crypt::RC4;
      # hype mac/hine's secret encryption cipher... shhh!
      $passphrase = 'abcdef1234567890';
      if($src = <>)
      {
      # decode the URL-safe parameter from base64
      $unencoded_src = decode_base64($src);
      # convert decoded input from hexadecimal bytes to a string of chars
      $charred_ciphertext = '';
      while(length($unencoded_src)>0)
      {
      $char = substr($unencoded_src, 0, 2);
      $charred_ciphertext .= chr(hex($char));
      $unencoded_src = substr($unencoded_src,2);
      }
      # decrypt with RC4 algorithm
      print RC4($passphrase,$charred_ciphertext);
      }

Pipe the *url* querystring parameter to that script and it'll spit out the URL of the actual file. Paste that into your browser and you'll be redirected to the file's actual location — your browser will begin downloading it quite happily.

Of course, this is all kind of a huge pain in the ass. It's much easier to follow the link to the blog where hype/m first found the mp3 and keep your fingers crossed that the original link is still alive. But! If you could just find Javascript libraries for `Base64 encoding <http://www.webtoolkit.info/javascript-base64.html>`__ and `RC4 decryption <http://home.versatel.nl/MAvanEverdingen/Code/>`__ you could make a bookmarklet or Greasemonkey script that automatically adds a direct download link to every hype/m entry. Hmmmmm.

Anyway, I should probably finish by saying that none of this should be taken as an indictment of the hype/m programmers' skills. The Hype Ma/chine is a truly impressive piece of software, and the countermeasures its creators have implemented to prevent direct downloading are pretty much everything I can think of doing. The problem is simply that allowing a user to hear content but not store it is an impossible task. And keeping secrets hidden in Flash — which is the only appropriate technology for this application — is similarly impossible, making whatever obfuscation they employ relatively easy to unravel.

The only improvement I can think to make would be to rotate encryption keys by serving a variety of different player SWFs, and invalidating an mp3's URL as soon as an incorrect key is used (I assume that the URLs produced by my script are temporary redirects that rotate fairly frequently and can be expired as necessary). This way a user couldn't cycle through the known keys. As far as I know, decompiling an SWF is not something that can be accomplished in Javascript.

But it probably *could* be done within a full-on Firefox plugin. And given browsers' enthusiasm for caching Flash (and Javascript's ability to easily differentiate SWFs with different names), the above proposal might not be a viable approach at all. Really, there's no way to completely secure this system. "Good enough" is all that one can reasonably hope for, and I think they've already achieved that.

*Cross-posted at* `EchoDitto Labs <http://labs.echoditto.com/hypem>`__
