cablemodem bleg
###############
:date: 2008-01-24 11:50
:author: admin
:category: tech
:slug: cablemodem-bleg
:status: published
:save_as: 2008/01/24/cablemodem-bleg/index.html
:url: 2008/01/24/cablemodem-bleg/
:private: true

The Comcast installation guys came by yesterday, and I said a sad goodbye to our beloved DirecTivo. The Comcast DVR seems pretty lame, but it's indisputably hi-def. I can see the marks on Michael Chiarello's cutting board! I can see the mottled horror of Fox 5 special correspondent `Logan 3 <http://en.wikipedia.org/wiki/Logan%27s_run>`__! It looks great, even if the software doesn't have a very consistent idea of what the "back" button is supposed to do (you might think the answer would be "go back", but that just betrays your lack of imagination).

We haven't got internet service yet, though. I thought I had a cable modem kicking around, but so far haven't been able to find it. The Comcast guys offered me a modem with an integrated router, but that would've cost us an extra $2 per month. More importantly, it would've brought the total number of active, transmitting wifi routers in the apartment up to five\*. Even I realize that's too many.

So: if you happen to have a spare cablemodem lying around that you wouldn't mind parting with for an eBay-ish price, please let me know. I admit that I'm not too keen to begin using Comcast's internet service after reading (and writing) so much about their Bittorrent-throttling shenanigans. But — chalk up another vote for custom Linux firmwares — my Linksys router runs iptables, which means that adding `this <http://autoignition.net/2007/10/17/comcast-bittorrent-seeding-fix/>`__ to its startup scripts should make it ignore the forged RST packets that Comcast is using to stymie seeders. I think it'll still be a step up from our decrepit Verizon DSL.

**UPDATE:** Crap, nevermind. `It looks like Comcast sends reset packets in both directions <http://www.dslreports.com/forum/r19036168-Tests-and-ResultsRSTs-are-set-in-both-directions>`__, which means that iptables-based fixes won't do anything unless they're implemented for both you and the person with whom you're exchanging data — and the odds of that being the case aren't very good. Boo.

\* hacked WRT54G running Sveasoft, generic Netgear WDS box, hacked Fonera running DD-WRT, regular Fonera, Comcast box
