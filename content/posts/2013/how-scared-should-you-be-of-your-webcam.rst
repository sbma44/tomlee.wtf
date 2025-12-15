how scared should you be of your webcam?
########################################
:date: 2013-12-19 00:35
:author: admin
:category: Uncategorized
:slug: how-scared-should-you-be-of-your-webcam
:status: published
:save_as: 2013/12/19/how-scared-should-you-be-of-your-webcam/index.html
:url: 2013/12/19/how-scared-should-you-be-of-your-webcam/

Yesterday Tim Lee and Ashkan Soltani reported a `surprising and alarming revelation <http://www.washingtonpost.com/blogs/the-switch/wp/2013/12/18/research-shows-how-macbook-webcams-can-spy-on-their-users-without-warning/>`__: some webcams can be activated without their accompanying light being turned on. This means it's conceivable that criminals or government agents could compromise your computer and take surreptitious pictures of you. It's a frightening prospect.

It's also one that I had more or less deemed impossible based on what I know about electrical engineering. I owe Tim and Ashkan my thanks for teaching me something new.

But I think it's worth delving into exactly what makes this attack possible. The paper their story focuses on concerns one particular attack on one particular type of webcam. Left unanswered is whether vulnerabilities like this one are commonplace. Examining how this attack works can provide some reassurance about engineers' good intentions, but leaves plenty of reasons to worry about their insufficiency.

You can find the paper detailing the attack `here <https://jscholarship.library.jhu.edu/bitstream/handle/1774.2/36569/camera.pdf?sequence=1>`__ (thanks, guan!).

Before we walk through how the attack works, let's establish our cast of characters -- one that's slightly simplified relative to the specifics of this attack, but which will suffice for our purposes.

First, there's your computer. It looks like a computer, and behaves in a computerlike fashion.

Second, there's the webcam microcontroller. This is also a computer! But it's a much tinier, lousier computer -- one that fits on a single microchip. Still, it can run programs, and it can talk to your computer. And we're not going to ask it to do very much: mostly it's just supposed to manage the other components in the webcam and report their outputs back to the computer when asked.

Third, there's the image sensor. It's digital and electronic, certainly, and it even speaks binary code and executes commands, but it doesn't run arbitrary programs. It does have internal states and settings, though -- it's not a completely passive, memoryless device like a lightbulb or motor.

Here's the key diagram from the paper:

|webcam_vulnerability|

On the bottom is the microcontroller. On the top is the image sensor. There is a connection between the two of them labeled "standby". When operating normally, the image sensor will go into standby mode whenever the microcontroller sends a voltage to this connection.

On the right side of the diagram is the LED. Its input side is connected directly to the system's power source (V\ :sub:`cc`), and its output side is connected to the "standby" line. A circuit can only do work when energy flows through it, so when both sides of the LED are set to the same voltage -- when the standby line is "high" -- no current will flow and the LED will remain dark. When the voltage on this connection is low, the image sensor will emerge from standby mode; current will flow from V\ :sub:`cc`, through the LED and out the "standby" line; and light will be generated.

This is a pretty good system! The LED's function is tied directly to something that enables or disables the image sensor. This arrangement can't be undone without cutting wires. Really, that "standby" line looks a lot like a power switch.

But it isn't. The image sensor was designed to be a flexible component that might be used in many different configurations, not just the iSight. This is the norm in electronics, with a few exceptions like the `custom chips <http://en.wikipedia.org/wiki/Apple_A7>`__ that Apple designs for its iPhones. In this case, the image sensor can be configured in different ways by sending it different setup commands from the microcontroller. One can imagine modes for "low light" or "video" or "grayscale", but there are also numerous esoteric settings that are only useful to engineers. In the case of this particular image sensor, it's possible to tell it to ignore any signals it sees on its "standby" pin.

This probably sounds pretty outrageous, but it's not hard to imagine configurations in which this capability could be useful. When prototyping a circuit, minimizing the number of features and connections that must be used can make the process faster and simpler. In some applications the image sensor might be on all the time, making a usable "standby" line irrelevant (or, if not properly grounded and shielded, even a source of buggy behavior).

Alternately, it might seem outrageous that the engineer designing the webcam system overlooked this capability in the image sensor. This is a stronger argument. But this is an easy mistake to make.

`Here's the datasheet for the image sensor <http://download.micron.com/pdf/datasheets/imaging/MT9V112.pdf>`__. At 61 pages it's not especially long (microprocessor datasheets can be thousands of pages), but I think you'll agree that it's not the easiest thing to read. What you probably can't see is that datasheets are often `riddled with errors <http://www.analog.com/en/content/raq_caveat/fca.html>`__. They are usually written by engineers, which produces a terrible product but is better than the alternative. As you might imagine, the result is more or less impervious to editing and verification by humans. Datasheets for very popular or venerable chips can be very good, but for complicated, new or little-used products, they can contain serious problems. Partially for this reason, datasheets often contain information about "reference implementations": partially or wholly built systems that show how the component is supposed to be used with a minimum of complicating details, and which engineers are implicitly encouraged to follow without question.

None of this excuses the webcam engineer's failure to foresee this security hole. But you can imagine how it happened. Having someone manipulate this completely undocumented hardware system, reprogramming a microcontroller to, in turn, reprogram an image sensor to use a counterintuitive operational mode that (for all I know) might be completely idiosyncratic to this image sensor chip? It's tough to get too angry over someone's decision to spend their time on other problems.

Is this comforting? Sort of. It's an awfully specific vulnerability. It's pretty easy to see how to design around it (use the LED to test for power to the image sensor, not the state of its standby line; harden the microcontroller's programming; the paper's authors discuss a number of possible remedies and the occasional tradeoffs they entail). It's clear that the engineer was *trying* to tie the LED's activity as closely and irrevocably to the image sensor's operation as he could, which is the right idea. We have no specific reason to think that similar bugs are present in other webcams that use different chips or have more careful authors.

Still. This is a reminder that the systems we use are wildly complex, executing code in many more places than just the CPU. And it's increasingly clear that many of those places have never been scrutinized for vulnerabilities. It's cheering to see security researchers uncover these problems, but criminals and governments have vastly greater resources and incentives to pursue this work, and have had plenty of time to do so. Some masking tape might not be a bad idea.

.. |webcam_vulnerability| image:: /static/2013/12/webcam_vulnerability.png
   :class: aligncenter size-full wp-image-2703
   :width: 349px
   :height: 428px
   :target: /static/2013/12/webcam_vulnerability.png
