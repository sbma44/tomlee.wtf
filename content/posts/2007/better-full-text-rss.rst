better full-text RSS
####################
:date: 2007-02-01 16:34
:author: admin
:category: tech
:slug: better-full-text-rss
:status: published
:save_as: 2007/02/01/better-full-text-rss/index.html
:url: 2007/02/01/better-full-text-rss/

Remember `when I asked for help </2006/12/19/do-me-a-favor/>`__ testing a script I'd written that turns partial-text RSS feeds into full-text ones? And it sort of sucked, but not entirely?

Well, I thought about it some more and came up with a way to significantly improve the algorithm. So I took another pass at it (improving the caching mechanism while I was at it) and I'm pretty happy with the results. But I'd like to test it some more before moving it to its final home. If you've got a partial-text feed that's been bugging you, please give it a try. And if it fails to work on any particular feeds, please let me know about them in comments.

.. container::

   .. raw:: html

      <form action="http://www.metamonkey.net/fulltextrss2/" method="get">

   RSS Feed URL

   .. raw:: html

      </form>

**UPDATE:** Looks like the dates on the feeds produced by this tool are screwed up. I'll fix that soon.
