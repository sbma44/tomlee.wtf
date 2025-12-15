giving up on DD-WRT
###################
:date: 2009-05-11 09:26
:author: admin
:category: tech
:slug: giving-up-on-dd-wrt
:status: published
:save_as: 2009/05/11/giving-up-on-dd-wrt/index.html
:url: 2009/05/11/giving-up-on-dd-wrt/
:private: true

My `DD-WRT adventures </2009/05/05/artomatic-update-python-on-the-fonera/>`__ have come to an end. I spent a long time finding the perfect firmware, cramming Python into it, massaging libraries and... found an immovable roadblock.

Here's the thing: in DD-WRT the serial port — which I intend to use for communication between the Arduino and Fonera — is connected to the Linux console. This makes sense: that port is there as an interface of last resort, but it'w only useful if it's actually connected to something like the shell. Unfortunately, a side effect of this is that all incoming communication triggers system commands — regardless of whether it's from an administrator who's just accidentally screwed up his ethernet port or from a microcontroller trying to politely say hello. Worse, the console hogs the serial port, preventing my Python script from reading from it at all.

This linkage is established when the kernel is invoked. That's not an easy thing to change without recompiling DD-WRT. It `can be undone at runtime <http://www.dd-wrt.com/phpBB2/viewtopic.php?t=28104&highlight=stty>`__ using a program called setconsole, but that program isn't compiled into the DD-WRT firmware I have — I'd have to recompile to get it. And if I'm going to recompile things, why not just use `OpenWRT <http://www.openwrt.org>`__? It's smaller, easier to build and more customizable. And while DD-WRT and its community is undoubtedly better for most people trying to simply turn their routers into better routers, OWRT's got more people ready to discuss the esoteric router territory where I've found myself. The order of magnitude difference in the projects' respective IRC channel populations is proof enough of that. Sure, in OWRT exotic network configurations may require a bit more wading through documentation and conf files (as opposed to DD-WRT's pleasantly powerful web interface). But that's a small price to pay if the goddamn thing actually *works*.

So last night I successfully `built <http://kamikaze.openwrt.org/docs/openwrt.html#x1-390002>`__ and `installed <http://wiki.cuwin.net/index.php?title=Flashing_the_La_Fonera_with_OpenWRT>`__ OpenWRT. I had to do it in a `VirtualBox Ubuntu image <http://virtualbox.wordpress.com/images/>`__ — building OWRT on OS X is `possible <http://forum.openwrt.org/viewtopic.php?id=318>`__ but a bit of a pain. Other than that, it went great. I haven't yet put the install through its python-using paces — I found I'd accidentally left a few packages out on my first pass, so after establishing that SSH worked I set it to recompile and went to bed — but every software component I need (python-mini, setconsole, pyserial, stty, etc.) was right there in the menuconfig build system. Clearly *somebody* has gotten these things to work in the past — tonight I hope to be next one to accomplish that feat.
