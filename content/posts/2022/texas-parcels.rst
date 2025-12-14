texas parcels
#############
:date: 2022-10-05 14:28
:author: admin
:category: Uncategorized
:slug: texas-parcels
:status: published
:save_as: 2022/10/05/texas-parcels/index.html
:url: 2022/10/05/texas-parcels/

.. container:: float wp-block-image

   |parcels|

At the start of the pandemic, a friend asked me if I could help with a problem. His organization studied educational institutions: what kind of people they serve and whether they do a good job of serving them. He wanted to look at the accessibility of these places: how many people, and what types of people, could reach them by foot, car, or transit?

This was an interesting problem and, given my work in the mapping industry, one I knew how to solve. I got my boss to say it was okay to lend a hand, and then embarked on what turned out to be an expansive side project--one that I hope will prove useful to other analysts doing work in Texas.

We examined colleges in Houston. Who could get to them, and how easily? I got the geographic coordinates for the colleges along with metadata about whether they were public, private, for-profit--a bunch of different dimensions. I took those coordinates and used them to make isochrones. These are funny-looking polygons that circumscribe the area that's reachable from a starting point in a given number of minutes, using a given transportation mode. For cars and walking, `good API options exist <https://docs.mapbox.com/playground/isochrone/>`__. For transit, I had to set up my own, but this was pretty simple thanks to `OpenTripPlanner <https://www.opentripplanner.org/>`__ and the availability of GTFS data. I intersected these isochrone polygons with Census data and began to look at the result. This is where the real work started.

Census data is imprecise (and `getting more so <https://www.bloomberg.com/news/articles/2021-08-12/data-scientists-ask-can-we-trust-the-2020-census>`__). Obvious problems appeared when I looked at how isochrones intersected with Census polygons. Say an isochrone's tip touches the edge of a Census tract. Do I count the whole tract's population? Do I divide it somehow? What if the part it touches is water in a lake? I hadn't calculated isochrones for canoeing.

What I wanted was to know where people lived inside the Census tracts. Of course that information isn't available, for excellent privacy reasons. But what about just differentiating the part of the tract that's residences from the part that isn't, then dividing the tract's population among that area? Surely that would go a long way to resolving my lake/isochrone problem.

This turns out to be possible--in Texas, at least. The state legislature's 1979 "Peveto Bill" tax reform implemented `a system of appraisal districts <https://bancad.org/the-history-of-your-local-appraisal-district/>`__. These entities vary widely in their specifics, online presence, and tech savviness, but so far I have found that their existence guarantees three things:

- There will be a geodata file of land parcels for the county, somewhere, and each parcel will have a unique ID.
- There will be a tax roll dataset for the county, somewhere, that connects to parcel IDs, somehow. It will probably be a horrible fixed-column-width file that arrives without any documentation, unless you count filenames, and you might need to email or call some bureaucrats to get it.
- The tax roll will classify each parcel using one of several versions of `a statewide land use taxonomy <https://tax-office.traviscountytx.gov/pages/SPTC.php>`__ and will do so with varying levels of rigor. But for a given county it will be mostly possible to figure out which parcels are residential.

After much emailing, calling, squinting at data, and scripting, I was able to generate a set of residential parcels for the greater--much greater--Houston area. In the end we had data collected and joined up for Austin, Brazoria, Brazos, Chambers, Colorado, Fort Bend, Galveston, Grimes, Harris, Liberty, Matagorda, Montgomery, San Jacinto, Walker, Waller, Washington, and Wharton counties. I am releasing all of that data and code `here <https://github.com/sbma44/houston-parcels>`__. You can read a more complete account of the project in the `README <https://github.com/sbma44/houston-parcels/blob/main/README.md>`__ and `METHODOLOGY <https://github.com/sbma44/houston-parcels/blob/main/METHODOLOGY.md>`__ documents.

I hope it will be useful to someone. I haven't done much work to make the repo into a properly-organized open source release. That's because the software is nothing special. What's worthwhile here is the effort that went into collecting and connecting the data. If you are trying to answer geospatial questions in Houston specifically or Texas generally, and wish that you could answer them with more precision, this may be very interesting to you.

What about the original project? Well, we had a whole draft going. I hesitate to speculate about what happened. Personnel moved on, and frankly our methodology was a lot more exciting than our results (Cars are useful! White people live in exurbs and rich white people live downtown! Houston's transit system is not talked about by urbanists all that much!).

It was a nice chance to write some bash, bash some open data, then turn it all back into writing. If I or it can be of any use to you, I hope you'll get in touch.

.. |parcels| image:: https://github.com/sbma44/houston-parcels/raw/main/img/parcels2.png?raw=true
