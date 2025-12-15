DIY abominations
################
:date: 2013-10-27 23:09
:author: admin
:category: Uncategorized
:slug: diy-abominations
:status: published
:save_as: 2013/10/27/diy-abominations/index.html
:url: 2013/10/27/diy-abominations/
:private: true

I like to make a new Halloween decoration every year. One year it was `corpsing a skeleton <http://www.hectorturner.com/halloween/corpse.html>`__; another year I built a coffin; another time I made some big glowing papier mache spiders.

This year I decided I wanted some skulls. Goat skulls, ideally -- dollar for dollar, I don't think there's a creepier skull out there. Probably it's all the `Doom 2 <http://doom.wikia.com/wiki/Final_boss>`__ I played as a kid.

I posted an ad on Craigslist appealing to hunters and farmers for help with (ahem) a "theatrical production." Eight days later I received a response. "Kyle" worked at Crazy K Goat Ranch, and he seemed to have a lot of skulls; we made plans to meet a few days later. I brought along Dave and Kriston to ensure that the encounter's net flow of skulls went in the direction I expected.

It only took a moment to verify that Kyle was probably the K in "Crazy K". He was certainly a strange guy. He seemed to live with his parents, and I'm not at all sure that the goat farming is a full-time occupation for him. But he was very nice to us, particularly since I happened to be wearing a Capitals t-shirt -- Kyle was, too, and turned out to be a bit of an Alex Ovechkin super-fan.

`$20 per skull is a steal <http://www.skullsunlimited.com/>`__, and we concluded our business quickly. Kyle sold me the skulls of a bunch of goats, an alpaca, a llama, and a pig that had (until recently) been giving him trouble. There is apparently some kind of solution he soaks them in to remove the soft tissue -- it's intensely unpleasant, I'm sure.

Anyway: I had some skulls.

|skulls|

|me_and_skulls|

A good start! But I wanted to do a little more. And hey: `I've achieved pretty good results with creepy glowing eye sockets before <http://www.flickr.com/photos/sbma44/8130970953/in/set-72157631911659225>`__. Let's do some more of that.

The basics are pretty simple. The idea of an `LED throwie <http://www.instructables.com/id/LED-Throwies/>`__ is at least seven years old now (can that be right?) but it works as well as ever. Let's pause for a brief interlude about sticking them all over the cube at Astor Place:

Nice.

Well, the gist is the same as always: the LED and the CR2032 battery are a lovely match. The CR2032's 3 volts are enough to light up most LEDs. Better still, its internal resistance will prevent the LED from burning out immediately, even when used without a resistor. You can wedge a CR2032 between an LED's leads and it will light up quite happily for hours! And hey, `it turns out that these batteries aren't even that terrible for the environment <http://cr2032.co/environment-article.html>`__.

You can get all of these components very cheaply on eBay. `Here are fifty red LEDs for $3 <http://www.ebay.com/itm/50-x-LED-3mm-Red-Water-Clear-Ultra-Bright-USA-Seller-Free-Shipping-/221288139799?pt=LH_DefaultDomain_0&hash=item3385cd0c17>`__; `here are 20 CR2032s for a little more than $4 <http://www.ebay.com/itm/20-CR2032-DL2032-ECR2032-5004LC-3-Volt-Lithium-Button-Cell-Battery-USA-US-Ship-/400433857727?pt=US_Single_Use_Batteries&hash=item5d3bb7c4bf>`__. If you want to get fancy (and I did) `you can get CR2032 holders for about fifty cents a pop <http://www.ebay.com/itm/Lot-5-Pcs-New-CR2025-CR2032-Battery-Button-Coin-Cell-Holder-Socket-Case-Black-/180907107772?pt=LH_DefaultDomain_0&hash=item2a1ee765bc>`__.

Wiring the necessary circuit is dead-simple. I have a distinct memory of getting a small light bulb to illuminate from a battery in second grade; it was the first thing they taught us about electricity. This is no more complex, except that you might need to flip the LED around if you get the polarity wrong the first time. So, no need to belabor that. Also: it turns out hot glue guns work well on bone.

But for a few of the more frightening skulls I went a little further and added a circuit that turns the lights on only when the surrounding environment is dark. It's a pretty useful technique for working with analog signals of any kind (I've also used it to trigger a light-sensor to activate a music box upon opening, for instance), so let's go ahead and run through it.

We'll need three things to make this happen. First, **some way of sensing light** -- that much is obvious. Second, **a way to define what our threshold for "dark enough" is**. Third, **a way to compare the two values and switch the LED circuit on**.

Let's start with the last one. I used an LM393 comparator, a common chip that looks like this:

|LM393|

`It, too, can be found on eBay for pennies per unit <http://www.ebay.com/sch/i.html?_trksid=p2047675.m570.l1313.TR0.TRC0.Xlm393&_nkw=lm393&_sacat=0&_from=R40>`__.

The LM393 is very simple. It takes a reference voltage. It takes a comparison voltage. If the latter goes above the former, the chip will make an electrical connection between its output pin and ground, potentially completing a circuit and doing useful work.

The LM393 also looks like this:

|comparator|

That's the schematic from `its data sheet <http://www.ti.com/lit/ds/symlink/lm393-n.pdf>`__, mapping the chip's 8 pins to their functions. Pins are numbered in counter-clockwise order, starting to the left of the chip's top side, which is marked by a little notch or off-center circle (or, in the above photo, both). As you can see, there are actually two comparators built into the LM393; we're only using one. For our purposes they're electrically distinct, except for a shared ground and supply voltage (V+ in the diagram, though it's more commonly called V\ :sub:`cc`). The LM393 can run off anything from 2 to 36 volts.

So how do we arrange the reference and comparison voltages? It's really simple, actually: we use a `voltage divider <http://en.wikipedia.org/wiki/Voltage_divider>`__. Picture it like this:

|divider|

V\ :sub:`in` is our supply voltage -- let's say 10 volts. The horizontal triangular thingy at the bottom is ground. R\ :sub:`1` and R\ :sub:`2` are resistors connected to one another. At the top, it's always gonna be 10 volts. At the bottom, it'll always be zero. That's axiomatically true. But what about *in between the resistors*, at V\ :sub:`out`?

That depends on the values of R\ :sub:`1` and R\ :sub:`2` -- or, really, the ratio between them. If they're both 100 ohms, or 2500 ohms, or 5 million ohms, V\ :sub:`out` will be 5 volts. If R\ :sub:`1` is 25 ohms and R\ :sub:`2` is 75 ohms, V\ :sub:`out` will be 7.5 volts. If you flipped them, it would be 2.5 volts. It's all pretty linear and straightforward (the `Wikipedia voltage divider article <http://en.wikipedia.org/wiki/Voltage_divider>`__ will walk you through the math, if you'd like). Make sense?

So! Let's set things up. Keep the battery out of the holder until you're done, but pretend it's in there -- now we have a 3 volt V+ and a ground. Connect 'em to the relevant pins on the LM393. Now take two resistors -- doesn't really matter what value, as long as they're the same, but they should be a decently high value to avoid voltage drain -- and connect them in series, bridging V+ and ground BUT, crucially, making a pit-stop in the middle at pin 5 ("non-inverting input B"). That pin will now be getting a reference voltage of 1.5 volts. If the voltage on pin 6 ("inverting input B") goes above this value, pin 7 will be connected to ground. If not, not.

But what gets connected to pin 6? Well, seems like we need something that changes its value based on light. Easy enough! A photoresistor is just what it sounds like and is, again, `cheap on eBay <http://www.ebay.com/sch/i.html?_trksid=p2050601.m570.l1313.TR0.TRC0.Xscrew+terminals&_nkw=photoresistor&_sacat=0&_from=R40>`__. They look like this:

|photoresistor|

That squiggle in the middle is made of a material that lowers its resistance as light hits it. Otherwise, this thing behaves just like a regular resistor. That means we can build a voltage divider with it, just like the one we connected to pin 5. What should we use for the other resistor in the voltage divider circuit, though?

We could just use a regular old resistor. But we'd have to be pretty careful about picking it, and it would lock us in to one particular level of darkness as our threshold value. That's not a great idea, particularly since human senses respond to energy changes adaptively and logarithmically, while sensors do not.

It will be much better to use a variable resistor -- a potentiometer. `Back to eBay <http://www.ebay.com/itm/100ohm-1M-Kit-Variable-Resistors-Potentiometer-65pcs-13-value-5pcs-each-Assorted-/221302553462?pt=LH_DefaultDomain_0&hash=item3386a8fb76>`__! These guys come in many different forms, but for this we can get away with a the teeny tiny ones that you adjust with a screwdriver (sometimes called `"trim pots" or "trimmers" <http://en.wikipedia.org/wiki/Trimmer_(electronics)>`__).

Picking the appropriate range for the potentiometer is important. We want something that will let us flirt with the half-of-V+ comparison voltage we already defined via the divider we built out of those first two resistors. In this case, that means getting out a multimeter and figuring out the range of your photoresistor. Test it in darkness; test it in daylight. Try to find a trim pot that can approximate this range of resistances, or at least one that can be adjusted to somewhere around the photoresistor's value in slightly-too-bright-for-goat-skull-glowing conditions.

Now make a voltage divider with these two -- it'll be the same deal as before, just connected to a different pin. The photoresistor lives on the side of the circuit closer to ground. The trim pot lives on the side closer to V+. The junction between the two goes to pin 6.

Finally, connect the ground side of the LED leads to pin 7. This is the final schematic:

|schematic|

I did all of this in "deadbug" style:

|deadbug|

Now wait until it's dark in the room and adjust the trim pot until the lights juuuust turn on. Voila!

|10526396545_5ac3a77ed6|

When it's brighter, the circuit should turn off. You'll want to fiddle with the placement of the photoresistor -- I gave mine a little wire lead and ran it out to the edge of the skull. It doesn't need to be in direct light, but obviously it does need to experience *some* change in lighting conditions, and the bigger those changes are the easier it will be to select and adjust your trim pot.

The batteries will experience some drain even when the LEDs are off, but the LM393 is designed to consume very little juice. The voltage dividers take a little bit of power, but hopefully you picked elements with adequately large resistive values. If your in-light resistor networks both amount to 10K ohms apiece, your total system will consume about 1 milliamp at rest. Not bad! At that load, a fresh CR2032 should last for about 200 hours (less if the LEDs are activated, of course).

The LM393 makes for a fun little project -- a nice way to build a night-light, or clean up an input signal to an Arduino, or just have something to mess around with on a breadboard. If you flip the two input pins, it'll become a light detector rather than a darkness detector. It's useful for almost any variable-voltage measurement of the analog world. I originally bought these components for a project designed to use a `thermistor <http://en.wikipedia.org/wiki/Thermistor>`__ to tell me when a cup of coffee was a pleasant temperature for drinking.

So, somewhat far afield from skulls. But the nice thing about this application is that there's really no precedent for anyone getting upset about mixing electricity and illicitly-obtained body parts.

.. |skulls| image:: /static/2013/10/skulls.jpg
   :class: aligncenter size-full wp-image-2635
   :width: 612px
   :height: 612px
   :target: /static/2013/10/skulls.jpg
.. |me_and_skulls| image:: /static/2013/10/me_and_skulls.jpg
   :class: aligncenter size-full wp-image-2636
   :width: 612px
   :height: 612px
   :target: /static/2013/10/me_and_skulls.jpg
.. |LM393| image:: /static/2013/10/LM393.jpg
   :class: aligncenter size-full wp-image-2640
   :width: 600px
   :height: 450px
   :target: /static/2013/10/LM393.jpg
.. |comparator| image:: /static/2013/10/comparator.png
   :class: aligncenter size-full wp-image-2637
   :width: 482px
   :height: 271px
   :target: /static/2013/10/comparator.png
.. |divider| image:: /static/2013/10/divider1.png
   :class: aligncenter size-full wp-image-2643
   :width: 178px
   :height: 168px
   :target: /static/2013/10/divider1.png
.. |photoresistor| image:: /static/2013/10/photoresistor.jpg
   :class: aligncenter size-full wp-image-2646
   :width: 720px
   :height: 571px
   :target: /static/2013/10/photoresistor.jpg
.. |schematic| image:: /static/2013/10/schematic-1024x803.jpg
   :class: aligncenter wp-image-2662
   :width: 614px
   :height: 482px
   :target: /static/2013/10/schematic.jpg
.. |deadbug| image:: /static/2013/10/deadbug.jpg
   :class: aligncenter size-full wp-image-2647
   :width: 527px
   :height: 518px
   :target: /static/2013/10/deadbug.jpg
.. |10526396545_5ac3a77ed6| image:: /static/2013/10/10526396545_5ac3a77ed6.jpg
   :class: aligncenter size-full wp-image-2648
   :width: 500px
   :height: 500px
   :target: /static/2013/10/10526396545_5ac3a77ed6.jpg
