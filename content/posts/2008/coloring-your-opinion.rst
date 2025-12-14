coloring your opinion
#####################
:date: 2008-11-08 14:30
:author: admin
:category: politics, science
:slug: coloring-your-opinion
:status: published
:save_as: 2008/11/08/coloring-your-opinion/index.html
:url: 2008/11/08/coloring-your-opinion/

Well, I guess it's time for that "purple America" map from Robert Vanderbei to start making the rounds again. Yglesias has the 2008 edition `posted over at his site <http://feeds.feedburner.com/~r/matthewyglesias/~3/446509415/the_more_things_change.php>`__. The basic idea here is that for all the talk of red and blue America, the political differences between regions are actually quite small, and we're really a united nation with a vigorous political discourse, tra la la la. Then we join hands and sing.

And, you know, fine. There's an element of truth to this, and it's certainly a nice thought. But also true: visualizing information by using a linear red/blue scale is about the worst way possible to make data legible to the human eye. First: our vision is logarithmic. When a photographer drags out his "50% gray" card for measuring lighting, `it's actually 18% gray <http://photo.net/bboard/q-and-a-fetch-msg?msg_id=000F55>`__. Judging by the triangular key in the corner of Vanderbei's image, he's just taking the percentage of vote totals and translating it flatly to 8 bit color — a 100% Republican district gets an RGB 24-bit value of (255,0,0).

The colors themselves are also a problem. As I'm sure you all remember keenly from `this post I wrote in 2006 <http://www.zunta.org/blog/archives/2006/04/07/graphic_violenc/>`__, perceptual image codecs spend more bits on brightness than on color because the color-sensing cones in your eyes have a much lousier dynamic range than the light-sensing rods. We're worse at distinguishing between levels of color than between levels of brightness. And since the percentage of the vote in any given spot on the map should always sum to 100, with negligible green (third party) contributions, the brightness will be relatively uniform (although admittedly not quite due to the perceptual differences between colors — monitor calibration and colorspace begin to enter the picture at this point, and things get just as hideously complex as you might imagine).

(I'll add, somewhat tentatively, that my recollection from college is that `the green cone is the most sensitive of the three types in your retina <http://www.glenbrook.k12.il.us/gbssci/Phys/Class/light/u12l2b.html>`__, making red/blue coding about the least distinguishable color continuum possible. The situation's complicated by your rods' preferential sensitivity to blue wavelengths, though, and the ratio of work done by rods and cones varies with ambient brightness. So I'll resist the temptation to make strong claims on this score.)

So what does this all mean? Depending on how you look at it, not much. It's not as if Vanderbei has done anything *wrong*. It's just that the choices he made will tend to produce a map that, at a glance, implies homogeneity. If, on the other hand, we pull out the red channel, desaturate the blue channel and maximize the contrast of the resulting image (in effect normalizing the values to the full possible dynamic range), we get something very different-looking — but still perfectly accurate, and still non-logarithmic (with the caveat that it gives third-party votes to the Dems). Click the image for a full-sized, easier-to-see version.

|image1|

Yglesias's point that this isn't a huge change between cycles still stands, of course, but the shifts are considerably easier to see this way (and easier still on that `cool New York Times map <http://yglesias.thinkprogress.org/archives/2008/11/the_mccain_belt.php>`__ that ran on their front page after the election).

It's also easy to see that there really *are* very Republican and very Democratic sections of the country. I don't want to overstate my case — obviously this conclusion can be drawn from the color map, too. Still, using a whole bunch of linearly-defined purple pixels is a clever way to latch onto a media cliche, but not necessarily the best way to visualize information. Things are more black and white than they may seem, and certainly less purple.

.. |image1| image:: http://www.manifestdensity.net/skitch/20081108_vanderbei_small-20081108-142538.jpg
   :class: center
   :target: http://www.manifestdensity.net/skitch/20081108_vanderbei_big-20081108-142429.jpg
