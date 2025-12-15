this is a seriously big deal
############################
:date: 2007-02-08 00:00
:author: admin
:category: tech
:slug: this-is-a-seriously-big-deal
:status: published
:save_as: 2007/02/08/this-is-a-seriously-big-deal/index.html
:url: 2007/02/08/this-is-a-seriously-big-deal/
:private: true

I know that most of my tech posts are completely inscrutable to normal humans. But do me a favor and go read `this <http://feeds.feedburner.com/~r/oreilly/radar/atom/~3/87934065/pipes_and_filte.html>`__ O'Reilly Radar post. I frequently disagree with the level of import that O'Reilly assigns to various web developments, but I actually think he's sort of on the money when he says that "Yahoo!'s new Pipes service is a milestone in the history of the internet." And I haven't even been drinking! Much!

It really is pretty cool. It's a drag and drop interface that lets you perform various web-mashup-y tasks. You can't do anything new with it, but you can do a lot of things much more easily — and with free hosting to boot. This puts the power of the customized web into the hands of everyone.

Here's an example. Let's say that I want to keep tabs on Kriston with just one unified RSS feed. I fire up the Pipes interface, drag a URL-fetching object into the workspace and add the RSS feeds for `Grammar.police <http://www.grammarpolice.net>`__, `Eye Level <http://eyelevel.si.edu>`__ and `FreeRide <http://readexpress.com>`__. I drag in a filter object and draw a connection between the URL Fetcher and plug it into the Filter. Then I set the filter to only allow items where the word "kriston" shows up in either of the author fields (a quirk of different RSS formats) or the description field (where the text of the entries lies). Then I draw a link from the Filter to the output. Presto! I now have `a unified Kriston feed <http://pipes.yahoo.com/pipes/EmbAcDC32xG.HZCot5qdmw/run?_render=rss>`__.

But suppose that I feel that this combined stream of art criticism is too accessible to the rabble. I can go back to my workspace and drag a Babelfish object into it, placing it in between the filter and output blocks. I select the desired languages et voila: Kriston's collective output is now available as an `RSS feed en Francais <http://pipes.yahoo.com/pipes/dkztwTC32xGuH4osphr.og/run?_render=rss>`__.

And this is just relatively simple RSS stuff. You can get into querystring parameters, different data sources, string parsing and control structures like *if..then* blocks and *for* loops. I've only scratched the surface.

There are two downsides, though. First, as O'Reilly mentions, there are some bugs — the interface doesn't work completely predictably. I had to highlight the filter box in order for it to fully populate the dropdown of filterable fields, and the babelfish module seems to miss some of the entries it's sent. Second, it's currently broken: it appears that the whole thing crashed shortly after I played with it (which was very soon after the O'Reilly post). Who knows if it'll ultimately scale. I hope they get things fixed soon, but a framework as powerful as this is likely on the verge of collapsing under its own complexity. I wouldn't count on the kinks being worked out in a particularly expedient manner.
