texameter
#########
:date: 2013-03-10 15:04
:author: admin
:category: Uncategorized
:slug: texameter
:status: published
:save_as: 2013/03/10/texameter/index.html
:url: 2013/03/10/texameter/
:private: true

I picked up this handsome fellow in Texas:

|Untitled|

I found him at `Uncommon Objects <http://www.uncommonobjects.com/>`__, a really lovely and fun antique-y shop on Congress. They had `a bunch of beautiful old radio stuff <http://instagram.com/p/V4ovyNvEMe/>`__, but this was the only thing I walked away with. It's a strange little piece -- just a sheet metal enclosure for a voltmeter, probably from a test bench of some sort. Those two ports on the front were originally for connecting to the voltage being measures (though the internal wires connecting them to the meter had been snipped by the time I got to it).

It took a `little work <http://www.flickr.com/photos/sbma44/8538628589/in/photostream/>`__, but I've given this guy a brain:

|image1|

 

That's a wifi-enabled Raspberry Pi which can drive the VU meter. I also added a red and an amber LED (also controllable via the Pi).  I haven't figured out what I want to measure just yet, but I'm sure something will come to me.

I've been trying to get a VU meter-driven project together for a while now, but between the software, hardware and enclosure, I was feeling a little overwhelmed. Having the enclosure taken care of made this a pleasant stepping stone.  Details/thoughts/tips:

**Networking**

- Linux wifi is a huge pain in the ass. Finding a card with a compatible chipset is your first major task. Lady Ada has helpfully identified a pretty cheap one and sells it `here <https://www.adafruit.com/products/814>`__. I bought a slightly cheaper Monoprice card with my BeagleBone in mind, and it works fine with the Pi's default Raspbian distro -- no messing with firmware downloads or 'nothin.
- Wifi cards suck up a lot of juice, and the Pi can't supply very much over its USB ports. You might need a powered hub. The revision 2 Pi can power this adapter okay, but only if you boot with it in -- plug it into a running system and the current draw will force a system reset.
- I hate messing with wpa_supplicant. The wicd package and its wicd-curses interface are your friends. But do *not* try to use them over SSH. The system flushes its routing when it sets up a new connection, and your SSH connection will get killed halfway through any connection to a wifi network, even if your SSH session started over ethernet. And then weird stuff will happen, like the wifi taking over the ethernet IP. It took me forever to figure out what was going on -- I thought maybe the current draw of connecting to a network was bringing the system down. The moral turns out to be: use a keyboard and monitor until you've got a system that reliably boots and connects to the wireless network.
- I've got `a simple Raspbian bootstrap script <https://github.com/sbma44/rpi/blob/master/bootstrap.sh>`__ that updates things and sets up a Python environment. You might find it useful -- though you'll probably want to remove the part that gives my public key access to your system :-/

**Hardware**

- The meter was designed to measure a voltage range of 0-15V; delightfully, it still did this pretty well, despite being an antique! But the Raspberry Pi's PWM only outputs a max of 3.3V. I had already bought a `cheapo buck converter off of ebay <http://www.ebay.com/itm/Boost-Buck-Voltage-Module-3-35V-to-2-2-30V-Step-Up-Down-Converter-Regulator-/290833291375?pt=LH_DefaultDomain_0&hash=item43b703d86f>`__ before Timball reminded me that VU meters are basically just galvos, and use resistors to set their range. Here's what the inside looks like:

  |Staring down some resistor network math to convert a 15v VU meter to 5v. Boo.|

  The resistor's in the upper left. I dug out `my old standby <http://www.amazon.com/Practical-Electronics-Inventors-2-E/dp/0071452818>`__, reminded myself `what a resistor network is <http://mathworld.wolfram.com/ResistorNetwork.html>`__, and added a trim potentiometer in parallel with the existing resistor (it's the blue square on the far right of the second picture in this post). Through some careful tuning with a screwdriver I was able to make the arm sweep all the way to the 15 with just the weensy 3.3V of the maxed-out Pi. Hurrah!

- I also added a couple of status-indicator LEDs to the bottom of the meter. Their placement isn't ideal, but you can see *something* when they're on, at least. The meter wasn't designed to accommodate them, so I had limited options.

- The LED holes and the entry point for the system's power cable both required some Dremeling. Having sparks of hot metal showering your arm can be counted on to prompt some justified self-congratulation about wearing eye protection. Yeesh.

**Software**

- The `wiringpi <https://projects.drogon.net/raspberry-pi/wiringpi/>`__ library and its `Python bindings <https://github.com/WiringPi/WiringPi-Python>`__ are designed to be pleasantly Arduino-like. Setup is  as easy as \`sudo apt-get install -y python-dev && pip install wiringpi\`. By default, you have to run your GPIO/PWM-manipulating scripts as root -- there's an alternate method available, but I couldn't get the /sys/ GPIO interfaces to work properly in userland (though I didn't try very hard). Ah well.
- Pay attention to the variability in pin names. wiringpi uses the pin numbers of the underlying microcontroller, not the numbers from the Pi connector. `This table will help you translate between the two <https://projects.drogon.net/raspberry-pi/wiringpi/pins/>`__. Unless you're doing `something crazy <http://blog.makezine.com/2013/02/12/pi-blaster-improves-software-pwm-on-raspberry-pi/>`__, the Pi's sole PWM comes out of GPIO1, which is "pin 1" to wiringpi and pin 18 on the Raspberry Pi connector.
- The software I wrote to run this thing is nothing special, though there is one convenience library you might enjoy: `pwmcalibrate.py <https://github.com/sbma44/texameter>`__. Using a curses interface, it slowly steps down the PWM output from max to zero, recording the active PWM setting as you hit spacebar, which you should do as the needle crosses each step on the meter. This data is used to create a calibration file that can be easily reloaded, allowing you to set the meter by the desired display value without having to think about it much. It also does some simple linear interpolation if you ask for a value that's between recorded calibration steps. I'm pretty pleased with how it performs, though the meter itself seems to display some performance variability at the low end of its range. Probably nothing to be done about this, given the age of the hardware. Oh, and it will slowly step down the PWM when making transitions, if you ask it to. This is worth doing if you don't want the needle to bounce around a ton.

I think that's it. Now I just need to hook it up to something worth measuring. Or Twitter, I guess.

.. |Untitled| image:: http://farm9.staticflickr.com/8512/8546140222_0250cb0b70.jpg
   :class: aligncenter
   :width: 375px
   :height: 500px
   :target: http://www.flickr.com/photos/sbma44/8546140222/
.. |image1| image:: http://farm9.staticflickr.com/8366/8545043397_a0b776138c.jpg
   :class: aligncenter
   :width: 375px
   :height: 500px
   :target: http://www.flickr.com/photos/sbma44/8545043397/
.. |Staring down some resistor network math to convert a 15v VU meter to 5v. Boo.| image:: http://farm9.staticflickr.com/8233/8532279025_da5402b70e_n.jpg
   :class: aligncenter
   :width: 320px
   :height: 320px
   :target: http://www.flickr.com/photos/sbma44/8532279025/
