some NextBus stats
##################
:date: 2009-07-02 22:26
:author: admin
:category: DC, tech
:slug: some-nextbus-stats
:status: published
:save_as: 2009/07/02/some-nextbus-stats/index.html
:url: 2009/07/02/some-nextbus-stats/

No word yet from WMATA, but I did end up writing a script to grab NextBus's routeconfig data (download `here <http://www.megaupload.com/?d=NUI1B2H8>`__). Then I tried to match each NextBus-defined stop with the closest one in the GTFS dataset. Some stats\*:

- NextBus's dataset tracks 711 unique stop IDs. GTFS has 10,380.
- Using `this <http://stefanobittante.blogspot.com/2007/11/latitude-longitude-distance-in-mysql.html>`__ function to measure distance, the average space between matched stops is 164 feet. The smallest is 11 feet. The largest is 9/10ths of a kilometer.
- 218 NextBus stops wound up sharing the same GTFS stop.

All in all, pretty bad — this level of data quality is clearly unusable. My GIS skills are weak; this may be my own stupid fault. I'll consult with some experts and see what I might be doing wrong. But the basic distance-matching idea is pretty straightforward, so I'm not terrifically optimistic. It's possible that data quality is just going to really, really stink — to be sure, `this <http://dcist.com/2009/07/testing_next_bus_stop_numbers_poste.php>`__ is not particularly encouraging. Here's hoping we can get a proper lookup table out of WMATA or NextBus. Otherwise I don't see a great alternative to manual intervention.

\* These numbers ignore the routes that NextBus tracks but which GTFS does not; those are B99, F99, L99, NH1, P99, REX, S80 and S91 (they appear to be shuttles and the like). I haven't yet identified the routes that are in GTFS but not tracked by NextBus.
