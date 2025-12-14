lasercut fingerjoint enclosures; pictures & code
################################################
:date: 2013-05-31 11:09
:author: admin
:category: Uncategorized
:slug: lasercut-fingerjoint-enclosures-pictures-code
:status: published
:save_as: 2013/05/31/lasercut-fingerjoint-enclosures-pictures-code/index.html
:url: 2013/05/31/lasercut-fingerjoint-enclosures-pictures-code/

My `last <http://www.flickr.com/photos/sbma44/5748853361/in/photostream/>`__ laser-cut finger-joint project (and the `electronics inside <http://www.flickr.com/photos/sbma44/5726518448/in/photostream/>`__) was meant to be a time machine, an emergency device, a way to bend reality. Also, it was octagonal. These aims proved to be unrealistic. I did pull off the octagonal bit, but even that was a struggle.

Less fraught projects need enclosures, too, though, and I liked the technique. You can do some `super-cool stuff <http://www.flickr.com/photos/sbma44/8002432003/>`__ with lasercut materials. Like 3D printing, it removes craftsmanship as an excuse for failing to instantiate the things you imagine.

But although laser-cut construction allows for much stronger and prettier `materials <http://www.ponoko.com/make-and-sell/materials>`__ than 3D printing, the process of translating from two dimensions to three is trickier than you might think. There are `various considerations <http://blog.ponoko.com/2008/11/03/how-to-create-better-nodes/>`__, from the variance of the width of the source material to the width of the path burned away by the laser ("kerf"). Accounting for these things in vector graphics editing programs can be quite tedious. It's easy to make mistakes.

The `right way <http://capolight.wordpress.com/2011/01/22/drawing-gears-in-sketchup/>`__ to do this would probably be to write a plugin for Inkscape/Illustrator. But I'm more comfortable writing Python, so that's what I did. I wrote up a support class that facilitates the creation of `finger-joints <http://en.wikipedia.org/wiki/Finger_joint>`__, and which handles things like kerf automatically.

The output isn't designed to be ready-to-print. You should plan to import it to a vector editor and do subsequent work. Here, for example, is the output of a simple script I used for my latest project:

|fingerjoint.py output|

And here's the EPS I constructed from it and submitted to `Ponoko <http://ponoko.com>`__:

|fingerjoint.py output edited|

Note the difference in the corners of the larger piece, in particular. Some editing is necessary. But the results are quite nice!

|Lasercut box=great success. Design/code to follow.|

(ignore those laser scorch marks; I haven't pulled the adhesive paper side off yet, but when I do and flip the sides, the outside should be relatively pristine)

`I've published the code <https://github.com/sbma44/fingerjoint>`__, and would love to see it expanded into a more general-purpose toolkit. Apologies for its hackiness/non-pythonicness. I assure you it's much better than the first two drafts. This version does matrix math and everything!

.. |fingerjoint.py output| image:: http://farm4.staticflickr.com/3690/8902584803_cae5f34b72.jpg
   :width: 500px
   :height: 355px
   :target: http://www.flickr.com/photos/sbma44/8902584803/
.. |fingerjoint.py output edited| image:: http://farm8.staticflickr.com/7391/8902584869_c0a202eb74.jpg
   :width: 500px
   :height: 332px
   :target: http://www.flickr.com/photos/sbma44/8902584869/
.. |Lasercut box=great success. Design/code to follow.| image:: http://farm9.staticflickr.com/8540/8893322212_e3e07bac27.jpg
   :width: 500px
   :height: 500px
   :target: http://www.flickr.com/photos/sbma44/8893322212/
