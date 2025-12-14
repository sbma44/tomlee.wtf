intermediate work product! woo!
###############################
:date: 2009-04-19 10:35
:author: admin
:category: DC, misc, tech
:slug: intermediate-work-product-woo
:status: published
:save_as: 2009/04/19/intermediate-work-product-woo/index.html
:url: 2009/04/19/intermediate-work-product-woo/

I've committed myself to getting something ready in time for `Artomatic <http://www.artomatic.org>`__, and that probably means that my GTFS explorations will be delayed for a bit. It's probably for the best, given the timing of the iPhone 3 SDK.

On the other hand, the folks who run the Chinatown bus frown on the use of soldering irons while in transit, so I did spend a little time writing scripts to chew through the dataset. At this point I have 85,921 CSV files delineating exactly where each bus or train is supposed to be on a second-by-second basis during a typical weekday. Well, alright, not exactly: when a unit is between two stops I just interpolate its position linearly — "as the crow flies", in other words. Still, sort of neat. Fun fact: under the current schedule, the last trip of weekday Metro service concludes on exactly the 100,000th second of the day (which is actually part of the next day, but the trip started before midnight).

Anyway, by counting the lines in each file, I was able to generate the following graph. It shows pretty much what you'd expect: there are a hell of a lot of active trips during rush hour. Still, it feels good to have wrangled with a dataset of this size and produced an actual image from it. Also: there must be well over a thousand Metro and Metrobus operators out there! It explains a few things: given those numbers, you can see how it's essentially a statistical certainty that on any given day one of them will `punch someone in a mascot costume <http://dcist.com/2009/03/why_did_a_metrobus_driver_punch_mcg.php>`__.

|Active Weekday WMATA Trips by Time|

.. |Active Weekday WMATA Trips by Time| image:: http://www.manifestdensity.net/skitch/weekday_wmata_trips_by_time-20090419-104847.png
   :class: center
   :width: 521px
   :height: 387px
   :target: http://www.flickr.com/photos/sbma44/3455180905/
