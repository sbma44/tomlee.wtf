desperately seeking serial
##########################
:date: 2008-04-18 18:01
:author: admin
:category: tech
:slug: desperately-seeking-serial
:status: published
:save_as: 2008/04/18/desperately-seeking-serial/index.html
:url: 2008/04/18/desperately-seeking-serial/
:private: true

One of the projects I've been fiddling with recently has been `Mobile Processing <http://mobile.processing.org/>`__. You might remember me `screwing around </2006/12/11/progressing-with-processing/>`__ with its parent project, `Processing <http://www.processing.org>`__, in 2006. That project's cross-platform IDE and open ethos has spread to a number of other projects, including `Arduino <http://www.arduino.cc>`__, `Wiring <http://www.wiring.org.co/>`__, `Fritzing <http://www.fritzing.org/>`__ and `Mobile Processing <http://mobile.processing.org>`__. Of these, Mobile Processing is probably the most like Processing proper, in that it attempts to provide an easy-to-use environment for writing small applications that can display graphics, respond to input and manipulate system devices. The only difference is that Processing Mobile is designed to work on J2ME-capable mobile phones.

In Washington, DC, the cheapest compatible phone that I'm aware of is Boost Mobile's i425, a crappy candybar handset from Motorola's iDEN line. It costs $40, which includes activation and $5 worth of Boost credit. Better still, for thirty-some cents a day you get unlimited data access. It's a GSM phone — speed won't be great — but still: unlimited data! **And** it has GPS! Surely that's enough to excuse its bulk and awful, awful screen.

All that you have to do to get it working with Processing Mobile `sign up for a free developer account with Motorola <http://developer.motorola.com/>`__, download their IDENJAL tool (Windows only, unfortunately), and then use it to load a Processing Mobile sketch's compiled Midlet onto the phone over USB.

With much greatly-appreciated assistance from the man himself, I've been trying to follow in the footsteps of `five.b.oh <http://five.b.oh.googlepages.com/>`__, who successfully got a similar phone to speak to his Arduino over a serial connection. If I can succeed in replicating that effort, I think this will be the most economical means of getting the Arduino online from anywhere.

Unfortunately, five.b.oh's phone is a different model from mine. His is a little older, and still uses a straightforward serial cable — one that, with some voltage-shifting circuitry, is pretty easy to connect to an Arduino. The i425 is too clever for its own good, and hides its serial port behind a USB connection. I'm confident that there \*is\* a serial port, since its baud rate can be set through the phone's menu system (five.b.oh also supplied me with a sketch that enumerates system ports, which prompted the i425 to spit out "COM0" — that's a good sign). But how can I get to that serial signal? Unfortunately USB-to-serial cables won't work in this case, I believe, since they rely upon a USB host controller being on one end. Both the phone and the Arduino will be acting as USB clients.

So I disassembled the phone, hoping to find a silkscreened label pointing me to the serial signal somewhere upstream from the USB chip. That was wishful thinking. So I'm posting the photos here, and crossposting to some relevant forums in the hopes that someone with more electronics experience will be inspired to offer a suggestion. How do I proceed? Are there things I should be looking for? Something in these photographs that looks particularly promising? Do I need an oscilloscope, or can I just probe with the Arduino's serial RX pin (under the assumption that I can trust the baud rate set on the phone)? What's the best way to get those metal covers off of the PCB?

Any advice is much appreciated. These pictures are taken in order of disassembly: imagine the phone on a table facing you, with the keypad closest to you. The phone has a top screen section, and two layers of PCBs under the keypad. These fold up like the advancing pages of a calendar.

Click the images to get to their Flickr pages, which contain higher resolution versions and notes on various components that I'm able to identify.

|motorola i425 disassembly|

|image1|

|image2|

If you're disassembling the phone yourself you'll need to remove a set of hex screws from the back (with back cover removed), then remove the front cover. At that point the keypad PCB can be carefully pulled up from the bottom of the handset — don't panic at the resistance, as there's a glob of adhesive goo there. There are a few more screws to contend with, and then the bottom PCB will lift up as well.

If this fails I plan to experiment with one-way communication to an Arduino by flashing the screen to encode data that can be detected by a phototransistor connected to the Arduino. But I'd rather have a clean serial connection.

.. |motorola i425 disassembly| image:: http://farm3.static.flickr.com/2315/2419558186_81043c131c.jpg
   :class: center
   :width: 375px
   :height: 500px
   :target: http://www.flickr.com/photos/sbma44/2419558186/
.. |image1| image:: http://farm3.static.flickr.com/2287/2419557514_9802768353.jpg
   :class: center
   :width: 375px
   :height: 500px
   :target: http://www.flickr.com/photos/sbma44/2419557514/
.. |image2| image:: http://farm4.static.flickr.com/3107/2419556742_29442cc3ec.jpg
   :class: center
   :width: 375px
   :height: 500px
   :target: http://www.flickr.com/photos/sbma44/2419556742/
