be your own Aronofsky
#####################
:date: 2006-12-08 12:41
:author: admin
:category: tech
:slug: be-your-own-aronofsky
:status: published
:save_as: 2006/12/08/be-your-own-aronofsky/index.html
:url: 2006/12/08/be-your-own-aronofsky/

I've now got an iSight camera built into the lid of my laptop. Naturally, I've been unable to resist the urge to play with it, so I spent about a minute on Wednesday morning writing a Perl script designed to take a steady stream of images. Then I let it run throughout the day. The results are pretty creepy, like a drug-use montage. And, yeah, a little longer than I'd like — but there are special guest appearances beginning about halfway through.

.. raw:: html

   <p>

.. raw:: html

   <center>

.. raw:: html

   <script type="text/javascript" src="http://blip.tv/scripts/pokkariPlayer.js"></script>

.. raw:: html

   <script type="text/javascript" src="http://blip.tv/syndication/write_player?skin=js&amp;posts_id=116357&amp;source=3&amp;autoplay=true&amp;file_type=flv&amp;player_width=&amp;player_height="></script>

.. container::
   :name: blip_movie_content_116357

   |image1|
   `Click To Play <http://blip.tv/file/get/Sbma44-TheGlamorOfInternetConsulting504.flv>`__

.. raw:: html

   </center>

.. raw:: html

   </p>

The Benny Hill music seemed like a much funnier idea when I was in a post-flight delirium. You should probably just mute it. Oh, and the weird chewing is from the cough drops that I was downing with disgusting regularity.

Lots of other people have taken videos like this one, and I'm sure there are better methods. But if you're curious to try it yourself, here's how I did it:

#. Download and install `iSightCapture <http://www.macupdate.com/info.php/id/18598>`__.

#. | Copy this perl script to an empty directory and run it from there. Use control-C to stop it when you've taken enough shots.

      ::

         #!/usr/bin/perl
         while(1==1)
         {
         # grab a shot and name it in order
         my $time = time();
         `isightcapture $time.jpg`;
         # wait for one second. because of the
         # time isightcapture takes to run,
         # this results in roughly one exposure
         # every three seconds
         sleep(1);
         }

#. | Download and compile `JpegToAvi <http://sourceforge.net/projects/jpegtoavi/>`__ (it may be finicky about compiling on OS X — I had to run it from a Linux machine). Run the executable (while in the directory with all the JPEGs) like so:

      ls \*.jpg \| tr '\\n' ' ' \| /path/to/jpegtoavi -f 30 640 480 > output.avi

#. Edit the AVI in your program of choice — I used iMovie to add the music and strip out the parts where we went for lunch or coffee. Then export it to a compressed format and upload it to your favorite video-sharing site. Don't bother with YouTube: I tried it twice and with a variety of export formats, and it choked on the file each time, producing clips that were only one second long. `Blip.tv <http://www.blip.tv>`__ worked great, though.

.. |image1| image:: http://blip.tv/file/get/Sbma44-TheGlamorOfInternetConsulting504.flv.jpg
   :target: http://blip.tv/file/get/Sbma44-TheGlamorOfInternetConsulting504.flv
