so here's something kind of fun
###############################
:date: 2007-02-26 14:03
:author: admin
:category: tech
:slug: so-heres-something-kind-of-fun
:status: published
:save_as: 2007/02/26/so-heres-something-kind-of-fun/index.html
:url: 2007/02/26/so-heres-something-kind-of-fun/
:private: true

I've been screwing around with `Processing's <http://www.processing.org>`__ video capabilities ever since doing a demo on it during out tech meeting at work a few weeks ago. It's pretty neat, and getting all the neater with the sudden ubiquity of iSight cameras.

I initially thought that there was a somewhat glaring security hole to all of this that would potentially allow a website operator to take snapshots of users without them noticing. Turns out that's not the case: an applet has to be signed in order for the camera libraries to work in a web browser. That means it either needs to come from a very trusted source (say, Sun Microsystems) or the user has to sign off on a security warning.

But even without the potential for sneakiness, this is still pretty neat. Here's a first pass at it that I thought I might as well post online. It's a pretty simple tech demo — it just distorts your image in a fun way. But the potential of the technology is amazing, mostly by virtue of how amazingly accessible it is. If you've got a webcam, click on the image below and say "ok" to the security warning. And don't worry: this applet doesn't send your picture anywhere. That'll be coming in a future blog post (and yes, I'll warn you).

I'm pretty confident that this works OK on Macs, but things may be dicier on Windows. When it comes to Java stuff there's always a chance of unexpected browser crashing, so please don't leave anything important unsaved in any of your other tabs.

.. raw:: html

   <p>

.. raw:: html

   <script type="text/javascript"><br />
   function replaceDiv()<br />
   {<br />
   var videodiv = null;<br />
   if (typeof($)=='function')<br />
   videodiv = $('processing-sinevideo');<br />
   else<br />
   videodiv = document.getElementById('processing-sinevideo');<br />
   if(videodiv!=null)<br />
   videodiv.innerHTML='<applet code=\'processingdemo_video\' archive=\'/static/2007/02/26/processingdemo_video.jar\' width=\'320\' height=\'240\' mayscript=\'true\'>
   <param name=\'image\' value=\'loading.gif\'>
   <param name=\'boxmessage\' value=\'Loading Processing software...\'>
   <param name=\'boxbgcolor\' value=\'#FFFFFF\'><!-- This is the message that shows up when people don\'t have Java installed in their browser. Any HTML can go here  (i.e. if you wanted to include an image other links,  or an anti-Microsoft diatribe. -->To view this content, you need to install Java from <a href=\'http://java.com\'>java.com</a></applet>';<br />
   }<br />
   </script>

.. raw:: html

   </p>

.. container:: center
   :name: processing-sinevideo

   |click here to launch the applet|

.. |click here to launch the applet| image:: /2007/02/26/20070226_appletlaunchbg.gif
   :width: 320px
   :height: 240px
   :target: #
