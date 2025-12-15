the operation was a complete success
####################################
:date: 2012-07-07 15:18
:author: admin
:category: Uncategorized
:slug: the-operation-was-a-complete-success
:status: published
:save_as: 2012/07/07/the-operation-was-a-complete-success/index.html
:url: 2012/07/07/the-operation-was-a-complete-success/
:private: true

I've been working on an electronics project for \*forever\*, trying to get past some nasty linux wifi bugs and on to the exciting lasercutting/3D printing/web scraping stuff that actually attracted me to the idea (the hope is to make it a repeatable but customizable gift I can give). But to be honest, my willpower has been fading -- a body can only spend so much time in a given IRC channel, asking the same obscure and tricky questions, hoping someone will deign to answer them correctly.

So I took a break to make something a lot simpler. I don't want to give the whole backstory away -- it's going to be a gift, and the recipients might read this blog -- but the core functionality is as simple as turning a garden hose on and off via remote control. And hey, it worked on the first try!

(I probably won't actually follow through on the motion sensor part -- the audio is just me talking to Kriston, Kaylyn and my neighbor Paul, who was nice enough to lend me the use of his water spigot when I found out mine was cracked)

You can see most of the components below, if this third party Flickr note embedding thing is working. The wiring's all wrong in this photo, and it's missing a 12v regulator to power the remote system and the automotive relay that actually switches the 24v valve. But you can see the most exciting parts.

\ |it might not look like much, but this is one voltage regulator away from being a remote controlled sprinkler system|\ 

The next steps are to arrange all this stuff in an appropriately-decorated Gladware container so that it can resist the elements and hopefully not light itself on fire: things get warm when the system's switched on, but I think that's got to be expected with a system this full of relays, and one that's shedding 12v through a voltage regulator (heatsinked and well within spec, though!). If anyone feels like replicating this project, here's the bill of materials and some approximate prices:

- `24v power supply <http://www.allelectronics.com/make-a-store/item/PS-2410/24VDC-1.25A-SWITCHING-POWER-SUPPLY/1.html>`__ ($16)
- `automotive relay <http://www.allelectronics.com/make-a-store/item/RLY-351/12V-SPDT-30-AMP-AUTOMOTIVE-RELAY/1.html>`__ (all auto electronics are 12v -- $2.50)
- `relay socket <http://www.allelectronics.com/make-a-store/item/SRLY-2/SOCKET-FOR-AUTOMOTIVE-RELAY/1.html>`__ (optional, $2)
- `12v keychain remote control system <http://www.allelectronics.com/make-a-store/item/RC-10/KEYCHAIN-REMOTE-CONTROL-12VDC-6-AMP/1.html>`__ ($19)
- `24v electronic sprinkler valve <http://www.amazon.com/gp/product/B004RUHADO/ref=oh_details_o00_s00_i00>`__ ($17, plus $7 shipping from Amazon)
- `12v voltage regulator <http://www.radioshack.com/product/index.jsp?productId=2062600>`__ ($2, though that's a ripoff)
- `heatsink for voltage regulator <http://www.radioshack.com/product/index.jsp?productId=2102856>`__ ($2, and ...less optional. Don't forget the thermal grease!)

It's a pretty good and easy project -- if anyone's interested in replicating it, leave a comment and I can sketch out a wiring diagram. If you buy the relay socket you wouldn't even need to solder anything: wire nuts would work just fine (I used a couple, in fact). Well, okay, you'll need to figure out how to attach the voltage regulator, and that's probably best done with a soldering iron. You might be able to get away with crimping stuff and then taping it up, though.

.. |it might not look like much, but this is one voltage regulator away from being a remote controlled sprinkler system| image:: http://farm9.staticflickr.com/8022/7482950154_5a2249547c.jpg
   :width: 500px
   :height: 500px
   :target: http://www.flickr.com/photos/sbma44/7482950154/
