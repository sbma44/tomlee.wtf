java made less godawful
#######################
:date: 2006-10-15 22:56
:author: admin
:category: tech
:slug: java-made-less-godawful
:status: published
:save_as: 2006/10/15/java-made-less-godawful/index.html
:url: 2006/10/15/java-made-less-godawful/
:private: true

Remember `this thing <http://www.aharef.info/static/htmlgraph/>`__? Pretty neat, I know. It made the interrounds back in `May <http://del.icio.us/echoditto/dom>`__ or so. Most people completely misinterpreted it, wrongly assuming that it tells you something about your site's relation to others. In fact, it tells you about your webpage's HTML structure. Not quite as exciting, unless you're a huge dork who gets a thrill out of his wondrously-parsimonious XML code.

But there *is* something fascinating about this project (aside from its value as eye candy, I mean). Check out the credits: `Processing <http://www.processing.org>`__, `Traer Physics <http://www.cs.princeton.edu/~traer/physics/>`__, and `HTML Parser <http://htmlparser.sourceforge.net/>`__. Those last two aren't that interesting — the third is an HTML-parsing library, and the second is a physics library (although `this <http://www.cs.princeton.edu/~traer/randomarboretum/>`__ is kind of cool).

Door number one is where the action is. How have I missed this project for so long? Apparently Processing was designed as an educational tool, providing a quick visual payoff to new programmers. And it does that. But it also provides a quick visual payoff to people who aren't Java programmers, but would like to make something cool-looking and animated that works across platforms. People like me. Check out the fruits of some very brief labor:

.. container::

   .. raw:: html

      <applet code="sine_dots" archive="/2006/10/15/sine_dots.jar" <br>

   .. raw:: html

      </applet>

   width="500" height="200" mayscript="true">

   .. raw:: html

      </p>

   To view this content, you need to install Java from `java.com <http://java.com>`__

   .. raw:: html

      </applet>

Sinusoidal dots may not be that exciting to you (although I do get significant enjoyment out of using the word "sinusoidal"). But the fact that those dots were made with a mere 67 lines of totally-unoptimized code should be — especially since more than half of those lines are variable declarations and stuff to read in configuration directives that could've just been hardcoded. Have a look `here <http://processing.org/learning/examples/storinginput.html>`__ to see just how much Processing can accomplish with very little code.

Still, crappy graphic demos can only get you so far. I wouldn't be nearly as excited about this if not for the `collection of libraries <http://processing.org/reference/libraries/index.html>`__ that are available for Processing — including an implementation of XML-RPC. So you could make one of these visualizations talk to Flickr, or Technorati, or Google, or del.icio.us, or a data source you programmed yourself. There's database, webcam, input and audio stuff, too (just for starters).

Anyway, more on this as I get a chance to play with it. And hopefully more on `how I found it <http://todbot.com/blog/spookyarduino/>`__, too, which is a completely different (yet slightly related) and extremely cool tech platform in its own right.
