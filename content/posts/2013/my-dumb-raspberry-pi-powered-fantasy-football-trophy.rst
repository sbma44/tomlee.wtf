My Dumb Raspberry Pi-powered Fantasy Football Trophy
####################################################
:date: 2013-12-28 22:11
:author: admin
:category: Uncategorized
:slug: my-dumb-raspberry-pi-powered-fantasy-football-trophy
:status: published
:save_as: 2013/12/28/my-dumb-raspberry-pi-powered-fantasy-football-trophy/index.html
:url: 2013/12/28/my-dumb-raspberry-pi-powered-fantasy-football-trophy/

Well, another fantasy football season is behind us. I entered the season as the reigning champion and left it as the... not champion. It would be churlish to try to make excuses for my poor showing. So instead I'll simply note that there is an ongoing, pressing need for organ donors in this country, and many of my fantasy players' families are proud to have done their part. My heartfelt congratulations to Ben on his apparent championship and the masterfully subtle campaign of cheating that must surely lie at its foundation.

But the season did have a few bright spots, even beyond the news that my WR1 is expected to walk again. In particular, I embarked on a semi-ridiculous project to build a Raspberry Pi-powered fantasy football meter. It worked out pretty well!

I should probably begin by assuring you that I'm not actually all that maniacal about fantasy football. It was a purchase that spurred this project: a few months back I bought `a big lot of antique electrical gauges on eBay <http://instagram.com/p/cNGn1EvEFn/>`__.

(OK, actually I bought two lots.)

Since then I've been building some little projects with them using Raspberry Pis and lasercut wooden enclosures. The fantasy football meter is one of the more grandiose examples.

The top gauge measures my ranking in the league. The bottom gauge measures how many points ahead or behind I am at the moment. I realize that this is deeply stupid.

It's fair to say that I have been working to (slowly) accumulate the expertise necessary for these projects for `more than half a decade <http://dcist.com/2008/04/transit_on_thur_27.php>`__. It's made me really, *really* wish that I had taken some electrical engineering classes in college.

Still, I've learned a lot during this process! So why not blog about some of those things?

Cut A Hole In The Box
---------------------

3D printing gets a lot of attention, and it is indeed frighteningly neat. But for my money a good old-fashioned robotic lasercutter is even more exciting. Anyone who has turned an IKEA flat-pack into an unattractive wine rack will be familiar with the basic principles underlying my approach.

Conceptualizing the transformation from two to three dimensions is trivially easy for some people and essentially impossible for others. I fall somewhere in the middle, and find that I am best served by workshopping a given geometric idea under a variety of pharmacological conditions -- specifically alcohol, caffeine and post-workout endorphines. Probably there is some nootropic cocktail available on the streets of San Francisco that delivers innovative furniture design insights and permanent synaptic damage instantaneously, but I'm uncool enough to require lengthy periods of mulling instead.

I would dearly love to employ interesting woodworking techniques, but working in two dimensions more or less mandates the use of `finger joints <http://en.wikipedia.org/wiki/Finger_joint>`__. And really, that's fine. The one thing you have to watch out for is *kerf*. Lasercutters work by vaporizing a small amount of material. The width of this area -- called kerf -- usually amounts to just a tenth or fifth of a millimeter, but it does add up.

I've written some `python scripts <https://github.com/sbma44/fingerjoint>`__ to help generate finger joint geometries that account for tedious kerf calculations automatically. They do require quite a bit of fiddling and subsequent modification in Illustrator or Inkscape, but they work well enough. A nicer online application can be found at `makercase.com <http://www.makercase.com/>`__, but I know my code and like it well enough.

|image1|

I used `Ponoko <http://ponoko.com>`__ for this particular trophy, and they provide a wonderful service. But `HacDC <http://hacdc.org>`__ now has a lasercutter, and though it's less powerful, you can't beat the price and turnaround time. I'm still experimenting with materials, but have purchased a bunch of stuff from `laserbits.com <http://laserbits.com>`__ that I hope will produce good results.

Raspberry Foray
---------------

I've spent a lot of time playing around with Arduino, and the experience has taught me a lot. But if you want to connect to the internet -- and look at you, of course you do -- you're going to want to turn elsewhere. I spent quite a bit of time on the `BeagleBone <http://beagleboard.org/bone>`__, and I admire its commitment to openness.

But there is no competing with `Raspberry Pi <http://raspberrypi.org>`__ right now. It wins on price. It wins on its choice of native distro. Most importantly, it wins on community. Next to these things, its just-OK (nongraphical) technical capabilities are afterthoughts.

Still, making the damn thing useful in embedded applications takes some thought! I have condensed a number of these lessons into `this repo <https://github.com/sbma44/rpi/>`__. You might want to borrow parts of it (you probably won't want all of it). Among the things the bootstrap.sh script and its siblings accomplish:

- Installs Bonjour so you can get to the Pi without looking up its DHCP-delivered IP address
- Gets a decent Python environment in place, complete with virtualenv
- Installs the `wiringpi and wiringpi2 libraries <http://wiringpi.com/>`__, which are what you'll want to use to control the General Purpose Input/Ouput (GPIO) pins on the device
- Sets up my default wifi networks. Whoops! You probably don't want that. But use this `/etc/network/interfaces <https://github.com/sbma44/rpi/blob/master/interfaces>`__ and `/etc/wpa_supplicant/wpa_supplicant.conf <https://github.com/sbma44/rpi/blob/master/wpa_supplicant.conf>`__ file templates to get yourself online. Note that you can have more than one network={} statements in the latter.
- Gives my SSH key root on the system. You probably don't want that either.
- Turns off the swap file. Swap files are the means by which your disk impersonates RAM to expand your system's capabilities. It's a super-neat idea in general, but less so if your disk self-destructs the more often you write to it -- which is indeed the case with a flash SD card. You should find a way to make do with physical memory. I've gone through a lot of SD cards.
- Relatedly! And not present in this install script! You should turn off journaling in the filesystem. Instructions can be found `here <http://raspberrypi.stackexchange.com/questions/169/how-can-i-extend-the-life-of-my-sd-card>`__. Journaling is a neat idea by which every change to the filesystem is first cached in a central location before being executed as a transaction. This allows for graceful recovery from a number of failure modes that can occur if an operation that requires multiple steps -- and which really, really needs to complete all of them for things to make sense -- is abruptly interrupted by a power loss or other failure. But that caching requires a *ton* of writes to disk, and will burn up your SD card in short order. You'll just have to get by without journaling, and commit to pulling the power as little as possible
- The script also `turns on the watchdog module <https://github.com/sbma44/rpi/blob/master/watchdog.py>`__ in the Broadcom processor that lives at the heart of the Pi. This is a little piece of hardware that listens for a heartbeat signal from the system and, if it doesn't hear one, reboots everything. Step one is turning on the hardware; step two is setting up the heartbeat. This can give your system a gentle kick when something you've done screws it up.
- Want to install a Python script in your virtualenv as a system service that starts at boot? I've made that `fairly simple <https://github.com/sbma44/rpi/blob/master/make_init.py>`__, though the script does bake in a few assumptions about your directory structure.
- Optionally, `this script <https://github.com/sbma44/rpi/blob/master/postfix.sh>`__ will help you set up outbound mail via your Gmail account
- Finally, there's `a script <https://github.com/sbma44/rpi/blob/master/phantomjs.sh>`__ to install an ARM processor-compatible version of `PhantomJS <http://phantomjs.org>`__. More on that in a sec.

Some things are best done once, however. For a long time I installed whatever the `latest Raspbian image <http://www.raspberrypi.org/downloads>`__ was, then went through the raspi-config script (which launches automatically on the first boot) and then ran my bootstrap script.

This takes forever, though. I got particularly sick of reconfiguring raspi-config to expect a non-UK keyboard.

But creating a new and improved disk image eluded me for a while. Installing all the aforementioned junk requires that you expand the filesystem to use more of the SD card (the default uses only 2GB). But if you use the dd tool to image the result, it'll show the full size of the SD card. And an image of one 4GB SD card (for instance) won't necessarily fit on a different model or brand of 4GB SD card. (You should be using 8+GB cards anyway, to minimize system failures due to repeated writes to the same sector.)

The solution: `expand the filesystem manually to 3GB or so <http://elinux.org/RPi_Resize_Flash_Partitions>`__. Use raspi-config to assert your American independence. Get everything set up. And then record an image using something like this:

   sudo dd if=/dev/disk1 of=preconfigured_raspberry_pi.img bs=1048576 count=3000

This instructs dd to copy from /dev/disk1 in 1 megabyte chunks, and to pull three thousand of them. The remaining five thousand or so (on an 8GB card) can simply be ignored, I think? Honestly, it's a bit difficult to keep track of which levels of filesystem abstraction and definition are included where. Perhaps those missing five thousand megabytes will come back to haunt me someday. But not yet.

Somehow the Vital Connection is Made
------------------------------------

All of the above gets us a wooden box and a cheap and useful Linux environment. How do we make it actually translate Things On The Internet into a dial moving... somewhere?

Well, first you'll need a wifi adapter. I tend to buy `this one <http://www.amazon.com/gp/product/B0069LOX7K/ref=wms_ohs_product?ie=UTF8&psc=1>`__, which is tiny, less than ten dollars, compatible with the Raspberry Pi default distro without any additional drivers, and can mostly connect to wifi networks without exceeding the Pi's rather wussy USB power capabilities. But there are other perfectly fine choices out there.

Getting wifi working on Linux is awful under the best of circumstances, but when done without a GUI it easily competes with the most imaginative punishments Greek mythology can offer. Please, please use the /etc/network/interfaces and wpa_supplicant.conf patterns linked above. For me, they're the culmination of more than a year's worth of trial and error across multiple embedded systems (next time you see me, ask to see my `FUCK CONNMAN <https://connman.net/>`__ tattoo). Others will have wisely gone straight to LadyAda's `excellent series of Raspberry Pi lessons <http://learn.adafruit.com/category/learn-raspberry-pi>`__, from which this solution is cribbed.

But wifi connectivity is only the beginning.

A Ghost Is Born
---------------

Fantasy football is one of those strange areas of human endeavor in which Yahoo is successful. It's free and it's what my friends and I use, anyway. And it's comforting to begin to know the annual rhythms: unnecessary redesign, mobile app flakiness, disastrous week 1 server outage, ensuing apology, eventual system stability. I look forward to repeating the cycle next year.

Alas, the API seems basically useless for anything beyond establishing that Yahoo runs a fantasy football service. So we're going to be screen-scraping, navigating and disassembling messy HTML pages in just the same way that your browser does.

This is not a reliable process. Worse still, Yahoo counts on tons of Javascript to render portions of the page after the initial HTML has been delivered. Knowing what is supposed to happen after that point requires a Javascript interpreter, which is a sophisticated piece of machinery beyond most scripting environments. Instead, you have to connect your script to a browser and ask it, intermittently and politely, what the hell is going on right now.

This task used to be so hellaciously finicky that I'd never gotten it to work. But `Phantom.js <http://phantomjs.org/>`__ has removed most of those difficulties, and as I mentioned above, there's a compiled version for Raspberry Pi which can simply be copied onto the device and used. I employed the Selenium Webdriver interface, but mostly because of peer pressure. I've been hearing good things about `Casper.js <http://casperjs.org/>`__.

Yahoo ensures that this will not be the end of your woes, but I've encoded a number of hard-fought lessons in `this Python class <https://github.com/sbma44/doughmeter/blob/master/yahoofantasyfootball.py>`__, and will probably update it once the 2014 season redesign arrives and breaks everything. (The rest of the code for the meter is `here <https://github.com/sbma44/doughmeter>`__, incidentally.)

Moving the Needle
-----------------

The last piece of the puzzle: making the damn needles move. Most of the excitement is already recorded in `this post <http://www.manifestdensity.net/2013/03/10/texameter/>`__. But in short: microcontrollers are all-or-nothing beasts, setting output pins to zero volts or ALL THE VOLTS (3.3 in the case of the Pi). But they can approximate intermediate values by turning a pin on and off very rapidly, with the ratio of on:off determining the voltage that's being approximated. This is called pulse width modulation, and the Pi has built-in hardware that allows it to deal with this constant switching without expending any brainpower -- but only on one pin.

Luckily, the wiringpi library has included as sophisticated a system for additional, software-controlled pins as one could hope for, though each additional pin comes at the cost of a bit more CPU utilization. Fortunately we only need two for this meter (the -100 to +100 meter is actually set up to behave as if it's two separate meters).

The vintage gauges themselves are not configured for 3.3v, of course. But that's where trim potentiometers come in:

Those `little blue and white dials <http://www.flickr.com/photos/sbma44/10102908783/>`__ labeled 1, 5 and 6 are the trim pots in question. Some trial and error can deliver resistor levels that max out the meter's range without overpowering it. The gauge's response might still not be perfectly linear, but that's where `this little library comes in <https://github.com/sbma44/pwm_calibrate>`__.

Wrapping Up
-----------

All that's left is to add a little flair:

Ben will get a plaque now, too. I guess.

.. |image1| image:: http://www.manifestdensity.net/static/2013/10/kerf_demo.png
   :class: center
