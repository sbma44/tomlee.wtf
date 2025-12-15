numbers aren't just numbers
###########################
:date: 2007-05-03 11:26
:author: admin
:category: tech
:slug: numbers-arent-just-numbers
:status: published
:save_as: 2007/05/03/numbers-arent-just-numbers/index.html
:url: 2007/05/03/numbers-arent-just-numbers/
:private: true

Ed Felten has `an interesting post <http://www.freedom-to-tinker.com/?p=1154>`__ up this morning discussing the 09-f9 HD-DVD key and why the net has been replicating it so enthusiastically. He has a number of explanations for why people are showing such antipathy toward the AACS LA's efforts to suppress the key. I'm most interested in the second one, because it's pretty widespread and very, very silly:

   | ...the content in question is an integer — an ordinary number, in other words. The number is often written in geeky alphanumeric format, but it can be written equivalently in a more user-friendly form like 790,815,794,162,126,871,771,506,399,625. Giving a private party ownership of a number seems deeply wrong to people versed in mathematics and computer science. Letting a private group pick out many millions of numbers (like the AACS secret keys), and then simply declare ownership of them, seems even worse
   | While itâ€™s obvious why the creator of a movie or a song might deserve some special claim over the use of their creation, itâ€™s hard to see why anyone should be able to pick a number at random and unilaterally declare ownership of it. There is nothing creative about this number — indeed, it was chosen by a method designed to ensure that the resulting number was in no way special. Itâ€™s just a number they picked out of a hat. And now they own it?
   | As if thatâ€™s not weird enough, there are actually millions of other numbers (other keys used in AACS) that AACS LA claims to own, and we donâ€™t know what they are. When I wrote the thirty-digit number that appears above, I carefully avoided writing the real 09F9 number, so as to avoid the possibility of mind-bending lawsuits over integer ownership. But there is still a nonzero probability that AACS LA thinks it owns the number I wrote.
   | When the great mathematician Leopold Kronecker wrote his famous dictum, â€œGod created the integers; all else is the work of manâ€?, he meant that the basic structure of mathematics is part of the design of the universe. What God created, AACS LA now wants to take away.

Okay, so it's a little melodramatic. But you can see his point. He's not alone in this, either: BoingBoing has been `petulantly <http://www.boingboing.net/2007/05/02/oh_how_i_love_the_ge.html>`__ `maintaining <http://www.boingboing.net/2007/05/02/are_these_colors_ill.html>`__ that if we all just pretend the number is being used for other purposes, it'll be just dandy to redistribute it.

I'm no fan of DRM, and I think the AACS LA's actions are pointless and stupid. But Doctorow and Felten are being disingenuous — they're simply too smart not to see the problem with this argument. Namely, that *any* type of data, sampled at a chosen level of precision, can be represented as a number. Consequently, if you believe that one or more types of information deserve legal protection — as Felten seems to, when he refers to songs & movies — then the argument that "it's just a number!" becomes ridiculous.

Sixteen bytes is probably too short to merit a copyright. But that's not the right that the AACS LA is asserting: they're calling the code a "circumvention device" under the DMCA. And even if you don't recognize the DMCA's validity, there are other forms of intellectual property protection that may apply — there are laws related to trade secrets, for example. If you just think about it a little, it should be obvious that even a very short piece of data can enjoy some kinds of legal protection. Sixteen bytes is more that enough room to encode the words "Coca-Cola", after all.

The thing is, geeks like to pretend that the legal system is some sort of Rube Goldberg contraption, easily foiled by their unparalleled cleverness. Sadly, this isn't the case. All the IANAL-prefixed prattling on Slashdot about quick & easy ways to make yourself legally bulletproof when the cops/MPAA/interpol come knocking are little more than wishful thinking. It's like holding your finger an inch from your sibling's face and yelling, "I'm not touching you!" over and over. Your parents weren't dumb enough to fall for that, and neither is the legal system.

So yes, if you accidentally used `these colors <http://t3knomanser.livejournal.com/906184.html>`__ in a design, I doubt you'd be breaking the law. If you wrote this `terrible poem <http://scriptorium.monastic.org/>`__ by chance, you'd be fine. But if you provided either intentionally, as a way of transmitting a "circumvention device", then you broke the law. It's entirely possible for a judge to make reasonable inferences about what you probably intended to do. I don't know where people got the idea that courtrooms are run by robots that'll start spewing sparks & smoke if you feed them a logical paradox. It just ain't so.

Most of all, I'm surprised by Felten saying that making a number protected will irk "people versed in mathematics and computer science" most of all. In fact, the people who don't understand why a number could deserve protection are the ones who sat through their CS and information theory classes but emerged without actually understanding the point of it all. Information is information. The fact that it can be encoded in many different ways is neat — it's nearly magical, in fact, and the very essence of why digital technology is so amazingly powerful — but doesn't change its essential nature. Refusing to admit that numbers are only protected *in context* reveals either ignorance of these ideas or simple denial of them.

*crossposted at* `EchoDitto Labs <http://labs.echoditto.com/hddvd>`__
