tech things!
############
:date: 2007-09-05 10:55
:author: admin
:category: tech
:slug: tech-things
:status: published
:save_as: 2007/09/05/tech-things/index.html
:url: 2007/09/05/tech-things/

My apologies, internet. I was being a pretty good blogger for a while there, but this week's looking rough. I'd desperately like to write a convoluted apologia on behalf of Bear Grylls, or explain how a pigeon almost killed me, or emphatically agree that `dragons are awesome <http://pygmalioninablanket.blogspot.com/2007/08/finally-real-summer-movie.html>`__. But for now all that will have to wait. Instead, please accept some bulleted items of a technical nature.

- Item the first! I received my `SuperCard <http://eng.supercard.cn/>`__ in the mail at long last. I'll explain the nefarious things it allows me to do with my gameboy later. For now, suffice it to say that the marginal cost of an experience point just plummeted.
- Tim's recently had a few great posts about the First Sale Doctrine and whether software companies can bind you to contractual terms by printing them on a tiny sheet of paper that you throw out, unread, with the rest of the packaging for Office 2007. His `latest <http://www.techliberation.com/archives/042750.php>`__ is particularly interesting — in it he responds to a criticism involving open source software and its own reliance on software licenses. I think Tim's second point in response is on the money: the use of compiled software is very different from the use of source code.
  Besides, there's no real reason why a more explicit contractual agreement couldn't be imposed on the distribution of open source code. Tim has noted that Microsoft could make you sign a contract to buy Windows, too, but doesn't because it would end up costing them money (and make consumers more aware of the terms of the agreements).
  But the vast majority of open source developers know about the licenses associated with their hobby, even if they can't explain the differences between the GPL, BSD, Apache, Mozilla and LGPL licenses off the top of their heads. I don't think too many lines of code would be lost by requiring some sort of deliberate acknowledgment of a project's license prior to downloading its source.
  But this may all be irrelevant. I'm no lawyer, but my general impression is that the exchange of money can significantly alter a legal landscape — it certainly does in other areas of intellectual property law. I'm not sure whether that works for or against open source evangelists in this case, but I think it's plausible to say that they may occupy a different legal position than that of commercial software vendors.
- Also at Tech Liberation, Adam Thierer `writes about wifi piggybacking <http://www.techliberation.com/archives/042749.php>`__. I already left a lengthy comment there, so if you want to hear my ruminations on the subject you can follow the link. But more practically, I wanted to say that it's really, really easy to set up a connection-sharing arrangement. I recently installed the custom DD-WRT firmware on Emily's router and set it to repeat Scooter's signal (he'd okayed the project at the beginning of the summer). Aside from some `router-specific difficulties <http://www.bitsum.com/openwiking/owbase/ow.asp?WRT54G5_CFE>`__ that won't be relevant for anyone following the directions below, it worked like a charm.
  So if you can get a willing neighbor's faint signal by the window and nowhere else, you might want to think about buying a router to handle the window-sitting for you. It's pretty simple to do:

  .. raw:: html

     </p>

  #. Go to `this page <http://www.dd-wrt.com/wiki/index.php/Supported_Devices>`__ and figure out what the cheapest compatible router is, then buy it. Plan on spending about $50.
  #. Follow `these instructions <http://www.dd-wrt.com/wiki/index.php/Installation>`__, which will guide you through downloading and installing the DD-WRT firmware onto your router. To set up the router as a repeater you'll need to use the v24 release of the firmware, which is still considered beta-quality.
  #. Use `these directions <http://www.dd-wrt.com/wiki/index.php/Universal_Wireless_Repeater>`__ to configure your newly-powerful router into a wireless repeater. It even works with encrypted networks! Well, provided that you have the password. Still, it's incredibly useful and seems to be quite speedy and stable based on my admittedly not-quite-rigorous testing.

- Finally, an `interesting but almost certainly specious argument <http://www.cnet.com/8301-13739_1-9769645-46.html>`__ stating that Comcast's specific anti-Bittorrent measures may be illegal.
