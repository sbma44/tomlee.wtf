DIY eye-fi server: docker, flickr, all sorts of good stuff
##########################################################
:date: 2017-04-20 17:24
:author: admin
:category: Uncategorized
:slug: diy-eye-fi-server-docker-flickr-all-sorts-of-good-stuff
:status: published
:save_as: 2017/04/20/diy-eye-fi-server-docker-flickr-all-sorts-of-good-stuff/index.html
:url: 2017/04/20/diy-eye-fi-server-docker-flickr-all-sorts-of-good-stuff/

|image1|\ The Eye-fi is an SD card with an embedded wifi chip. Configure it, put it in your camera and it can wirelessly upload photos without human intervention. It's a neat gadget, even if I never did manage to get my mother's working for her.

Alas, Eye-fi's software accomplishes this feat by running in the background of an always-on desktop computer. Worse, they've been steadily eroding their services' capabilities, stripping away integration with photosharing sites people actually use in favor of their own cloud photo service (don't worry, the first year is free).

A few intrepid geeks reverse-engineered the early Eye-fi cards, but enthusiasm seems to have diminished as Eye-fi's services changed and their early-gen cards stopped working. Nevertheless, the techniques they discovered and software they wrote still work... well, they almost worked. There were some rough spots.

I have a baby on the way (did I mention that?) and expect to be generating lots of photos. So I have taken one `low-dependency-count open source project <https://github.com/dgrant/eyefiserver2>`__ and given it a fresh coat of paint. In addition to the satisfaction of knowing you are running slightly more reputable Python, the system is now able to upload your photos to Flickr, if you let it. And it runs in Docker (`renamed as of today to Moby, ugh <https://news.ycombinator.com/item?id=14156954>`__), which should remove many of the idiosyncratic configuration headaches that would otherwise make sharing a project like this a masochistic declaration of one's intent to provide free tech support, forever.

If any of this sounds useful I hope you'll `give it a look <https://github.com/sbma44/eyefi-docker>`__. It has already happily uploaded many debug photos of my coffee table to Flickr from my a household Raspberry Pi. Perhaps it will prove equally helpful to you.

.. |image1| image:: /static/2017/04/eyefi.png
   :class: alignright size-full wp-image-3071
   :width: 345px
   :height: 317px
