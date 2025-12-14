cheaper automation magic
########################
:date: 2007-06-04 13:11
:author: admin
:category: tech
:slug: cheaper-automation-magic
:status: published
:save_as: 2007/06/04/cheaper-automation-magic/index.html
:url: 2007/06/04/cheaper-automation-magic/

`Via uC Hobby <http://www.uchobby.com/index.php/2007/06/04/free-arduino-microcontroller-kits/>`__ I see that `Modern Device <http://www.moderndevice.com/>`__ is offering cheap Arduinos, a microcontroller platform that makes building tiny embedded computers easy and affordable.

Previously the only place I knew for acquiring Arduinos was `Spark Fun <http://www.sparkfun.com/commerce/advanced_search_result.php?keywords=arduino&x=0&y=0>`__. And although I like Spark Fun a lot, the $40ish price tag for an Arduino had me eying the possibility of learning how to directly program and use the AVR microcontrollers that make up the Arduino's heart, without using the other features that the Arduino platform makes available. $40 is a considerably bigger outlay for a pointless home automation project than an AVR (which only costs a few dollars) and some components I already have lying around.

But Modern Device seems to have realized some savings by pulling the USB-to-serial chip off the Arduino board and counting on it being in the programming cable. There's something to be said for having it on-board the chip — if you want your Arduino project to talk to a PC, you'll want the USB-to-serial interface to always be present. But if you're building an embedded device that stands on its own, there's no need for that functionality except when you're loading your program.

Of course, all of this is possible because the Arduino is an `open source platform <http://www.arduino.cc>`__. Here's hoping they keep gaining marketshare and driving down prices. Competitors like Parallax may offer chips with more capabilities, but they're proprietary and more expensive. And given the low cost of full-blown PCs these days, the returns on adding functionality to a general-purpose hobbyist microcontroller begin to diminish *very* rapidly. There's just not much point in `building speech synthesis <http://makezine.com/10/propeller/>`__ into a relatively hard-to-use uC when a `complete <http://www.acrosser.com/Product/Embedded%20PC/3.5%20Biscuit%20SBC/sbc_eden_b1651.html>`__, tiny `embedded PC <http://gumstix.org/>`__ can be had for a little over $100.
