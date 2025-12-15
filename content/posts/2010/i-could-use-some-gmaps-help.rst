I could use some GMaps help
###########################
:date: 2010-06-06 13:19
:author: admin
:category: tech
:slug: i-could-use-some-gmaps-help
:status: published
:save_as: 2010/06/06/i-could-use-some-gmaps-help/index.html
:url: 2010/06/06/i-could-use-some-gmaps-help/
:private: true

Way back when, I wrote a `Google Maps application <http://dcist.com/map/>`__ for `DCist <http://www.dcist.com>`__ that overlaid the DC Metro system on the usual GMaps tiles. People found it useful -- me especially, since I think it helped me land a job at `EchoDitto <http://www.echoditto.com>`__.  Its only real innovation was some simple, hacked-up geometry that would horrify a cartographer, but which allowed me to make an attractive map that recalled `the more stylized WMATA map <http://wmata.com/rail/maps/map.cfm>`__.  It wasn't rocket science, but I still occasionally get emails from developers asking me how I did it (which is slightly bizarre, given that the code is right there for them to see).

In 2007 the GMaps API got an update, and `I converted the project into something called a mapplet <http://dcist.com/2007/07/13/dcist_maps_come.php>`__. I had to rewrite a few things, but it was more or less the same.  The main difference was that mapplets were used through the maps.google.com interface -- you could add a bunch at the same time, but you could still use Local Search and permalinking and comments about businesses and other Googly innovations from within the interface.  I didn't have to implement any of that stuff!  Instead, users could simply have their polished Google Maps experience supplemented by my modest mapplet.  Handy.

Unfortunately, over the last few weeks I've started receiving reports that the mapplet's behaving weirdly.  Load the mapplet, then do a search for something -- the station markers will disappear, and sometimes some of the lines that are supposed to connect them will, too.  It looked to me like an event handler had started working differently, so I went to investigate.

Alas!  It turns out that v2 of the API has been deprecated.  They're on to v3 (not so bad) and they've discontinued the mapplet platform entirely (bad)!

I can still make the lines appear on a Google Map.  But I don't think I can do it on the maps.google.com interface.  This is a drag: I don't think the thing's half as useful as a standalone product as it is when it supplements search functionality.  And I really don't want to reimplement the entire maps.google.com interface (even though, yes, they expose the API for their local search stuff).

So! Developers! Anyone out there dealt with this? I'm not eager to dump a huge amount of time back into this project -- a project that's increasingly unnecessary thanks to Google Transit and the addition of transit stations to the GMaps tileset, but which is still useful when you're working at a modestly wide zoom level.  But it would be nice to get things working again.
