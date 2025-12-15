the march of progress
#####################
:date: 2008-03-10 11:56
:author: admin
:category: music, tech
:slug: the-march-of-progress
:status: published
:save_as: 2008/03/10/the-march-of-progress/index.html
:url: 2008/03/10/the-march-of-progress/
:private: true

`Looks like <http://tinyurl.com/yt7ynq>`__ someone took `my work <http://tinyurl.com/24k82j>`__ as a starting point and make a `hy/pe m Greasemonkey script <http://userscripts.org/scripts/show/23612>`__. It's nice! I wrote an equivalent bookmarklet right after I wrote that post but didn't distribute it. It wasn't as nice as this Greasemonkey script, either — check out the fancy data-URI-encoded icons on this guy! Anyway, get (and use) it now before they rotate encryption keys and break both of em.

It seems slightly silly to me that the free music sampling position we've arrived at is so delicate and tendentious. Everyone's fiercely guarding their bandwidth and ability to deny liability while tacitly admitting the underlying truth: single tracks are now essentially free, priced only by the amount of inconvenience it takes to obtain them — which is primarily a function of which startup has how much remaining money/lawsuits pending against them. It's all pretty dumb.

A suggestion for the idle Flash developers that I'd like to believe are reading this but probably aren't: how about a `PlayTagger <http://blog.delicious.com/blog/2005/11/we_rock_part_2.html>`__-like application with the following capabilities:

#. The ability to take a semicolon-delimited list of URLs for an mp3 link (in the *rel* attribute or similar) and randomly serve one so as to balance load and bandwidth costs.
#. HTTP_REFERER header forging; either automatic (root of serving domain) or user-specified.
#. The ability to scrape HTML pages included in that *rel* list of URLs and find matching mp3 links based on filename or link text comparison.
#. Testing links for 404s/30xs; on error, proceed to the next URL specified.

It should all be pretty simple stuff, except perhaps for the second and last item — I'm not sure how sophisticated ActionScript's HTTP functionality is. And it'd allow linking to mp3 files in a way that's unlikely to break, unlikely to bankrupt the people hosting the files, and that could be automatically generated without too much trouble.
