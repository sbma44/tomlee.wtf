the stack
#########
:date: 2010-01-29 13:57
:author: admin
:category: Uncategorized
:slug: the-stack
:status: published
:save_as: 2010/01/29/the-stack/index.html
:url: 2010/01/29/the-stack/

A couple of weeks ago, `Bunnie Huang wrote this in response to a piece on NPR <http://www.bunniestudios.com/blog/?p=826>`__:

   Here’s [the part of the NPR story that] I found particularly poignant:

      Two centuries ago, our forebears would have known the precise history and source of almost every one of the limited number of things they ate and owned. They would have been familiar with the pig, the carpenter, the weaver, the loom and the dairymaid. The range of items available for purchase may have grown exponentially since then, but our understanding of their genesis has grown ever more obscure. We are now as imaginatively disconnected from the production and distribution of our goods as we are practically in reach of them, a process of alienation which has stripped us of opportunities for wonder, gratitude and guilt.

   That last sentence, I think, resonates strongly with my personal motivation as a Maker. I dive deeply into the supply chain, learning the processes and understanding the people behind our Things, because it enables me to once again feel the wonder, gratitude, and guilt for the Things we otherwise take for granted. Wonder at the skill of craftsmen and the cleverness of designers; gratitude for the passion and hard work of my peers; and guilt for the sacrifice, waste, and unsustainable practices motivated by an obscure system of perverse economic incentives.

When I was a kid, I fell in love with computers.  The world was incomprehensibly vast and terrifying, but here was a sort of bounded system, created by and therefore obviously understandable by humans, yet still mysterious enough to fascinate.  It was the closest thing to magic that I knew of that I also knew I could master.

So, without even realizing what I was doing, I started to try to learn about computers.  I messed around with AppleSoft BASIC; I set up BBS software; I figured out how to get a dual-modem setup working for 3-person games of Doom; I snipped the keyboard lock wire on my parents' 386 so that they couldn't keep me off of the thing during summer break while they were away at work.

Along the way I began to understand bits and pieces of these systems.  More importantly, I began to understand the larger aesthetic that unified them.  It's a cliche that kids are better at technology than adults -- the joke's now about programming Tivo instead of programming the VCR, but it persists because it's true.  I think that's mostly because kids come to new interfaces with fewer preconceptions about how they ought to work, and with more patience because their time is worth less (I've certainly found myself getting worse at learning new interfaces as I've gotten older and (even) less patient).

But I was *really* good with technology, not just kid-good, and I think it's because I had immersed myself in so much of it.  The thing you have to understand about bad interface design is that it's not a product of stupidity: it's a product of engineering.  There's a reason that your childhood TV's power button made a bigger click than its channel button did.  There's a reason that the channel button only became a button after it was a dial!  At that age, I couldn't explain those reasons.  But I could sense their existence, and became able to make inferences based upon them.

This isn't a project that I've completed, and certainly not one that I've abandoned.  People sometimes refer to "stacks" of technologies that work in complementary ways -- the PHP scripting language runs on the Apache webserver, which runs on a machine using the Linux operating system that also has a MySQL database installed, and together they form the so-called LAMP stack that serves a lot of the web's content.

What the above quote is talking about is what I think of as the stack: the system of abstractions and physical mechanisms that makes digital computing possible.  There is *so much of it*.  It's a good thing, too, because as you chase down an explanation for one mysterious part, the fascination associated with it recedes.  There was a time when I didn't know how web pages worked, and was thrilled to learn HTML.  Now, frankly, I don't give a shit.  But I *am* interested in how HTML is interpreted by Mozilla's layout engine. And how operating systems work. And how those operating systems abstract away the varyingly serial and parallel nature of processors.  And how silicon doping and photolithography produce those processors (and why ever-higher wavelengths frequencies of light are needed for that -- and what limits there are on this technique). Or how sound is stored on a hard drive. And what makes a keyboard's keys rebound, and how USB keyboards are different from PS/2 keyboards. And how copper is mined, and how we create a voltage across huge stretches of it.  And what a voltage is! And why my LCD monitor needs to create such a large voltage to produce light, and how that light is encoded by my retina.  And the way that an HTTP request becomes TCP packets which become ethernet frames, and then how that's all reversed on the other side.

I can give pretty good answers to a few of these questions, perform tolerable hand-waving for others, and am totally at sea for some.  As you might've noticed from my list, I've become less and less interested in what's happening within software's incredibly vast tangle of abstractions as I've gotten older -- the abstraction itself eventually becomes a predictable pattern, and therefore a bit boring.  These days it takes a relatively extreme case of novelty to get me excited about software (typically something that will be completely inscrutable to non-geeks who don't share my now-quite-perverse taste).

And of course there's always more. Really, the computer was a conceptual frame and gateway through which I could start considering every piece of technology, bit by bit.  It's a little more than a hobby and considerably less than a religion, but pondering the stack is important to me.

It's not for everybody, though.  `Here's an example <http://www.rinich.com/post/358597818/i-love-walled-gardens>`__!

   Some of the biggest complaints [about the iPad] come from programmers that say the closed system means people won’t be able to satisfy their computer curiosities. To which I again say: Good! Then they’ll have to satisfy their curiosities about emotional maturity and social interaction and possibly even thinking about making the world a better place.

   It is not productive to spend an hour learning how to change the font on your computer’s clock. Even if while you’re doing that you’re learning about how computers work, you’re wasting your time and getting somewhere trivial very slowly. It reminds me of those copies of Shakespeare schools give children with all the annotations defining words and metaphors and techniques, so that kids can appreciate Shakespeare. It doesn’t work. It just makes Shakespeare look like a cryptogram that you can’t read like you do a normal play. Opening up a system that wasn’t meant to be opened just makes little kids cry.

   The standard response, when I sink so low as to let programmers communicate with me, is: “But Rory, programming is my passion. I was willing to spend that long learning how to code.” No, I think back at them — programmers are not given the satisfaction of hearing my voice. No, you were willing to spend that long because you had obsessive-compulsive problems mixed with an antisocial attitude.

   [...]

   This system is closed! No tinkering! You can browse the Internet, or check your mail, or take notes, or listen to music, but when you’re out of little buttons to press then you’re out of things to do. Discover something else. You are not allowed to delve into the things that nobody ought to care about. You’re forced to get another button, or to put down your pad and make out with the other people wandering, dazed, unsure of what to do.

   But however will children learn how to program? Simple: We will make them applications that teach them how to program. Every kid wants to make video games and Google, so it’s not like having a closed system will make them forget that such things are possible. When they go to learn, however, they will not learn by wasting their time doing things that will never make them happy in life. Instead, they will go to the carefully-screened App Store, and they will search for “How do I make video games”, and they will find a little button that teaches them and gives them a run-time environment in which to tinker. And because the iPad is so elegant and makes elegance so relatively easy, these apps will be elegant. We won’t get a row of advanced text editors too complex for people to understand. We will have a lot of simple, easy things that show us how joyful it is to tinker around, and that reveal their complexity and power as we learn enough to work at that level. I might even try my hand at something like that myself.

There is something to this!  And yet, it's just *wrong* about how to teach programming.  Programs that teach programming are stupid -- they're for tourists.  The motivating impulse is noble, and I'd use one to give a class of students an idea of how computers work, but the talented engineers that emerge from that class will abandon such toys as soon as they can.

This is how people like `Alex <http://al3x.net/2010/01/28/ipad.html>`__ and myself learned to do the things we can do.  Like anyone else, we like some things about ourselves, and we don't like things that we perceive as threats to the cultural dynamics that made us the way we are.

And I think this is why we don't like the idea of the iPad.  More abstraction is good for users and bad for budding engineers.  A kid today will learn much less about engineering from an HDTV's on screen menu than he would from my grandparents' chunky black & white set.  There's just more complexity to sort through, and replacing those raw objects d'engineering with stupid toys that represent what some engineer *thinks* is important about engineering -- well, I'm not sure there's a better alternative, but really it's just adding another layer of abstraction, one that will inevitably have to be peeled back.  The entry point to the stack is getting `further and further away from its bottom <http://feedproxy.google.com/~r/matthewyglesias/~3/i0sJv8S8apQ/the-end-of-hierarchical-file-systems.php>`__; the task ahead of those kids is getting harder and harder.

Fortunately, we're not all going to be issued iPads.  The personal computer will continue to exist.  It's still quite modular, projects like Linux are still going strong, and the geeks of tomorrow will still be able to get a foothold as they begin to figure out how the world works.  But hopefully this explains why things like the iPad are galling to people like me.  My objections aren't really technical; they're cultural.

**UPDATE:** `Tim feels similarly <http://timothyblee.com/?p=2191>`__. Imagine that!
