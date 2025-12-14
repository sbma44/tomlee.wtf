smash
#####
:date: 2008-03-18 11:07
:author: admin
:category: tech
:slug: smash
:status: published
:save_as: 2008/03/18/smash/index.html
:url: 2008/03/18/smash/

Super Smash Bros. Brawl was waiting for me when I got home on Sunday thanks to a years-old, barely-remembered gift card from my mom (thanks, mom!). Wanna play? My friend number is 0645-5578-9044.

In other Wii news, it looks like the homebrew scene is heating up a bit. First, there was this:

.. raw:: html

   <p>

.. raw:: html

   <center>

.. raw:: html

   <object width="425" height="355">

.. raw:: html

   <embed src="http://www.youtube.com/v/H5YB1Mmx7E4&amp;hl=en" type="application/x-shockwave-flash" wmode="transparent" width="425" height="355">

.. raw:: html

   </embed>

.. raw:: html

   </object>

.. raw:: html

   </center>

.. raw:: html

   </p>

At the CCC these guys presented a significant advance. The Wii can emulate the Gamecube console that preceded it. And software tools for running homebrew applications on the Gamecube are, as you might expect, better developed than those for the Wii. Those tools can run on the Wii, but only in Gamecube mode, which locks programs out of the console's enticing new features — things like Wiimote control and network connectivity. These guys found a way to scan the device's ordinarily-protected memory space from Gamecube mode and plucked some encryption keys from it. Using those keys they can create discs that the Wii thinks are Wii games, which consequently have complete access to the console's hardware resources. Neat, huh?

But more immediately relevant to home users is the so-called "Twilight Hack", which debuted in February. The Zelda game for the Wii is called The Twilight Princess and it contains that perennial favorite, a buffer overflow vulnerability.

Think of it like this: a computer's memory is filled with a very long list of things it has to do, and it proceeds through these steps in order. Some of these instructions tell it to jump to other places in the list, some of them tell it to manipulate different parts of the list, and some of them tell it to run comparisons on the list and do different things depending on the result. In simple systems the memory is allocated as needed, which can result in a chunk of data like an image sitting next to a chunk of code that will actually be fed to the processor. As you might imagine, maintaining the boundaries between these regions is important.

But it's easy to screw up and forget to do it when loading a file's contents into memory, particularly on a platform like a console. Hey, why bother checking, say, a save game? If it's only your code that's writing the file, and it checks the content's length when it writes it, why check again when you read it? You trust your file-writing code, and where the hell else are save files going to be coming from?

The answer, of course, is hackers. In this case they took a save file and discovered that when it's loaded there's no check on the length of the text string that names Link's horse. So you write a super-long string and when it's loaded into memory it not only writes into the memory set aside for the horse name, but also into the memory after it. You fill that up with what's called a no-op sled — a long list of instructions saying "no operation; do nothing, go to the next step", at the end of which you put some code that gives you control of the system in one way or another. When, during the normal execution of the game, the processor reads a legitimate instruction telling it to jump somewhere into that no-op-filled region and start executing instructions it will slide allllll the way down the sled and then run your system-pwning code. The sled lets you avoid needing to know precisely where the processor is going to begin reading, improving your odds of getting your code executed.

This, incidentally, is also the technique used to "softmod" an Xbox. There are three different Xbox games that don't properly check their savegames. That's an easy point of entry for a file with a custom payload. The game will have already passed all the security checks built into the system, meaning that any code you can introduce into memory will be treated as part of the game itself — and frequently this will be enough to let you tear down any lingering security for good.

Initially the Twilight Hack required a special (though commercially available) Gamecube SD card adapter, but it's now been improved to the point where you can use the Wii's built-in SD reader, allowing user-created code to be booted from the card slot in the console's front:

.. raw:: html

   <p>

.. raw:: html

   <center>

.. raw:: html

   <object width="425" height="355">

.. raw:: html

   <embed src="http://www.youtube.com/v/IowCjQb6dQA&amp;hl=en" type="application/x-shockwave-flash" wmode="transparent" width="425" height="355">

.. raw:: html

   </embed>

.. raw:: html

   </object>

.. raw:: html

   </center>

.. raw:: html

   </p>

So far it looks like Linux, emulators and a homebrew version of Tetris are available. That's pretty much par for the course when a new system is opened up: those first two are huge piles of useful code that are freely available, requiring work to adapt but not any original design. Small games like Tetris are also pretty common, serving as necessary learning exercises for probing how the console's various hardware functions operate.

But will there be a proliferation of other software? I'm doubtful. The homebrew scenes for the Dreamcast and Gamecube are cool but haven't yielded any killer apps. The Xbox scene has been more successful, but largely because of the console's beefy specs, onboard hard drive and widely-pirated software development kit. If I had to bet I'd say that continued refinement of WiiLinux and the emulators can be expected, and that there may be a few apps showcasing `Johnny Lee's neat Wii demos <http://www.cs.cmu.edu/~johnny/projects/wii/>`__. Maybe there'll be an underpowered media player, too, and a few lousy games. But that will be about it.

Except, of course, for one other application: piracy. The binary game dumps `are out there <http://thepiratebay.org/browse/405>`__, and we can now run arbitrary code. I haven't looked for a writeup yet, but I can guarantee you that someone out there is using Twilight Princess to load pirated games from their Wii's SD card slot.
