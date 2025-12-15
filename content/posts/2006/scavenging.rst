scavenging
##########
:date: 2006-11-01 23:49
:author: admin
:category: tech
:slug: scavenging
:status: published
:save_as: 2006/11/01/scavenging/index.html
:url: 2006/11/01/scavenging/
:private: true

| Tonight was tapedeck disassembly night:
| |disassembled tape deck|
| I'm trying to decode some metro cards for a DCist post in the vein of the the one where I `pulled apart a SmarTrip card <http://www.dcist.com/archives/2005/12/14/dissecting_the.php>`__. But decoding magstripe data is a little harder than splashing around some acetone and plagiarizing wikipedia's RFID article.
| I started off trying to use `this project <http://stripesnoop.sourceforge.net/>`__ and `this reader <http://stripesnoop.sourceforge.net/hardware/reader.html>`__. And it works great for most of the cards in my wallet — but not for metro cards. Strangely, this problem even occurs in raw mode, where the reader simply spits out ones and zeros. The blocks of digits occur in roughly the same places, but the sizes of these blocks aren't consistent.
| I've done some googling. From what I can tell, it looks like most financial institutions use a standard encoding scheme, complete with checksums and well-known formats. The stripesnoop reader and software expect this scheme, but DC metro cards don't abide by it. In fact, they may not even be digital: apparently some older card systems are acoustic, using various overlapping frequencies to encode data (the same way that telephone touchtones do).
| Anyway, I'm hopeful that `this software <http://www.sephail.net/articles/magstripe/>`__ will be up to the task of analyzing it. It's a little more bare-bones: you hook a magnetic read head up to your sound card, record the sound of the magstripe and the software analyzes the resulting wav file. This is why I made that request for breakable tape decks — big thanks to `Ray <http://wryandstanley.blogspot.com/>`__ for providing a suitable victim (and to `Matt <http://ficke.blogspot.com>`__ and `Jeff <http://www.jeffnye.org>`__ for similar offers).
| At the very least I've managed to get a motor out of it and a useful-looking transformer that will probably prove to be even more dangerous than I suspect. But I'd say that odds of successfully decoding a card are low. If I can just produce some weird-sounding mp3s I'll call this project a resounding success.

.. |disassembled tape deck| image:: http://static.flickr.com/100/286498673_aadee74d70.jpg
   :width: 500px
   :height: 375px
   :target: http://www.flickr.com/photos/sbma44/286498673/
