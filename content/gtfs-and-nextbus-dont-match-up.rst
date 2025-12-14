GTFS and NextBus don't match up
###############################
:date: 2009-07-01 22:00
:author: admin
:category: tech
:slug: gtfs-and-nextbus-dont-match-up
:status: published
:save_as: 2009/07/01/gtfs-and-nextbus-dont-match-up/index.html
:url: 2009/07/01/gtfs-and-nextbus-dont-match-up/

NextBus launched! It's exciting. I and a lot of other area developers are looking at how to take advantage of the realtime GPS data that NextBus collects to make the DC transit system easier to use. I haven't gotten too far with it — I'm just poking around — but the early word is that NextBus isn't going to make this easy.

First: they're claiming copyright on the location of metrobuses. They serve their data as XML, and each <body> tag looks like this:

   ``<body copyright="All data copyright NextBus 2009. Allowed use is for noncommercial purposes only.">``

Not great. But okay, whatever — whether this data is copyrightable in a meaningful sense is the first question; whether WMATA willingly sold off their bus locations is the second. But realistically, NextBus can apply whatever license terms on their service that they'd like, and can plausibly enforce them against commercial users. So that'd bring us back to where we are, which is fine.

But just because NextBus says it's *okay* to have the data doesn't mean they're going to make it easy. Your browser makes a lot of requests to NextBus in order to show a map, of course, but the most interesting ones are to http://wmata.nextbus.com/service/googleMapXMLFeed, a script that performs a number of different operations based on what querystring parameters it's passed. For instance, http://wmata.nextbus.com/service/googleMapXMLFeed?command=routeConfig&a=wmata&r=64&key=1424073267381 will get you a list of stops and route geometry for the 64 bus.

But if you paste that URL into your browser, you'll get this:

   | ``<Error shouldRetry="false">``
   | ``  Feed can only be accessed by NextBus map page.``
   | ``</Error>``

Charming. But of course it works in the context of the map. So we need to figure out what the difference is. `Here's </2009/07/01/nextbus_headers.txt>`__ a complete conversation between my browser and NextBus. And here's a specific request that worked for that URL:

   | ``http://wmata.nextbus.com/service/googleMapXMLFeed?command=routeConfig&a=wmata&r=64&key=1424073267381``
   | ``GET /service/googleMapXMLFeed?command=routeConfig&a=wmata&r=64&key=1424073267381 HTTP/1.1``
   | ``Host: wmata.nextbus.com``
   | ``User-Agent: Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.0.11) Gecko/2009060214 Firefox/3.0.11``
   | ``Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8``
   | ``Accept-Language: en-us,en;q=0.5``
   | ``Accept-Encoding: gzip,deflate``
   | ``Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7``
   | ``Keep-Alive: 300``
   | ``Connection: keep-alive``
   | ``Referer: http://wmata.nextbus.com/googleMap/customGoogleMap.jsp?a=wmata&cssFile=http://www.wmata.com/css/nextbus.css``
   | ``Cookie: userProfile_rev1=wmata|A11|A11_A11_0|7067|8166&wmata|64|64_64_0|16797|7073&wmata|64|64_64_0|6454|16793&; __utma=222659997.501906468.1246378684.1246395595.1246496449.3; __utmz=222659997.1246496449.3.3.utmccn=(referral)|utmcsr=wmata.com|utmcct=/rider_tools/nextbus/arrivals.cfm|utmcmd=referral; userID_rev4=5534021; __utma=64696752.769952994.1246496428.1246496428.1246496428.1; __utmb=64696752; __utmc=64696752; __utmz=64696752.1246496428.1.1.utmccn=(organic)|utmcsr=google|utmctr=nextbus+wmata|utmcmd=organic; Coyote-2-407c7b2d=c0a80a66:0; JSESSIONID=53015434E8CF00D3FEC91D4B491FFA08; __utmb=222659997; __utmc=222659997``

It actually can't be that many things. There's the set of session-maintaining cookies, the HTTP referrer header, and the user agent reported by the browser (or some combination). Spoiler alert: it's the referrer. So! Borrowing the referring URL from the headers (it checks for more than just the domain), we can use *curl -e"http://wmata.nextbus.com/googleMap/customGoogleMap.jsp?a=wmata&cssFile=http://www.wmata.com/css/nextbus.css" "http://wmata.nextbus.com/service/googleMapXMLFeed?command=routeConfig&a=wmata&r=64&key=1424073267381"* and get back `this file </2009/07/01/routeconfig.xml>`__.

It's got three things in it: stops; routes, which are ordered lists of stops; and paths, which define the shape of the lines that'll be drawn to represent the routes (because roads have twists and turns, connecting stops with straight lines is insufficient).

This is pretty much how the GTFS dataset is organized. So you might expect to be able to match up the stops from GTFS to NextBus. Well, here's a stop from NextBus:

   ``<stop tag="5880" title="11th St Nw + H St Nw" dirTag="null" lat="38.90032" lon="-77.02657" stopId="1001159"/>``

Here's the same stop from a fresh download of the WMATA GTFS dataset:

   ``7591 / NW 11TH ST & NW H ST / 38.899812 / -77.027053``

It's a drag. The IDs don't match. The human-readable stop names don't match. *Even the latitude and longitude don't match*. I mean, sure, they're close. But making these line up is going to be a sloppy, relatively expensive calculation. Now, true, it probably only has to happen once. It's not that hard of a problem. It's just that it's so *unnecessary*. Ah well. I've got an email in to Metro; we'll see if they can provide a cleaner solution than the one I'm thinking about scripting up.

**UPDATE:** `Some thoughts on NextBus's javascript interface from 2006 <http://blog.case.edu/gps10/2006/01/30/debugging_nextbus>`__. A few things have changed since then, but from my initial investigation I'd say that not *too* much is different — just URLs, mostly.

An alternative to messing with the protected javascript interface is to scrape the HTML for the "next arrival time" pages. But a) this only gets you distance-expressed-as-time, which is lousy data compared to actual lat/lon coordinates and b) it's still messy, as "`apparently NextBus hired a live bear to write their markup <http://mihasya.com/blog/?p=203>`__" (the author of that post does have his `scraping code up on GitHub <http://github.com/mihasya/yourmuni/tree/master/>`__, though).
