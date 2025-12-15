more make-believe
#################
:date: 2012-11-04 11:36
:author: admin
:category: personal, tech, Uncategorized
:slug: more-make-believe
:status: published
:save_as: 2012/11/04/more-make-believe/index.html
:url: 2012/11/04/more-make-believe/
:private: true

Notwithstanding last night's late-breaking pumpkin seed roasting and the Obama jack o'lantern rotting in my front yard (thanks, neighbor), it's probably time to let go of Halloween 2012. But it was a good year, marked, in some subtle ways, by more and more friends indicating that their crazed devotion to the holiday is just as deep as my own. I find this immensely encouraging.

The only down notes: the continued lack of a Fickeween-competitive party venue (although: tremendous thanks to Megan, Peter, Kate and Brant for leaping into the breach so ably; I just miss running my own party); and the unavoidable aging and en-lamening that makes it less and less likely that we'll find one while it still matters. There was also the hurricane's cancellation of Sunlight's Halloween Open House (which is a good time, though I am a little saddened, even if only by the symbolism, to have been forced to reprogram my decorations and general spooky zeal away from a big huge mess of a dance party and toward a professional event).

But nevermind all that. As with last year, I redirected my enthusiasm toward my costume, and it all turned out pretty well.  Dave got the best shot of it (apologies to him and everyone else whose Instagrams I'm about to rip off):

|my Mr. Freeze costume|

Here's a pretty good (almost) full-body shot:

|Mr. Freeze|

I'm proud of the engineering behind this one, so excuse me while I indulge myself with a walk-through.  First, the easy stuff:

|purple nitrile gloves + duct tape cuff|

I veered further off-model than `last year </2011/10/30/this-years-model/>`__. In part this was out of simple necessity: Mr. Freeze has gone through a bunch of different character designs; and the realities of fitting a dome over a human head (especially my outsize noggin) require different spacing for things than in the cartoons. But it also reflected preference: I don't actually like the `gray torso in the animated series original <http://villains.wikia.com/wiki/File:Mr.Freeze_BTAS.jpg>`__ all that much, and didn't feel like trying to implement a design as focused on conveying a sense of boxy roboticism.

But the gloves are a legitimately nice touch from the original design. Victor Fries is a scientist; scientists wear `purple nitrile gloves <http://www.amazon.com/Kimberly-NITRILE-NITRILE-XTRA-Examination-Kimberly-Clark/dp/B001GXCWZ6/ref=sr_1_3?ie=UTF8&qid=1352039202&sr=8-3&keywords=nitrile>`__. Easy!

The cuffs are made from some cheap jersey sheets I bought on Amazon, rolled into cords and covered in colored duct tape. I had a lot of success `last year </2011/10/30/this-years-model/>`__ with colored duct tape, and it proved really easy to work with this year, too -- when something only has to work for one night, it becomes a really fantastically easy and versatile fabrication technique. The whole thing is secured by adhesive velcro, a shift from last year's use of taped-in-place neodymium magnets. Magnet fetishism is fun but not all that practical, it turns out.

|mantle with LED strip|\ The mantle is posterboard (which these days is cheapo, paper-thin garbage! scandalous) and more tape. The cut-off bottom of a `stackable garden cloche <http://www.amazon.com/gp/product/B004U4A9C6/ref=oh_details_o06_s00_i00>`__ adds some structure and stability. Incidentally, I had no idea cloches were a thing until `Fancy Hands <http://fancyhands.com>`__ turned them up in response to a costume-related request I made. Thanks, guys! The top dome, as you might imagine, is an uncut cloche from the same three-pack.

On to the electrics! I'm pretty proud of this. The LEDs are mounted on an adhesive-backed strip that I got off of ebay. These things are absurdly cheap -- `they're sold all the time for about $1/meter <http://www.ebay.com/sch/i.html?_trksid=p5197.m570.l1313&_nkw=led+strip&_sacat=0&_from=R40>`__ -- and are very pleasant to work with. All of the resistors are in place, the adhesive backing makes mounting easy, and you can cut them to various lengths with a pair of scissors. Highly recommended.

I terminated the power leads in a barrel connector, the other end of  which I ran down to a belt I contructed, again, out of colored duct tape and velcro. The buckle ornament was a $2 5K potentiometer from Radioshack (pre-soldering shot `here <http://www.flickr.com/photos/sbma44/8121010724/in/photostream/>`__; `here's <http://www.flickr.com/photos/sbma44/8147952771/in/photostream>`__ the front). It's a circuit simple enough that you might've built it in elementary school, but it did the job nicely. LEDs' perceived brightness level doesn't scale linearly with current, meaning that there was a bit of a brightness cliff right in the middle of the potentiometer dial. This worked out fine, since I mostly just wanted to pulse the display in time to music or to surprise people, not fade it smoothly -- having a quick transition point was desirable for this. If you wanted to do it "right" you'd probably want to move things to a little AVR, setting the brightness with PWM control of the duty cycle rather than simple resistance. Actually, a 555 in astable mode might work very well for this, now that I think about it (though the AVR would allow for some cool automatic effects). But this was basically fine, and dead-simple. And having a costume that involves integrated circuits sounds like a good goal for next year.

The LED strip industry was basically invented to help stupid men make their cars look tacky, so it all runs on 12V. This made a `sealed lead acid battery <http://www.amazon.com/gp/product/B002L9EW48/ref=oh_details_o00_s00_i00>`__ a natural choice:

|sealed lead acid battery, plus duct tape pouches for money, ID, iphone|

Pros: the aforementioned voltage; cheapness; safety and simplicity of charging relative to other chemistries like lithium. The downside: weight. But this thing was only 3 or 4 pounds, and I don't think I used more than a fraction of its charge over the course of the night. A cut-up black nylon backpack let me carry it around fairly comfortably (though getting it mounted on the backpack required some creativity).

Also worth noting: the duct tape pouches for credit cards, ID and my iPhone. I'm rather proud of those last-minute additions. More support for the flexibility of the velcro/duct-tape combo. I had spare coin cell batteries taped in various places, too -- more on that in a second.

My freeze gun was the last, and most half-assed, thing that I tackled. But it was also the most ambitious.

|Freeze gun with bike brake lever actuator, LED system|

That's a bicycle brake lever and cable that a gentleman at `Bicycle Space <http://www.bicyclespacedc.com/>`__ sold me while he replaced my wheel. Pretty cheap! Going to a bike shop was a good idea: I wouldn't have known that I needed little metal collars for the cable housing, for instance, but they threw 'em in for free, plus they provided some valuable installation guidance.

|cable pull system. carabiner is holding safety pin in place.|\ The inside of the gun is PVC, which was probably overkill. But, as I said, this was ambitious, because everything was connected to an actual pressure vessel. In this case, a fire extinguisher. I drilled holes through the two handles, then terminated the cable with a couple of bolts tightened in an appropriate spot. The carabiner is there to hold the safety pin in place. The whole thing was connected to the freeze gun by both the brake cable and a `pressure hose and clamp <http://www.flickr.com/photos/sbma44/8147985058/in/photostream/>`__.

Did it work? Well, sort of. The trigger mechanism worked great! But I didn't appreciate just how little charge is in a conventional fire extinguisher, or how focused its design is on moving yellowy fire retardant powder around. The powder got stuck in the hose (and spread everywhere -- very glad I did this outside), and the pressure was discharged after two quick test bursts. Boo. My dreams of an actual freeze gun: dashed. If I had to do it all over again, I would probably look at a `CO2 extinguisher <http://www.amazon.com/Fire-Extinguisher-Wall-Hook-21111/dp/B002L63BOS>`__, particularly since we have a 25 lb tank at work that I could probably have used to refill it after any test firing. Ah well -- sloppiness on my part.

The final bit was the goggles. These were a big hit:

|the goggles do something!|

They were also pretty simple to make. You can see the construction `here <http://www.flickr.com/photos/sbma44/8147949817/in/photostream>`__. I had bought a bunch of CR2032 cells off Ebay a while ago for my bike lights. Protip:  batteries are one of many electronic-y commodities that are `super-cheap <http://www.ebay.com/sch/i.html?_odkw=cable+valve&_osacat=0&_from=R40&_trksid=p2045573.m570.l1313&_nkw=cr2032&_sacat=0>`__ on ebay; in this case, just 5% of the retail CVS/Radioshack price, if not better.

So I had a bunch of these things hanging around, and a few nice `holders <http://www.ebay.com/itm/10-x-New-Battery-Coin-Button-Cell-Socket-Holder-Case-CR2032-Black-/120837294039?forcev4exp=true&forceRpt=true>`__ (I don't even remember what project that was for). I added a couple of cheapo Radioshack switches and some not-so-cheapo Radioshack red LEDs (the LED Ebay/Radioshack price difference is perhaps the most astounding and offensive). I threaded things through the side ports on a pair of `cut-rate welding goggles <http://www.amazon.com/Hobart-770096-Welding-Oxy-Acetylene-Goggle/dp/B0017Z04SK/ref=sr_1_2?s=hi&ie=UTF8&qid=1352041823&sr=1-2&keywords=welding+goggles>`__ that helpfully came with a set of clear lenses in addition to their impractically dark default lenses. I scuffed the LEDs with sandpaper to make the light diffuse better, and bang: I was done! I didn't even need a resistor -- the battery's internal resistance is enough. Each eye is basically an `LED throwie <http://www.graffitiresearchlab.com/blog/projects/led-throwies/>`__, but with two LEDs instead of one and no magnet. I changed the batteries once during the night, but this was mostly because I'd been running down the originals a lot in the preceding weeks (the goggles were the first thing I built).

Like I said, these were a big hit -- several people said they wanted a pair. If I did it again, I would choose a smaller switch and move to surface mount LEDs (and perhaps more of them) so that the light sources wouldn't be so individually noticeable. The LED strips I used for the mantle/dome might be a good choice, actually, if you could pare down the sides. Better still, you might use `bicolor LEDs <http://www.ebay.com/sch/i.html?_sacat=0&_nkw=bicolor+led+smd&_frs=1>`__ and let people swap between modes. Hmm...

As is probably clear, I get way into this stuff. But this was much less work than it probably looks like. I spent a Saturday afternoon on the last-minute gun bit (which included some overkill LEDs of its own), but the rest of it was done in three evenings' worth of puttering around the apartment while watching Battlestar Galactica.

The biggest revelation, for me, was understanding how much of successful fabrication is about knowing what to source and where. Knowing about the existence of the LED strips made everything much easier; knowing to get them from Ebay instead of an auto shop made it cheap. Same goes for having the batteries and holders lying around, and the right crimping connector tabs for the battery -- something I'd bought years ago for who knows what, and managed to remember I had on hand. Pretty much everything else came from Amazon Prime or the hardware store around the corner.

Basically, I felt like Adam Savage seems to in this video:

I'm much less talented, and have much less impressive tools (just some electronics bric-a-brak; meager compared to a guy who has a band saw on hand). But I can relate to the experience of seeing how a system is going to fit together, and building it with surprising speed thanks to the investments you made in parts (or yourself) in the past. That's a very nice feeling -- one of the best things about engineering, if you ask me, even if it's in service of something as silly as a Halloween costume.

.. |my Mr. Freeze costume| image:: http://farm9.staticflickr.com/8053/8130970953_8101f374d0.jpg
   :class: center
   :width: 500px
   :height: 500px
   :target: http://www.flickr.com/photos/sbma44/8130970953/
.. |Mr. Freeze| image:: http://farm9.staticflickr.com/8473/8130994339_155965b95d.jpg
   :width: 500px
   :height: 500px
   :target: http://www.flickr.com/photos/sbma44/8130994339/
.. |purple nitrile gloves + duct tape cuff| image:: http://farm9.staticflickr.com/8193/8147951015_d346de7c42.jpg
   :class: center
   :width: 500px
   :height: 375px
   :target: http://www.flickr.com/photos/sbma44/8147951015/
.. |mantle with LED strip| image:: http://farm9.staticflickr.com/8047/8147983214_25ce0216aa_n.jpg
   :class: right
   :width: 240px
   :height: 320px
   :target: http://www.flickr.com/photos/sbma44/8147983214/
.. |sealed lead acid battery, plus duct tape pouches for money, ID, iphone| image:: http://farm9.staticflickr.com/8051/8147954189_d0e8b9a9ab.jpg
   :class: center
   :width: 375px
   :height: 500px
   :target: http://www.flickr.com/photos/sbma44/8147954189/
.. |Freeze gun with bike brake lever actuator, LED system| image:: http://farm9.staticflickr.com/8465/8147984442_865944ff87.jpg
   :class: center
   :width: 500px
   :height: 375px
   :target: http://www.flickr.com/photos/sbma44/8147984442/
.. |cable pull system. carabiner is holding safety pin in place.| image:: http://farm9.staticflickr.com/8054/8147986200_7ea9e18702_m.jpg
   :class: right
   :width: 180px
   :height: 240px
   :target: http://www.flickr.com/photos/sbma44/8147986200/
.. |the goggles do something!| image:: http://farm9.staticflickr.com/8188/8131005830_3e81dfa73f.jpg
   :class: center
   :width: 500px
   :height: 500px
   :target: http://www.flickr.com/photos/sbma44/8131005830/
