LEDs for halloween
##################
:date: 2014-11-30 18:51
:author: admin
:category: Uncategorized
:slug: leds-for-halloween
:status: published
:save_as: 2014/11/30/leds-for-halloween/index.html
:url: 2014/11/30/leds-for-halloween/
:private: true

I've continued to drift away from my commitment to dressing as villains. In my defense, Cyclops is kind of a jerk.

|image1|

I worry that I'm beginning to stagnate: my palette of duct tape, under armour and LEDs is flexible enough for a variety of comic book characters. If augmented with adhesive velcro strips and the choice of a pouch-laden Rob Liefeld character, it's even sort of convenient.

The LED components are always a hit, and I've seen more costumes incorporating them in recent years. I've added light to my costumes with a variety of different systems in the past, but they always had shortcomings. This is the first year that I achieved a well-engineered yet simple implementation, so it seems worth writing up how best to do it.

LED strips
~~~~~~~~~~

China now produces these in great volumes, and they're both cheap and easy to work with. Tons of different colors and configurations are available from `eBay <http://www.ebay.com/itm/1-20M-RGB-5050-SMD-waterproof-300-LED-Light-Strip-Flexible-IR-Remote-12V-power-/161255347539?pt=US_String_Lights_Fairy_Lights&var=&hash=item258b915553>`__ and `Amazon <http://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=led+strip>`__, invariably arriving on black plastic spools and with peel-off adhesive backing. Besides color, you'll have to decide on brightness, which varies both LEDs per meter and LED type, and waterproofing. For a halloween costume, pretty much anything will be fine -- which is to say blindingly bright.

The strips can only be cut in certain spots, but these are clearly marked. Solder tabs are present if you want to connect strips together. You're going to need a soldering iron to connect the strip to power, but it's about the simplest soldering job imaginable.

Power
~~~~~

The strips aren't just LEDs: they also have integrated resistors that are rated for 12 volts, presumably because this is the voltage at which automotive systems run. That's what you'll need to supply to the strip. You have a few options:

- Batteries' voltage is summed when wired in series. Alkaline batteries like AA cells, AAA cells and D cells are all 1.5 volts per cell, meaning that 8 placed in series will give your LEDs the power they need. You can find appropriate battery cases at Radioshack or eBay (you might need to chain two four-battery cases together). This is arguably the easiest of the approaches listed here, but also the shortest-lived and the one most likely to cause problems if asked to power too many LEDs (particularly with AAA cells, which I don't recommend).
- Lead-acid batteries are rechargeable, can hold a ton of power, and come in 12 volt or 6 volt varieties. Avoid the latter, buy a cheap trickle charger, and connect directly to your LEDs. The downside, as the name suggests, is weight (and price -- a small battery will probably run $30). Any lead-acid battery is likely to be 10 or 15 pounds. For the right costume, this is no problem. For others, it's a huge pain in the ass. If it suits your needs, though, a lead-acid battery can be a handy thing to have around: keep one charged and one of these doohickeys on hand and you'll be able to power your cell phone for a solid week when civilization finally collapses.
- Lithium-polymer USB batteries are rechargeable, pack a lot of juice, are compact and lightweight, and `can now be had for less than ten bucks <http://www.ebay.com/itm/Power-Bank-Battery-Charger-Universal-USB-Backup-Portable-External-Pack-2600mAh-/171503255918?pt=US_Cell_Phone_PDA_Chargers&var=&hash=item27ee64016e>`__. They're ideal for costumes, and they often wind up being useful cellphone supplements after the holiday. Their downside is complexity. USB power is always 5 volts. That's not enough for a 12 volt LED strip. Chaining these batteries together isn't a great idea, either. There are already electronics in play in those enclosures; and anyway 12 isn't divisible by 5. We need a way to turn 5 volts into 12.

Boost converters do this pretty efficiently, and `cost just a few dollars on eBay <http://www.ebay.com/itm/DC-DC-Adjustable-Step-up-boost-Power-Converter-Module-XL6009-Replace-LM2577-/310717070508?pt=LH_DefaultDomain_0&hash=item48582e3cac>`__. You'll need a few more things to use them, though: wirecutters, a USB cable you don't mind ruining, and a multimeter. This last tool might sound intimidating, but `a crappy $10 multimeter <http://www.amazon.com/DT830B-Digital-Voltmeter-Ammeter-Multimeter/dp/B005KGCI0Y/ref=sr_1_5?ie=UTF8&qid=1417390547&sr=8-5&keywords=multimeter>`__ will work just fine.

At this point your mission is to cut the USB cord in half and expose conductive portions of its four wires. Plug the USB connector into the battery and use the multimeter's probes to test the wires until you find a pair that gives you a reading close to 5 volts (it might not be exact, but it should be within a tenth of a volt or two). If your USB cable was designed by good people, these wires will be red and black, like the probes of your multimeter almost certainly are. But maybe they won't be. I'll assume they are.

Disconnect the USB plug from the battery. Then solder the USB wires onto the boost converter. Red is positive; black is ground. They go to the IN(+) and IN(-) solder terminals of your boost converter, respectively.

Now reconnect the cable to the battery and use the multimeter to probe the output terminals of the boost converter. There'll be tiiiiny screw on top of a plastic box on the boost converter. Turn it while reading the measurement from the multimeter until it reads twelve. It can be tough to do all of this with only two hands, so finding someone to help is recommended.

Once your boost converter is set to twelve volts, you can solder your LED strip's connection to the output terminals. Simple.

You can avoid the multimeter hassle by buying `one of these units <http://www.ebay.com/itm/DC-4-35V-LM2577-Adjustable-Boost-Step-up-Converter-Red-LED-Voltmeter-12V-24V-/351216675095?pt=LH_DefaultDomain_0&hash=item51c6252917>`__ and using its integrated display to set the voltage.

|image2|

This is both more expensive and a waste of energy (the display will remain on while powering your costume). It's also not something I've personally tried -- I've only used these to step down voltage from 12 to 5, not to step it up. I think it should work, but I can't make any guarantees.Either way you'll need to chop up a USB cable. And a basic multimeter is a handy thing to have around.

How Much Power?
~~~~~~~~~~~~~~~

It's a drag, but if you're powering more than a dozen LEDs, you should do at least a *little* math to ensure longevity and safety. Batteries can get dangerously hot when they're drained quickly. Besides, you wouldn't want to run out of power before the end of the party, would you?

We're concerned with amperage -- milliamperage, to be more precise. A liberal estimate of an individual LED's power consumption is 30 milliamps. This level of current draw, held for an hour, equals 30 milliamp-hours (mAH). Conveniently, this is also the unit that battery capacity is measured in.

If your battery assembly's output is 12 volts, the math is really easy: just divide the mAH rating of a your alkaline battery type by the number of LEDs in use multiplied by 30. A typical AA battery might hold 1200 mAH (check the label). Given that rating, a 12-volt assembly of them (8 in series) could power 40 LEDs for an hour.

If you're using a single lead-acid battery, it's just the same, except your battery's capacity might be measured in *amp*-hours. One amp-hour equals 1000 milliamp-hours. That means a 6 amp-hour lead-acid battery could power 200 LEDs for an hour.

With varying voltages, like we'll encounter with a USB lithium battery, things get slightly trickier, but only slightly. We need to figure things out in terms of energy, not just current -- that means watts, which are amps times voltage. Here's how it works out:

   | (5 volts \* USB battery milliamp hours) / (12 volts \* number of LEDs \* 30 milliamp-hours)
   | =
   | number of LEDs

The boost converter we use with the USB battery isn't perfectly efficient, so we should include a fudge factor. Let's be conservative and say it's only 90% efficient:

   | (0.9 \* 5 volts \* USB battery milliamp hours) / (12 volts \* number of LEDs \* 30 milliamp-hours)
   | =
   | number of LEDs

A small USB lithium battery might hold 2400 mAH (the packaging will usually say). Using the above math, that means such a battery could power 30 LEDs for an hour.

Of course, you probably want to power your costume for more than an hour. In fact, you should make sure of it: asking a battery to dump all of its power in an hour is fairly aggressive, and might make it heat up more than is comfortable or wise. Use the above to figure out the capacity you need per hour, then double it. Remember, you can always swap out batteries. Or, for the alkaline and lead-acid otions, you can increase capacity by adding more cells in parallel (don't do this with the USB lithium option -- just plug a new one in, or power different sections of LEDs from different batteries).

The above estimates are conservative. Boost converters are generally more than 90% efficient, and the types of LEDs I'm suggesting you use generally draw 15 or 20 milliamps, not 30. But it's good to employ a generous fudge factor. I've always been pleasantly surprised by how long my batteries hold out. You'll probably want to give your rig a test run before the party, anyway.

Fading
~~~~~~

The first time I tried to dim the LEDs in a Halloween costume it didn't work very well. I had attached a potentiometer: a knob that can add resistance to a circuit when you turn it. Increasing the resistance lowers the voltage that gets to the LEDs. A lower voltage does dim LEDs, but the behavior isn't very smooth. At first the change is almost imperceptible, then it's very sudden, and then the LEDs just turn off completely. This is because LEDs emit photons in response to voltage in a nonlinear way; even worse, humans perceive brightness in response to number of photons in a nonlinear way.

The solution is not to alter the brightness of the LED, but to change its duty cycle: how much of the time it's turned on. If an LED is only turned on every third microsecond, it will appear 33% as bright as if it were on steadily. LEDs turn on and off very quickly, so it's easy to make them strobe so fast that the human eye can't notice the flicker.

The way to do this is beyond an introductory blog post, but the short answer is: a `MOSFET <http://www.ebay.com/itm/5PCS-New-IRF740-Power-MOSFET-N-Channel-10A-400V-/321524795852?pt=LH_DefaultDomain_2&hash=item4adc5f09cc>`__, an `Arduino <http://www.ebay.com/itm/New-ATMEAG328-5V-16Mhz-Replace-ATmega168-For-Arduino-Pro-Mini-Compatible-Nano-/191117208428?pt=LH_DefaultDomain_0&hash=item2c7f792b6c>`__, and the `analogWrite() <http://arduino.cc/en/Reference/analogWrite>`__ function. The first two can be had for less than $5 combined, and the last is free. If you decide to try this but have no idea what you're doing, get in touch with me and I'll try to help.

A nice side-effect: by adding an Arduino you can easily start programming strobing or fading effects. You could even make your costume respond to the partygoers around you.

EL Wire
~~~~~~~

LEDs aren't your only options for lighting a costume. Electroluminescent `wire <http://www.ebay.com/itm/US-5M-16ft-Flexible-EL-Wire-Neon-LED-Light-Rope-Party-Car-Decorati-BATTERY-PACK-/271509438262?pt=US_String_Lights_Fairy_Lights&var=&hash=item3f37393f36>`__, `strips <http://www.ebay.com/itm/1-4m-electroluminescent-strip-with-lead-wire-connector-48-EL-tape-light-lamp-/121268322259?pt=LH_DefaultDomain_0&var=&hash=item1c3c27bfd3>`__ and `panels <https://www.sparkfun.com/products/10799>`__ are fairly cheap and generally come with their electrical systems prebuilt, thanks to their unusual power requirements (very high voltage and frequency alternating current at very low amperages). Those power supplies generally run off of just one or two alkaline batteries and can last for many hours.

The downside to EL systems is how difficult they are to manipulate. EL wire and panels can be cut, but they can't be spliced without unusual tools and more skill than I can muster. The power supplies also tend to be made cheaply, and when they are they emit a quiet but high-pitched whine which might be annoying in environments that are supposed to be silent and spooky, like a haunted house.

.. |image1| image:: /static/2014/11/IMG_0185-300x300.jpg
   :class: aligncenter wp-image-2855 size-medium
   :width: 300px
   :height: 300px
   :target: /static/2014/11/IMG_0185.jpg
.. |image2| image:: /static/2014/11/Screen-Shot-2014-11-30-at-6.38.23-PM-300x250.png
   :class: aligncenter size-medium wp-image-2853
   :width: 300px
   :height: 250px
   :target: /static/2014/11/Screen-Shot-2014-11-30-at-6.38.23-PM.png
