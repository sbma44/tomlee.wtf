beat me to it
#############
:date: 2007-06-15 11:15
:author: admin
:category: tech
:slug: beat-me-to-it
:status: published
:save_as: 2007/06/15/beat-me-to-it/index.html
:url: 2007/06/15/beat-me-to-it/
:private: true

|a 555 timer chip|\ Ever since `reading <http://www.wired.com/news/technology/0,71087-0.html?tw=rss.index>`__ about the body-modification folks who've implanted magnets in their fingers I've been `kind of fixated <http://www.zunta.org/blog/archives/2006/06/07/oh_dear/>`__ on the idea. Being able to sense magnetic fields seems like it'd be awfully cool. But even if the unavailability of anesthesia for the operation wasn't enough to scare me off, the apparently-guaranteed infection that follows would be.

As my meager knowledge of electronics has grown, the idea of building a tool has begun to seem more feasible, and promises to merely result in finger burns instead of outright amputations. I've been screwing around with a 555 timer and pricing Hall Effect sensors in preparation for building a gadget that'll whistle to me when it feels a field.

But `look <http://www.instructables.com/id/EXPHY2GW12ERXTRZAS/?ALLSTEPS>`__! Someone already built *the exact same thing* and put it on Instructables. It's a good thing, too, since I a) didn't realize that Hall sensors put out varying voltage instead of resistance and b) wouldn't know how to change a 555's timing on that basis. In fact, due to my unwillingness to untangle resistors and figure out their `color codes <http://www.zambetti.com/projects/resistulator/>`__, my 555 circuit keeps threatening to melt down. I'd still like to put this together, but I may substitute a vibrating motor that I scrounged from a walkie-talkie instead of making it sound-based — turning it into a tactile feedback mechanism seems like it'd do more to satisfy my fingermagnet lust.

At any rate, it's cool to see that the idea's workable, even if it's slightly disappointing to be beaten to the internet writeup of what I thought was an original(ish) idea.

The curious can find a little pedantry from a decidedly underqualified electronics expert after the jump.

The gadget works thanks to three components. First, there's a `555 timer <http://www.google.com/custom?domains=makezine.com&sitesearch=makezine.com&q=555&sa.x=0&sa.y=0&cof=GALT%3A%23008000%3BGL%3A1%3BDIV%3A%23336699%3BVLC%3A663399%3BAH%3Acenter%3BBGC%3AFFFFFF%3BLBGC%3A336699%3BALC%3A0000FF%3BLC%3A0000FF%3BT%3A000000%3BGFNT%3A0000FF%3BGIMP%3A0000FF%3BFORID%3A1%3B&client=pub-1711976718738240&forid=1&ie=ISO-8859-1&oe=ISO-8859-1&hl=en>`__, a venerable chip that can be bought at Radioshack for about fifty cents. This ingenious little device can be wired up to do two things: it can either act as a one shot timer, turning on an output for a configurable amount of time and then switching off; or it can act as an oscillator, switching an output on and off continuously at a configurable rate. The first mode of operation is called monostable mode; the second is called astable mode. You generally configure the delay by swapping different-sized resistors and capacitors into a very `simple <http://home.cogeco.ca/~rpaisley4/LM555Monostable.GIF>`__ `circuit <http://home.cogeco.ca/~rpaisley4/LM555Astable.GIF>`__ that contains the 555. It's great for projects that flash lights or need to trigger action after a set delay, and it makes for a good Baby's First Integrated Circuit. That's certainly why I'm using it.

In this case the 555 is set up to work in astable mode, switching its output on and off very quickly. Its output is connected to the second major component, a piezoelectric element. This is a little ceramic disc that expands and contracts ever so slightly when voltage is applied to it. You may have run into piezoelectrics in advertisements for fancy pseudoscientific skis, or you may have heard about how quartz crystals work to keep time. It's pretty much the same deal. You can buy one at Radioshack for a couple of bucks. In this case the expansion and contraction is occurring so quickly — thanks to the 555 timer — that it actually generates sound waves. I'm not sure what the 555's nominal oscillation range is, but it's not hard to get it to fall within the ~20-20000 hertz range of the human ear.

The final bit is the sensor, which works thanks to something called the Hall Effect. In the absence of a good explanation, I'll simply state that it's magic. The spell amounts to this: stick it in a magnetic field and the voltage of a current run through the sensor will vary based upon the magnetic field's strength. Radioshack doesn't stock these guys, but they can be acquired from Digikey for a few dollars. You also might be able to scrounge one out of those ridiculous battery-powered home security alarms that you stick on windows — you know, the ones that come in blister-packs for $20 or so. That's how the window alarms operate: one side has a permanent magnet in it and the other has a Hall sensor. If the window is opened the magnetic field goes away, the sensor detects the change and an alarm is triggered. Hall sensors are used in all kinds of mechanical systems that need to detect the position of something without actually coming into physical contact with it. `Here's <http://www.instructables.com/id/EEVRBRUWWIES9J6KPG/>`__ an instructable where a Hall sensor is used to count how many times a drill head has rotated.

The basic idea here is that the Hall sensor's output changes the characteristics of the circuit that govern the 555's oscillation rate. When that rate changes, the pitch of the sound generated by the piezoelectric element is altered. For a lot of sensors, the internal resistance changes in relation to whatever's being sensed. You incorporate the sensor into the portion of the 555 circuit that determines its timing based on resistance, et voila. But in this case the sensor changes its output voltage, which the instructable author deals with by feeding it into the 555 in a way that is probably pretty simple, but never would've occurred to me.

The rest of the circuit is just stuff to regulate the power supply. It's a pretty simple doohickey, but I still think it'd be fun to build.

.. |a 555 timer chip| image:: /static/2007/06/15/20070615_555.jpg
   :class: right
   :width: 250px
   :height: 250px
