progressing with processing
###########################
:date: 2006-12-11 22:32
:author: admin
:category: tech
:slug: progressing-with-processing
:status: published
:save_as: 2006/12/11/progressing-with-processing/index.html
:url: 2006/12/11/progressing-with-processing/

I've got a couple of projects in the works centering around novel interfaces — specifically, some hijinks with Asterisk and my poor, neglected `Arduino <http://www.arduino.cc>`__. The only problem with this is that it means I have to have something to interface with. Drat.

So, to resolve this issue I went ahead and wrote an implementation of Tetris in `Processing <http://www.processing.org>`__. Since that's kind of boring, I spent some additional time (okay, a lot of additional time) rewriting my one original contribution to the field of Tetrology: a fancy sinusoidal effect that I came up with in high school (let's hear it for Pascal!). I hope you'll find it as confusing as I do.

Of course, based on early reports from my expert beta tester\ [STRIKEOUT:s], there's a fairly decent chance that this will crash your browser. If it already has, uh, sorry. I'm sure you'll take comfort in the fact that it runs fine on my machines.

**UPDATE:** That's enough browser crashing for one day. I've moved the applet below the fold so that this website doesn't mean instant death for affected users. It's weird that this is happening — I don't think I'm doing anything *too* exotic. And I'd expect Processing to protect me from causing these kinds of crashes (and expect the Java VM, upon which it's based, to offer further protection). I guess that's not the case. Well, maybe a future release of Processing will produce better results. Sorry for the inconvenience.

.. container::

   .. raw:: html

      <applet code="tetris" archive="/2006/12/12/tetris.jar" <br>

   .. raw:: html

      </applet>

   width="150" height="200" mayscript="true">

   .. raw:: html

      </p>

   To view this content, you need to install Java from `java.com <http://java.com>`__

   .. raw:: html

      </applet>
