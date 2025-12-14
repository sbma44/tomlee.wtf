iphone/nextbus progress
#######################
:date: 2009-07-08 23:54
:author: admin
:category: tech
:slug: iphonenextbus-progress
:status: published
:save_as: 2009/07/08/iphonenextbus-progress/index.html
:url: 2009/07/08/iphonenextbus-progress/

|nextbus on the iphone|\ Nextbus stops! Served by Google App Engine! Displayed on the iPhone!

Of course:

- The app crashes as soon as you try to do anything after the map loads.
- There are way too many pins. And I don't want them to be pins anyway. And the stops aren't likely to change often so I should actually move this operation off the network and onto the iPhone, which might mean reimplementing `geohash <http://en.wikipedia.org/wiki/Geohash>`__, which I don't yet fully understand (but know to be neat!).
- I haven't written code to query Nextbus for predictions. This will be fairly easy, but exactly how I want to handle caching is an open question.

Still: wheels, motion, etc.

P.S. Objective C suuuuuucks

.. |nextbus on the iphone| image:: http://farm3.static.flickr.com/2673/3702613279_5f14faf8ef_m.jpg
   :class: right
   :width: 133px
   :height: 240px
   :target: http://www.flickr.com/photos/sbma44/3702613279/
