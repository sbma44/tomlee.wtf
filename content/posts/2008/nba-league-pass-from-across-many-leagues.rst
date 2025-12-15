NBA League Pass, from across many leagues
#########################################
:date: 2008-01-23 11:34
:author: admin
:category: tech
:slug: nba-league-pass-from-across-many-leagues
:status: published
:save_as: 2008/01/23/nba-league-pass-from-across-many-leagues/index.html
:url: 2008/01/23/nba-league-pass-from-across-many-leagues/
:private: true

A couple of days ago `Kriston <http://grammarpolice.net>`__ hit me up with a question on behalf of `Matt <http://www.mattwrightphotography.blogspot.com/>`__, who's in Germany and found himself stymied by NBA League Pass Broadband's insistence that he be in America in order to watch the games he'd paid for. I suggested he give `Tor <http://tor.eff.org>`__ a try and hey! Somewhat to my surprise, it actually worked. For those of you facing similar problems, here's Matt's advice:

   | Tom, great recommendation on Tor. It's not 100% perfect, but I've found a way to do what I need to do. The key is that you can view the Tor Network Map and monitor where the final Relay, as they call it, is located. For my specific problem I just had to make sure that last relay was in the U.S.
   | More specifically, to get it to work, I just had to keep trying connections until the series of relays ended in a computer in the U.S. Then I just loaded the NBA League Pass Broadband, it thought I was from the States, and I was able to launch the streaming RealPlayer app. The quality of the feed seemed to synch up with the bandwidth readings I was getting from Tor -- it was still slow, mind you, but if all three of my Relays had high bandwidth, the streaming video worked fine. It also proved to be a good idea to leave the connection uninterrupted (you can switch from one live game to another normally), in case Tor switched Relays on you.
   | A `screenshot <http://flickr.com/photos/sbma44/2214835428/>`__ is attached. This technique is also probably really useful when trying to stream radio over the internet. I've run into similar problems out here where stations weren't allowed to stream their station outside the U.S. Don't ask me why.
   | Oh, and for Tor to have been perfect, the feature I would've liked is to be able to specify which country was the final chain in the Relay, obviously, instead of a guess and check method.

If you're running into similar problems, it might be worth giving this a try. But Tor isn't anything magic. In this context it's just an unusually slow (and unusually reliable) proxy server — it encrypts everything and sends it through multiple servers to better ensure anonymity, which slows everything down. You can try to find a `single-hop <http://www.samair.ru/proxy/>`__ proxy for better performance (be sure to pick one in the right country), but it may take some effort to find one that works: it's safe to assume that most of the proxies on that list don't know their systems are open to relaying traffic from the world. The proxies tend to disappear as their owners become aware that they're being used.

In either case you'll end up needing to edit your network settings so that they include the address of the HTTP or SOCKS proxy (depending on which type of server it is — HTTP's more common, SOCKS can handle more types of applications). Exactly where to do this may vary. Standalone apps like Realplayer or IM will likely have their own settings. Things like Flash will probably inherit your browser's proxy settings (`here's <https://addons.mozilla.org/en-US/firefox/addon/125>`__ a handy Firefox extension for changing proxy settings quickly). In some cases you might need to hunt down your operating system's network settings and make the change there. You can find more detailed instructions `at the Tor project <http://tor.eff.org>`__.

But where ever you need to make the change, it's a useful technique to know. Proxies are the best, simplest way to hide where your traffic is coming from (from private system owners — you certainly shouldn't count on it for anything more serious, particularly if you don't know who's running the proxy/Tor exit node; nor should you send any sensitive information across such a link unless using a free-of-error-warnings SSL session). Whether beating DRM, stuffing an online ballot box or leaving an intemperate blog comment, this is something that the enterprising web user will find handy surprisingly often.
