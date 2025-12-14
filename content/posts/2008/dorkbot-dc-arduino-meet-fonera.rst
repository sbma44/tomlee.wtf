Dorkbot DC: Arduino, Meet Fonera
################################
:date: 2008-03-26 12:05
:author: admin
:category: DC, tech
:slug: dorkbot-dc-arduino-meet-fonera
:status: published
:save_as: 2008/03/26/dorkbot-dc-arduino-meet-fonera/index.html
:url: 2008/03/26/dorkbot-dc-arduino-meet-fonera/

Whew! Well, I presented last night at Dorkbot and it seemed to go pretty well. Thanks to Gareth, Alberto and everyone else who makes Dorkbot possible. Alberto was particularly helpful and encouraging, and I greatly appreciate it.

As promised I've got an audio recording of the talk to share, as well as a PDF of my slides and some Arduino and Ruby code. I haven't yet taken any really good photos of my project, but once I do I'll add some links to them here.

For those just wandering in: I spoke about using a router with a custom firmware as a way of adding wireless internet access (and more!) to your Arduino project. In particular I used the Fonera router, which is especially ubiquitous and cheap. Once you've got a custom firmware loaded you can use a simple serial link to make the router speak to your Arduino and relay whatever internet goodness you might like. I used this functionality to create an ambient display that talks to the `WMATA website <http://www.wmata.com/tripplanner_d/TripPlanner_Form_Solo.cfm>`__ via wifi and uses a couple of needle gauges and LEDs to tell me when the next bus and train will be arriving at the stops nearest my apartment.

   | **Dorkbot DC: Arduino, Meet Fonera**
   | `Audio (MP3/64kbps, 11M) <http://manifestdensity.net/2008/03/26/dorkbot_arduino_and_fonera/dorkbot_tom_64_mono.mp3>`__
   | `Slides (PDF, 10M) <http://manifestdensity.net/2008/03/26/dorkbot_arduino_and_fonera/dorkbot-tom_lee-arduino_meet_fonera.pdf>`__
   | `bus_o_meter.pde (Arduino code, 3.2k) <http://manifestdensity.net/2008/03/26/dorkbot_arduino_and_fonera/bus_o_meter.pde>`__
   | `wmatarideguide.rb (Ruby class, 1.6k) <http://manifestdensity.net/2008/03/26/dorkbot_arduino_and_fonera/wmatarideguide.rb>`__

The rest of the project code is available inside the slides. You can find some useful hyperlinks in there, too, as well as my email address.

**UPDATE:** The original version of the Arduino project code uploaded here contained a number of critical bugs. I've replaced it with a more complete version, but it should still be considered a work in progress.
