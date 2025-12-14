boarduino!
##########
:date: 2008-04-16 16:28
:author: admin
:category: tech
:slug: boarduino
:status: published
:save_as: 2008/04/16/boarduino/index.html
:url: 2008/04/16/boarduino/

|boarduino!|

On Tuesday night I successfully assembled a `Boarduino <http://ladyada.net/make/boarduino/>`__ kit for the first time. I had tried once before and accidentally swapped the two electrolytic capacitors — whoops. But I placed an order for a couple more kits, and their creator, Lady Ada, was even nice enough to send an extra one my way. Thanks!

The Arduino, as you might know from my earlier ramblings, is a microcontroller doohickey that can run tiny programs and read and write signals from its twenty or so connections. It can also talk to your computer over USB.

The Boarduino is pretty much the same thing. This is one of the benefits of the Arduino being an open platform: it can be freely copied. The Boarduino is just as open, as Lady Ada provides downloadable schematics that you can use to print your own circuit boards if you'd like.

There are a few differences between the Boarduino and a standard Arduino, though. First, it looks very different. That's because it's designed to be plopped into a breadboard, which is a commonly used mechanism for wiring up prototype circuits without soldering anything. Second, it's sold as a kit that has to be `assembled and soldered <http://ladyada.net/make/boarduino/solder.html>`__, which makes it cheaper. Third, it moves the chip that translates from USB to serial (which the Arduino chip can understand) into a reusable cable instead of keeping it on the Arduino, which makes it cheaper still. This means that for applications where a connection to a computer is important, the Boarduino doesn't make that much sense.

But if your application stands on its own and you don't mind spending some time soldering the Boarduino is a great option. And a kit only costs $17.50 — about half as much as an assembled, full-featured Arduino.

.. |boarduino!| image:: http://farm3.static.flickr.com/2251/2419562126_0c376d29da.jpg
   :class: center
   :width: 500px
   :height: 375px
   :target: http://www.flickr.com/photos/sbma44/2419562126/
