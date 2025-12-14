better Google Maps/Metro integration
####################################
:date: 2007-07-12 20:23
:author: admin
:category: DC, tech
:slug: better-google-mapsmetro-integration
:status: published
:save_as: 2007/07/12/better-google-mapsmetro-integration/index.html
:url: 2007/07/12/better-google-mapsmetro-integration/

Tech project the first!: I've revisited my venerable `DCist Map <http://www.dcist.com/map>`__ project and ported it over to Google Mapplets — a `just-launched <http://www.techcrunch.com/2007/07/11/google-to-launch-my-maps/>`__ feature that lets you add user-contributed mashups to your Google Map display in a wholly integrated way. This lets you do all kinds of neat stuff. For example, you can turn on a crime overlay by checking the "crime overlay" box. Then you could compare area muggings to gas prices by clicking the "gas price" checkbox. You'll be revolutionizing sociology in no time!

I've dusted off my code and ported it to the Mapplet version of the GMaps API, which actually entailed porting it to the GMaps v2 API first. It's nice of them to have finally un-switched latitude and longitude, but it made things kind of a pain in the ass for me. Still, it's nice to have it done and the tool up-to-date. Oh, and while I was at it I finally extended the yellow line up to Ft. Totten, as I should've long ago.

I've submitted the mapplet to Google's directory, but who knows when or if they'll add it. For now, if you want to add it to your "My Maps" toolbox, you can do so in the following way. You'll only have to do this once, then it should sit happily in your sidebar, waiting for you to toggle it on whenever you need it.

#. `Launch the mapplet-enabled version of Google Maps <http://maps.google.com/maps/mm?mapprev=1>`__ (it's still in beta).
#. Click on "Add content" in the upper left of the "My Maps" section.
#. To the right of the search bar at the top of this page is a tiny little link that says "Add by URL". Click it.
#. Enter "http://dcist.com/map/mapplet.xml". Note the lack of www! The Gothamist folks have set up the hostname to redirect to the www-less version, but Google isn't smart enough to handle that. Enter it like this and you'll be fine. Click "Add".
#. Say "OK" to the security warning that'll pop up. Trust me, I'm a nice guy.
#. Follow the "Back to Google Maps" link in the upper left of the screen.
#. That's it! You should have a new item in the "My Maps" section. Check the box next to it and the metro overlay will be activated.

I'll write up a post for DCist about this tomorrow (or maybe I'll wait to see if it's accepted into the directory). But I thought I'd put it up here first, so that you guys can give it a try and let me know if you run into any horrible problems.

**UPDATE:** One other interesting side-effect: this makes it easy to see where Google and I disagree about a Metro station's location. In most cases this is because the station has multiple entrances; I usually went with whichever one was most visible. In others its because of different standards: I generally used the satellite view to find the platform and geocoded that (yeah, I did them all manually). Google appears to use street entrances. I'd consider redoing them, but it'd mostly be for pride — having both on there is (arguably) the best solution.
