technology!
###########
:date: 2010-01-27 18:29
:author: admin
:category: Uncategorized
:slug: technology
:status: published
:save_as: 2010/01/27/technology/index.html
:url: 2010/01/27/technology/
:private: true

I didn't watch the iPad announcement. Having read `this <http://createdigitalmusic.com/2010/01/27/how-a-great-product-can-be-bad-news-apple-ipad-and-the-closed-mac/>`__ and `this <http://timothyblee.com/?p=2169>`__ -- which I think you should read, too! -- it sounds like it was incredibly disappointing.  Between my laptop, netbook and iPhone, the thing that I wish I could do but can't is read digital content while I'm sitting outside in the sun.  To me the only thing that's interesting about this device is the `psychotic <http://twitter.com/choitotheworld/status/8288754455>`__ level of interest in its announcement that was on display, even by people from whom I wouldn't normally expect it.  I'm increasingly convinced that the enthusiasms that make up geek culture (to the extent that such a thing exists) are part of a larger, communicable pathology that an ever-growing segment of the population is becoming susceptible to -- and not just because it's fashionable.

Anyway! Of today's tech news, I thought that the `PS3's hypervisor getting cracked <http://rdist.root.org/2010/01/27/how-the-ps3-hypervisor-was-hacked/>`__ was much more interesting than the iPad.  Not really in an applied way -- you can already boot Linux on the thing (props to Sony for that), so you've gotta suspect that piracy is the primary aim of these efforts, which is a bit boring (especially since I don't plan to buy a PS3). But the technical details are just *neat*.  The linked account gives a good rundown, but maybe I can explain *why* they're neat.

In the case of the PS1, Xbox and Xbox360, circumventi0n\* techniques were clever but essentially reflective of failures of security design. By contrast, the engineering of the PS3's protection still looks logically bulletproof.  The approach used by geohotz -- who also has done good work opening the iPhone, incidentally -- was to introduce a bunch of very tiny brown-outs into the system, screwing up the progress of the security-related things that it finds itself doing from time to time.  There's more to it than that, of course: he needed to use what access to the system he *was* allowed to establish conditions such that when something went wrong, it was likely to go wrong in a way that was advantageous to him.  As you might imagine, this is a considerably trickier thing than just pulling the plug until the power LED is half-faded (though using an FPGA sounds like overkill to me).

But still!  More than the specific technical prowess involved, this speaks to the incredible difficulty of securing a system over which you can't assert physical control (especially if that system runs too hot to just encase its vulnerable parts in a blob of epoxy).  In that respect it's kind of like `freezing RAM to make it preserve its contents long enough to extract them <http://freedom-to-tinker.com/blog/felten/new-research-result-cold-boot-attacks-disk-encryption>`__ (something done at the program `Tim <http://www.timothyblee.com>`__'s attending, I should note).

\* This is a completely providential typo. I have no idea how it happened, but I'm sure as hell not fixing it.
