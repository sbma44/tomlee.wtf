my LED monstrosity
##################
:date: 2008-05-07 11:12
:author: admin
:category: tech
:slug: my-led-monstrosity
:status: published
:save_as: 2008/05/07/my-led-monstrosity/index.html
:url: 2008/05/07/my-led-monstrosity/
:private: true

So! Let's talk about what I've been working on. I wasn't very good about documenting my WMATA picture frame build. This time I'm aspiring to do a better job.

At the moment I'm working on getting a 10x20 array of LEDs working. I haven't completely made up my mind about what I'm going to use it to display, but it'll be something that can be hung on the wall, I think. At the moment there are two parts to the project.

First is the array of LEDs. I'm using a sheet of pegboard for spacing; last night I began soldering them together. As you can see, I still have a lot of work ahead of me. I installed 70 LEDs last night over the course of two or three hours (admittedly, with breaks for dinner and the expression of my very important opinions regarding American Idol). That's 35% of the total number.

|miles to go...|

Each hole in the board has an LED, to which a resistor is attached. The anodes of every LED in a row are electrically unified; the cathodes in every column will be, too. This lets me avoid having to use 200 individual on/off connections. Instead I'll rely on persistence of vision: each row will be powered up in sequence, and during that period each column will be switched on or off. One row — ten LEDs — will be illuminated at any given instant. By flipping through rows very quickly the display will appear to be continuously on. Our retinas are stupid that way.

|closeup of the assembly|

The advantage gained by this is that I only need 30 connections instead of 200. That's an improvement — much less soldering! — but still more connections than the Arduino has to offer.

So, to expand the available connections (which I should really be calling pins, and will be from here on out) I'll be using four daisy-chained five-bit shift registers. These are integrated circuits that require various connections — power, ground, and some others supporting optional functions that I'm not using — but the real action happens on the chips' input and clock pins. You set the input pin to a desired value; you then flip the clock pin on and off. The chip then remembers the value that was on the input pin, and begins displaying it on its first output pin. If you do the same thing, the originally-remembered value is moved to the second output pin, and the new input value takes the first position. In this way you can shift bits down the line — and by connecting one chip's final output to another's input, you can make the line arbitrarily long. Voila: as many output pins as you need, all at the cost of a mere two Arduino output pins.

The video below is a proof-of-concept for this commonly-used idea — it's just my effort to make sure I know what I'm doing before I start making irreversible soldered connections. The Boarduino (the thing with the blinking red light) is connected to the first shift register (the chip closest to the Boarduino), and set to send four ON signals, then four OFF signals (distinguishing the divisions between each one by flipping the clock signal, which is indicated by the flashing red LED).

In the actual device each shift register output will provide power to an entire row's anodes — there will only be one ON bit at a time, and it will travel down the twenty outputs in sequence. This is why there are transistors in the setup, too: the shift register could provide enough current for a single LED, but ten would be pushing it. The transistor allows a very small current from the shift register to switch on a much larger current.

Electronically astute readers might be asking themselves why I'm going to the trouble of attaching 200 resistors (and for my electronically non-astute readers: the resistors are necessary to keep the LEDs from consuming too much current and burning out). After all, if only ten LEDs will actually be on at a time, why not just have ten resistors — one for each column?

There are a couple of reasons, most of them related to a lack of confidence in my ability to keep just one row enabled, particularly during the debugging process. First, in general it's a bad idea to have LEDs sharing resistors. If one LED fails the other one may suddenly experience twice the current you had intended, and will also fail immediately. Second, the resistors are rated for a half-watt of power dissipation. Each LED consumes about 30 milliwatts; if an entire column is illuminated, that'd put me 20% over spec for the resistors. I probably could've gotten away with shared resistors in this case, but I'm still sufficiently unsure of what I'm doing that I didn't want to risk it. Besides, all that additional soldering will build character.

.. |miles to go...| image:: http://farm4.static.flickr.com/3276/2473114747_7ed146e1bb.jpg
   :class: center
   :width: 375px
   :height: 500px
   :target: http://www.flickr.com/photos/sbma44/2473114747/
.. |closeup of the assembly| image:: http://farm3.static.flickr.com/2208/2473934182_d09f376304.jpg
   :class: center
   :width: 500px
   :height: 375px
   :target: http://www.flickr.com/photos/sbma44/2473934182/
