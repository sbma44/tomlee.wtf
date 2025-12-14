geocoding your way to a great vacation
######################################
:date: 2016-07-10 20:46
:author: admin
:category: Uncategorized
:slug: geocoding-your-way-to-a-great-vacation
:status: published
:save_as: 2016/07/10/geocoding-your-way-to-a-great-vacation/index.html
:url: 2016/07/10/geocoding-your-way-to-a-great-vacation/

The road had descended steeply into the valley, and if there was a river anywhere near, it seemed like we would find it soon. There were even a few signs for a dock, but by that time we were suspicious. The people of Skradin would have you believe that their great civic passtime is standing on street corners, wearing t-shirts emblazoned with the letter P and proclaiming the availability of free parking for ferry passengers. It seemed suspicious. Besides, Google told us the ferry was over one more mountain. Nice try, Skradinze.

Our rented VW diesel leapt up the incline, no doubt leaving unimaginable pollutants in its wake. At the bottom of the hill a construction worker made a sort of :no_good: gesture but maybe he was communicating with a colleague behind us? We proceeded onward toward the pin. The road became one way, not too unusual for this part of the world. Some trees were growing into the road; I rolled up my window. Soon the gap became so small that we worried about our mirrors. But the pin urged us on.

Eventually we reached the end of the alley. The walls had closed in. There were a couple of driveways headed up to estates on the hill to our left, so steep that a scooter might tip backward. Backing out looked terrifying: to our right, footpaths ramped down from, then parallel along the road. With no guardrails in evidence, a misplaced wheel could fall into several feet of empty air.

I was panicking, but Steph got out of the car and eventually guided me through a many-, many-point turn (restarted three times). The owner of an adjacent house looked on disapprovingly, convinced with good reason that an idiot was about to crash into her house at low speed.

Obviously you should not ask me for advice about driving when abroad. But thanks to work I can tell you exactly why this happened, and how you can spot the circumstances that might produce similar predicaments for you.

We had geocoded the ferry, plopping its address into an app's text field and relying on the location to which it was matched. Results from such a service can be divided into two levels of quality: *address point* and *interpolated*.

Point geocoding works the way you might imagine. If you put in "150 Main Street", the system finds the coordinates associated with the building at that address and returns them. Exactly what that spot represents can vary. Sometimes it represents the land parcel, sometimes the building's rooftop, sometimes even the entryway.

Point geocoding results are the best kind. But point geocoding datasets are never comprehensive. People build new structures all the time, and it's hard to drop pins for them all in a prompt manner, particularly since address numbers aren't visible from satellite imagery.

So virtually all geocoders fall back to interpolation when they can't find a point to match a query. An interpolated dataset includes a map of road network line segments. Each segment record has the road's name, a start and end number, and whether the odd-numbered addresses go on its right or left side. This lets the system make an informed guess about an address location when no point is available. If a segment named "Main Street" starts at 100 and ends at 200, then a query for "150 Main Street" will be placed at its middle.

This works well a lot of the time. But of course addresses are not spaced perfectly evenly along roads. Some buildings are wider or thinner than their neighbors. Some blocks have several buildings clustered at one end, followed by empty space.

Geocoding data like this is often collected by state or municipal authorities and stitched together into national and international datasets. Those authorities collect it for different reasons: taxes or emergency services or road maintenance, for instance. So it's common to have the level of quality vary by location even within a single country or region.

And quality tends to be worse in rural areas. There are fewer government agencies managing and maybe-digitizing those places. Businesses can't make as much profit from those areas, so there's less money sloshing around to fix problems. And everything is spread out: a so-so interpolation result can be off by a few hundred feet on a city block, or several miles along a farm road.

The interpolation data for our Croatian ferry terminal just wasn't very good. And there probably wasn't any data at all for the small houses that I nearly drove into.

In the abstract, this might not be of much interest to people who don't work on geocoders all day. But it's worth keeping in mind for your next vacation: if you get a result that doesn't land on a rooftop, it might pay to be suspicious of the next results, too. At the very least, I recommend paying close attention to any non-obscene gestures that you see construction workers making.
