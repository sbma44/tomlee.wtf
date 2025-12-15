back!
#####
:date: 2006-12-31 14:07
:author: admin
:category: tech
:slug: back
:status: published
:save_as: 2006/12/31/back/index.html
:url: 2006/12/31/back/

Hi everybody. Well, the New Year's party is only a few hours away, and vacation is winding down. Going into this time off I had grand, bloggy plans, nearly all of which went completely ignored and unfulfilled. Among my intended projects:

- Fixing my `full-text RSS thingamajig </2006/12/19/do-me-a-favor/>`__. I ended up not touching a line of code. I'll get to it eventually.
- Building an extension cord that could toggle itself on and off based on input from my Arduino (the original plan was to have some Christmas lights blink a yule-appropriate message in Morse Code). I put some time into this one, but although I managed not to electrocute myself or blow any circuit breakers (to my astonishment/disappointment), I appear not to understand how transistors work very well. The relay assembly seems to work pretty well, and the Morse Code program blinks the Arduino's pin 13 LED reliably, but the transistor doesn't seem to do anything despite the input to its base. Anyone who's even slightly competent at electronics is hereby begged to have a quick look at the following diagram. I know I'm missing a protection diode across the relay coil, but I kind of doubt that's the source of the problem. Maybe, though! I'm just piecing this stuff together from the internet and `this book <http://www.amazon.com/Practical-Electronics-Inventors-Paul-Scherz/dp/0070580782/sr=8-2/qid=1167601484/ref=pd_bbs_2/105-1151806-0209230?ie=UTF8&s=books>`__, and consequently I'm probably making some obvious mistakes.
  |circuit diagram|
  **UPDATE:** Thanks to `anachrocomputer <http://www.flickr.com/photos/11328208@N00/>`__, who figured out the problem for me in the `comments <http://www.flickr.com/photos/44137303@N00/340044058>`__ on the photo. I'd accidentally made an `emitter follower <http://en.wikipedia.org/wiki/Emitter_follower>`__ (aka common collector) circuit, which resulted in the transistor only allowing through as much voltage as was applied to its base — in this case, the Arduino's ~5 volts. The result was that the relay (which requires 12V) wouldn't fire. Whoops!
- My Javascript-powered automatic illustration doohickey: untouched!
- My Tetris project: well, finished before leaving work, actually. But the demonstration video: unproduced!
- And I'm pretty sure I've forgotten about a couple of other things I meant to do. Oh well. They probably weren't that great, anyway.

I did accomplish `one <http://www.movering.com/node/303>`__ or `two <http://www.dcist.com/archives/photos/>`__ small things, but mostly I just sat around, played with the Wii and worked to `liberate Aether from the dreaded Ing <http://www.metroid.com/prime2/main.htm>`__ (and `hanging out with internet weirdos <http://www.unfogged.com/archives/week_2006_12_24.html#006015>`__, of course). It's been a pretty unproductive break. But after a year without a real vacation, I think that's exactly what I needed.

.. |circuit diagram| image:: http://farm1.static.flickr.com/156/340044058_60fb84fa16.jpg
   :class: center
   :target: http://www.flickr.com/photos/44137303@N00/340044058
