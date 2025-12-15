wasting money takes a lot of research
#####################################
:date: 2006-10-09 22:33
:author: admin
:category: tech
:slug: wasting-money-takes-a-lot-of-research
:status: published
:save_as: 2006/10/09/wasting-money-takes-a-lot-of-research/index.html
:url: 2006/10/09/wasting-money-takes-a-lot-of-research/
:private: true

A while back I did `a post on DCist <http://www.dcist.com/archives/2005/12/14/dissecting_the.php>`__ about pulling apart our subway system's SmarTrip card. I've been meaning to follow up, but wasn't quite sure what to do. The obvious next step is to try to get some data off of WMATA media. I actually took a stab at this with the old magnetic farecards, ordering the `necessary parts <http://stripesnoop.sourceforge.net/faq.html#a17>`__ and never receiving them from DigiKey.

But magstripes are boring anyway. Pulling data from the SmartTrip would be considerably more exciting. But where to begin? My acetone-powered adventures notwithstanding, it's tough to even know what technology is inside the SmarTrip, much less how to access it. How should one go about figuring this out? The totally unsurprising answer: use Google.

It turns out that the SmarTrip is `actually a "GO CARD" <http://lnweb18.worldbank.org/External/lac/lac.nsf/Sectors/Transport/FCB7AB38B086D96F852568B200777333?OpenDocument>`__ manufactured by a company called Cubic that makes `videogames for the military <http://www.cubic.com/ecc/cctt/index.html>`__, `complicated charts <http://cubic.com/cts/sysdiagram.htm>`__ and wireless farecard thingamajigs. And look! It's a gigantic `datasheet PDF <http://www.itsc.org.sg/plugfest/pf_documents/pf2004/CryptoSC-6-Cubic.pdf>`__, which reveals that GO CARDS are modified `ISO 14443 B <http://en.wikipedia.org/wiki/ISO_14443>`__ cards.

That internet says that means that they run on the 13.56 MHz frequency, which means that `for a mere $96 <http://www.sonmicro.com/1356/sm1013.php>`__ I could get an RFID dev kit that'd let me talk to the chips. Probably.

But surprisingly, I'm not ready to drop that much money on a blog post. Yet.

**ALTHOUGH:** Section 4.4.0 of `this document <http://64.233.161.104/search?q=cache:BkRfDOdZAGcJ:www.apta.com/about/committees/utfs/standard/documents/trends_in_electronic_fare_media_1_5.doc+trends_in_electronic_fare_media_1_5.doc&hl=en&gl=us&ct=clnk&cd=2>`__ makes me think I shouldn't waste my time — they namecheck `Bruce Schneier <http://geekz.co.uk/schneierfacts/>`__. Since doing that is about the extent of my own knowledge of cryptography, I figure I'm probably outgunned.
