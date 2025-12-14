cooling PCs with salad dressing and magic
#########################################
:date: 2008-07-11 14:35
:author: admin
:category: tech
:slug: cooling-pcs-with-salad-dressing-and-magic
:status: published
:save_as: 2008/07/11/cooling-pcs-with-salad-dressing-and-magic/index.html
:url: 2008/07/11/cooling-pcs-with-salad-dressing-and-magic/

`Kriston <http://grammarpolice.net>`__ sent me `this link <http://www.economist.com/displayStory.cfm?source=hptextfeature&story_id=11699909>`__ earlier this week, which discusses using water to cool our ever-hotter computer processors. It's an interesting read, particularly the part about using waste heat from datacenters for cogenerative heating.

But the ins and outs of the CPU heat problem are actually even moreinteresting than the article implies. So interesting, in fact, that I think I'll blather on about them for a bit.

First: this isn't a new problem. As we cram more transistors onto chips every electrical component gets smaller and noisier, and we have to crank the voltage up to be able to hear the signal. That produces more heat. As we increase processor clock speeds the heat-generating operation of all those tiny switches happens more frequently, too, which also produces more heat.

This is a pretty well-known problem in hobbyist circles, where overclocking — running your CPU at a faster speed than it's designed for — is a popular way to eke out more bang per buck. Doing so also produces a lot of extra heat, which these days translates into the CPU shutting itself down rather dramatically once it reaches the danger zone (earlier chips dealt with overheating in considerably more expensive ways).

In overclocking circles exotic cooling solutions are pretty common, whether in the form of beefed up fans, Peltier coolers or water. A normal CPU cools itself with a fan that uses air to wick heat away from a radiator-like block of aluminum, which is strapped tightly to the CPU with just a tiny smear of thermally conductive grease between 'em. But air is much less efficient at transmitting heat than the same volume of liquid, so if you're pushing the envelope it may make sense to shuttle energy around with liquid.

This isn't a particularly exotic technology any more — Dell was `shipping water-cooled gaming systems over a year ago <http://www.hothardware.com/articles/Dell_XPS_710_H2C_Performance_Gaming_System/>`__. But it's still unlikely to enter the mainstream. As you might imagine, the potential for disastrous failure is much higher than with a fan. And there are other inconveniences — if you don't use the right chemicals you might find your PC clogged with algae.

An amusing alternative exists: use a nonconductive fluid and simply submerge the whole system. Like, say, `cooking oil <http://www.tomshardware.com/reviews/strip-fans,1203.html>`__. Dump your PC's guts in a tub, cover with oil and overclock away! As you might imagine, there are some downsides. First, atmospheric water may foul the oil and perhaps even collect in small patches sufficient to cause a short. Second, anything with moving parts — hard drives, for example — will need to be kept safely unsubmerged. Third, various compounds in your machine's electronics, like cable insulation, may slowly dissolve in a nonpolar solvent like oil. Fourth, you'll still need to circulate the oil if you want it to properly exchange heat. Fifth, and most importantly: it's going to be really messy and gross. Seriously, don't pour oil on your PC.

But there are other technologies being used to mitigate heat problems. One of them — admittedly, kind of a boring one — is the general trend toward multiprocessor computing. This is being undertaken primarily for other reasons, but a pleasant consequence of greater parallelism will be an ability to avoid some heat problems.

A somewhat more speculative (but still plausible) idea is to escape silicon and its heat limits by finding another semiconductor substrate material. Diamond is the one most often bandied about, as `in this Wired article <http://www.wired.com/wired/archive/11.09/diamond_pr.html>`__. It's a pretty neat idea, although so far as I know nobody's yet trying to build such a processor outside of a research lab.

The coolest, most semi-magical solution to the heat problem is `reversible computing <http://www.theregister.co.uk/2003/11/14/reversible_computing_is_the_only/>`__. I can't claim to be an expert, but the basic idea goes like this: if you keep track of every step of a computational process in such a way that, after arriving at your answer, you can run them all *backward*, the final result will be a much less entropically disordered state than a traditional processor would have arrived at. A result is that much less of your input energy is converted into heat.

I know: it sounds kind of ridiculous, as though we're expecting our mathematical doodlings to bend reality in a completely implausible way. There must be some obscured practical gotcha hiding beneath the theory, ready to spoil our cool-computing aims in the same way that every magnet-based free energy machine fails to live up to its imagined performance. But the idea's been around for decades, and not in fringe circles. It's just that it's a sufficiently advanced technology, indistinguishable from... well, you know.
