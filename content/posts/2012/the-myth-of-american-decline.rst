the myth of American decline
############################
:date: 2012-12-21 00:18
:author: admin
:category: Uncategorized
:slug: the-myth-of-american-decline
:status: published
:save_as: 2012/12/21/the-myth-of-american-decline/index.html
:url: 2012/12/21/the-myth-of-american-decline/

Being the crotchety old man that I am, the time I spent this evening on my gym's treadmill left me feeling cantankerous. I had been watching Jeopardy, and all of the categories seemed horrible, dagnabit. Back in my day we didn't have questions about sitcoms! No, it was all Latin, and poetry, and similarly high-minded pursuits.

Then I got home and remembered I had a bunch of code left over from when we built `this thing <http://sunlightfoundation.com/blog/2011/12/08/remembering-richard-cordray-nominee-and-jeopardy-champion/>`__. See, there is a terrifying website called `j-archive.com <http://j-archive.com>`__. It's maintained by former players, and it comprehensively chronicles every game of Jeopardy.

It's possible to scrape this site to reconstruct games, which is what I did for the Cordray infographic. With this as a starting point, figuring out the percentage of categories devoted to television versus weightier topics was a relative cinch. I was absolutely confident that I would find a line snaking smoothly upward. Here are the regular expressions I used:

| [cc]RE_TV = re.compile(r'(T\\.?V\\.?|TELEVISION|SITCOM)', re.I)
| RE_BIBLE = re.compile(r'BIBL(ICAL|E)', re.I)
| RE_HISTORY = re.compile(r'(PRESIDENT|HISTORY|HISTORICAL)',re.I)[/cc]

And here's the graph that resulted (normalized by total number of categories in a season):

|image1|

Gotta say, I didn't see this one coming. I guess the nerds are (mostly) all right after all. Alex Trebek's still kind of a supercilious asshole, though.

Anyway, I'm open to other suggested analyses. Lay 'em on me.

 

.. |image1| image:: http://www.manifestdensity.net/wp-content/uploads/2012/12/Screen-Shot-2012-12-21-at-12.02.03-PM.png
   :class: aligncenter size-full wp-image-2290
   :width: 628px
   :height: 425px
   :target: http://www.manifestdensity.net/wp-content/uploads/2012/12/Screen-Shot-2012-12-21-at-12.02.03-PM.png
