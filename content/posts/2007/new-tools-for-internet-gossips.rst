new tools for internet gossips
##############################
:date: 2007-01-25 12:13
:author: admin
:category: tech
:slug: new-tools-for-internet-gossips
:status: published
:save_as: 2007/01/25/new-tools-for-internet-gossips/index.html
:url: 2007/01/25/new-tools-for-internet-gossips/
:private: true

I've begun screwing around with my attempt at a larger-buffer Hype Machine player, and became aware of HTTP dereferers in the process. Want to provide a link to a site, but not have the site's owner track it back to you? Then use one of these things.

Here's an example. First, the normal link, which will go to a page showing your HTTP referer information on the third line from the top:

   http://c2.com/cgi/test/

and now the same link, passed through a dereferer:

   http://ultimod.org/?url=http://c2.com/cgi/test/

Handy!

Of course, it's no help on my particular project — what I was actually looking for was a proxy that will spoof my HTTP referer string on the fly. Unfortunately, referer spoofing seems to be constrained to the realm of the browser plugin (it's commonly used to get free porn from protected sites), and even the excellent `Squid Proxy <http://www.squid-cache.org/>`__ doesn't seem to have this functionality (or at least it's not written up in an easy-to-find manner). But I think I can get by without this workaround.
