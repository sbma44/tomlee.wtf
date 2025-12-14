iPhone presence detection
#########################
:date: 2008-01-24 11:42
:author: admin
:category: tech
:slug: iphone-presence-detection
:status: published
:save_as: 2008/01/24/iphone-presence-detection/index.html
:url: 2008/01/24/iphone-presence-detection/

I have `a post up over at EchoDitto Labs <http://labs.echoditto.com/iphone-presence-detection>`__ talking about detecting the presence of an iPhone over a wifi network.

The basic idea is pretty simple: you set up your router so that it always gives the phone the same IP address (you \*are\* running a `custom Linux firmware <http://dd-wrt.com/dd-wrtv2/index.php>`__, right?). Then you run a script every minute or so that pings the phone's assigned address (the script can also be run on the router). Depending on whether the ping is successful, you perform an action — in the post I just log the results and then graph them, but it'd be just as easy to have the router load a given webpage. I'm thinking that it might be neat to have my router and Emily's router both report to this site whenever they see me. I could use that data to populate a little box on the sidebar indicating whether I'm in Philly or DC. Or at work, I suppose.

But I'm not sure what granularity I want to provide for such a display, or if it'd actually be useful to anybody. It is, I admit, pretty creepy.
