hacking your Canon point & shoot
################################
:date: 2008-05-07 13:22
:author: admin
:category: tech
:slug: hacking-your-canon-point-shoot
:status: published
:save_as: 2008/05/07/hacking-your-canon-point-shoot/index.html
:url: 2008/05/07/hacking-your-canon-point-shoot/
:private: true

Slashdot `posted <http://hardware.slashdot.org/hardware/08/05/06/2032216.shtml>`__ something yesterday; today I gave it a try. Apparently the `CHDK project <http://chdk.wikia.com/wiki/CHDK>`__ allows you to supplement your Canon camera's firmware. The modified software allows you to override the rather constrained exposure times and ISO settings, and do other fun things like shoot in RAW, trigger exposures via USB, record longer movies and even set the camera up to take pictures whenever it detects motion. There are also a few less useful applications thrown in:

|playing reversi, compliments of CHDK|

Reversi! Neat.

Installation is pretty painless: after figuring out your camera's firmware revision, you download and copy two files to the root directory of your SD card. Then boot into picture-viewing mode and go to the "update firmware" menu option. Despite what this sounds like, it's all reversible: by default you'll have to repeat the operation every time you turn the camera on. And even if you set it to automatically boot, you can always revert to the stock firmware by deleting the files from the memory card.

My geriatric SD400 is juuuust below the cutoff for official distributions, but a little searching turned up a `beta release <http://chdk.wikia.com/wiki/SD400>`__ that seems to work fine. If your camera isn't listed as being supported, use the wiki's search function.

I'm afraid that my camera hasn't got enough life left in it to really make good use of this new photographic freedom — the focus hasn't been great ever since some sand got into it at the beach. But knowing that these capabilities exist makes me virtually certain to buy another Canon when I finally decide to replace it.

.. |playing reversi, compliments of CHDK| image:: http://farm4.static.flickr.com/3248/2473392789_48512f6896.jpg
   :class: center
   :width: 500px
   :height: 375px
   :target: http://www.flickr.com/photos/sbma44/2473392789/
