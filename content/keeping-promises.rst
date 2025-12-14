keeping promises
################
:date: 2007-03-02 21:25
:author: admin
:category: tech
:slug: keeping-promises
:status: published
:save_as: 2007/03/02/keeping-promises/index.html
:url: 2007/03/02/keeping-promises/

I said I'd have a similarity matrix for you, didn't I? Well, here it is.

|congressional similarity matrix|

The Sunlight Foundation is holding a `mashup contest <http://www.sunlightfoundation.com/mashups>`__, and I've been screwing around with the data they've made available on `opencongress.org <http://www.opencongress.org>`__ to see if there's anything cool that I can do with it.

I started off by scraping every member of congress's voting record, then running a comparison of how similar they were (`this photo <http://www.flickr.com/photos/44137303@N00/406129174>`__ wasn't taken just because I'm pretentious — I had another reason, too). This graph is sort of my way of checking my work so far: it orders members by party, then state, then district. So the block in the upper left represents the democrats, and the one in the lower right is the republicans. The diagonal white line represents where each member is plotted against themselves (they'll always have an identical record, of course, so it's worth blanking this out to show that it isn't valuable data). The brighter the color, the more similar the voting record.

Of course, some members are too new to have cast enough votes to make analyzing them worthwhile, and I haven't bothered to filter them out yet (hence the scattered black dots). And this isn't the interface I intend to use for this data — it's static and visually boring, and unlikely to wow any judges.

But it's still kind of interesting, and you can draw a few conclusions from it (many of which are easier to see in the black & white version, behind the jump). For one thing, you can see that the republicans vote like one another more consistently than the democrats do — as a result, their block is darker (on the black & white graph; it's brighter on the color version, but it's a little hard to compare red pixels to blue ones directly due to how our eyes work). For another, you can see that the bands of dissimilar color are often a few pixels wide (again, particularly among the democrats). These correlate to particular states' delegations that tend to vote unlike their parties. Unsurprisingly, these tend to be folks like Iowa democrats and Texas republicans.

Those are just my initial impressions, though, and I could be misinterpreting something. Tomorrow I'll put up a simple DHTML browser that lets you see which column belongs to which legislator. That should make it easier to see whatever glaring mistakes I've made.

| 
| |image1|

.. |congressional similarity matrix| image:: http://www.manifestdensity.net/2007/03/02/20070302_similarity_matrix_color.png
   :class: center
   :width: 439px
   :height: 439px
.. |image1| image:: http://www.manifestdensity.net/2007/03/02/20070302_similarity_matrix.gif
   :class: center
   :width: 439px
   :height: 439px
