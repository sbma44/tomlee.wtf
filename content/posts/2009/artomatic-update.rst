Artomatic update
################
:date: 2009-04-28 14:29
:author: admin
:category: tech
:slug: artomatic-update
:status: published
:save_as: 2009/04/28/artomatic-update/index.html
:url: 2009/04/28/artomatic-update/
:private: true

I stayed up way too late last night working on my piece for Artomatic. Playing with electronics can frequently be frustrating — everything goes wrong, then keeps going wrong, and at the end of the night you're left with nothing besides a pile of wasted components and a vague worry about how much lead you've just ingested. Other times, though, everything seems to go right, and that's how it went last night. There's still much more work to be done, but I'm making definite progress.

The piece in question involves a set of `reception bells <http://images.google.com/images?q=reception%20bell&hl=en&btnG=Search+Images>`__ that can be rung through electronic means, and the manual ringing of which can be similarly detected. The first part is done, in a proof-of-conceptish way — I have 12V solenoids installed that can push the clapper into the bell with satisfying vigor — but isn't completely wired up yet, largely because if you run a solenoid incorrectly it'll, er, melt.

The other major task is the detection of a manual ring. I initially thought I'd manage this by electrically isolating the clapper from the dome of the bell, then checking for a completed circuit between them. Ah, the naivete of youth. It turns out that this is a lousy way to make a circuit; worse, it's hard to solder wires onto an anodized bell; worse still, it's *really* hard to solder to a bell without changing its tone to something unpleasant.

Instead I decided to detect when the clapper breaks an infrared beam. `These things <http://www.sparkfun.com/commerce/product_info.php?products_id=241>`__ seemed promising due to their physically decoupled nature, but there's no filter to prevent visible light from affecting the photodiode. This might've worked fine inside the darkness of the bell, but it made prototyping a pain.

`These <http://www.sparkfun.com/commerce/product_info.php?products_id=247>`__ work much better, although the gap between the emitter and detector is juuuust too small to work with the bell's clappers. Bravely ignoring the package's admonishments to avoid breaking open devices made of gallium arsenide, I sawed 'em in half and mounted them with hot glue, and they've been working great ever since.

(Incidentally, I don't think I poisoned myself — the GaAs is only used for the actual semiconducting materials, not the mounting armature, and the package allowed me to see that I would only be cutting plastic if I separated the two halves.)

Here are the fruits of my labor: a creepy video of yours truly showing off an LED blinking in time to the dings of the bell. I still have a minor issue to resolve related to one clapper's tendency to bounce (mechanically, not electrically), but I think I can account for that behavior in software.

.. container:: center

   .. raw:: html

      <embed src="http://blip.tv/play/Af3OIgA" type="application/x-shockwave-flash" width="500" height="400" allowscriptaccess="always" allowfullscreen="true">

   .. raw:: html

      </embed>

Next I'll be prototyping the full bell-strike-detection solution; doing the same for the solenoid; soldering those working circuits onto the breakout/power board; adding active cooling to the case; getting two way serial communication working between the Fonera and Arduino; writing the final software; and then doing the boring, non-electronic stuff: staining, sanding, installation. I've got about a month to get it all done, and right now I'm feeling pretty good about it. But there are certainly still a lot of loose ends.

Speaking of which! Anybody got a pair of bar stools or similarly-sized tables that I can borrow for the month of June?
