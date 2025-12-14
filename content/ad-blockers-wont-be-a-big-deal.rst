ad blockers won't be a big deal
###############################
:date: 2015-09-18 01:24
:author: admin
:category: misc, tech
:slug: ad-blockers-wont-be-a-big-deal
:status: published
:save_as: 2015/09/18/ad-blockers-wont-be-a-big-deal/index.html
:url: 2015/09/18/ad-blockers-wont-be-a-big-deal/

One of the few downsides to attending a conference in Asia is that when the English-speaking world is waking up and beginning to groggily think serious thoughts, you will have just returned to your hotel from a reception with free beer, which you will have had sort of a lot of. The food here is spicy enough that beer availability is a basic amenity, like electrical outlets or ventilation. Korea is a great country.

Although fundamentally delightful, this dynamic can push your level of Twitter cantankerousness out of global circadian sync. Last night it led me to wade, intemperately, into the Great Media Ad Blocker Freakout of '15.

This morning I woke up and resolved to be a better, more understanding conversational partner. It was easy enough to identify the pieces influencing everyone's thinking via the `Today in Tabs Media Monoculture <http://www.fastcompany.com/3051234/today-in-tabs/today-in-tabs-live-from-carly-fiorinas-feverish-imagination>`__. But these pieces are surprisingly bad!

`Here is The Verge's Nilay Patel <http://www.theverge.com/2015/9/17/9338963/welcome-to-hell-apple-vs-google-vs-facebook-and-the-slow-death-of-the-web>`__ bringing the kind of tech blogger tunnel vision that `can turn a wristwatch into the fulcrum of conscious experience <http://www.theverge.com/a/apple-watch-review>`__. He thinks this minor iOS feature is best understood as a major chapter in the Manichean conflict between tech company nation-states. `Here is The Awl's Casey Johnston <http://www.theawl.com/2015/09/welcome-to-the-block-party>`__ relaxing into the newly-minted blend of evocative GIFs, Marxist analysis and depressive fatalism that has made her employer the web's most prestigious purveyor of media industry commentary. She never mentions pop-up blockers or points out that non-Safari webviews aren't affected. The other pieces just don't make any fucking sense.

Notwithstanding the App Store rankings of the new iOS ad blockers--which are better understood as a measure of download acceleration, not velocity--I doubt that all this handwringing will be justified by the number of ads whose lives are actually cut short. But let's suppose that's wrong.

Ad blockers work by preventing your operating system from speaking to ad networks' domains. Those domains are where the ad network Javascript lives, which gets added to the page and loads the images or video or flash for the ad (among other things).

You could make ad blocking much, *much* harder by serving this Javascript from the same domain as the page content. Ad networks don't want to do this for two reasons.

Their first objection is about control. It's coming from their servers, it's their Javascript, and they get to make the decisions. Handing these Javascript responsibilities to publications would introduce a big support headache and would require the networks to police the code to ensure it isn't modified. Their Javascript is often inexcusably shitty, and modifying it would be a great idea, so publishers might be tempted to do so. Personally, I would be very excited to see this devolution of technical power.

Their second objection is about capability. Something called the same-origin policy means that when you visit *publisher-a.com* the site cannot detect that you have visited *publisher-b.net*. However, if both pages include Javascript from *ad-network.biz*, your path between sites can be observed. This allows your behavior to be tracked, and enables the networks to assign you to *segments* like "auto buyer" or "likely golfer" or "pervert".

You can pull off tracking while serving everything from a constellation of publisher domains, but it's not trivial to do so. Many publishers would need a hosted solution to handle these engineering details, and this is where the Awl's paranoia about a totalitarian Facebook dystopia starts to look a bit plausible.

The hypothesized migration toward a central Facebook-like architecture has a cyclical fat/thin client whiff about it, and I suspect the pendulum will swing back before too many of us are forcibly grafted to Oculus Rifts. But then again I earn my living in a different industry and have the luxury of waiting to form a conclusion.

Still, I'm unconvinced that audience segmentation is actually good for publishers. The goal of segmentation is to target ads efficiently. But efficiency means achieving a result with fewer resources than you otherwise might. In this case, those resources are the very things that pay for all those tickets to XOXO. (I've meandered toward this point `before </2010/12/05/more-efficiency-means-less-profit/>`__.)

Besides which, there's a convincing case to be made that `ad efficiency is meaningless <http://www.bloomberg.com/bw/articles/2014-03-03/advertisings-century-of-flat-line-growth>`__. A roughly constant share of the economy goes to advertising:

| |ADS_gdp_vs_spending|
| |ADS_percent_GDP_b|

Maybe some of the spikes in those graphs came from VCRs or `loudness regulation <https://www.truthinadvertising.org/wp-content/uploads/2011/10/Advertisement-Loudness-Mitigation-Act.pdf>`__ or FTC actions or the `payola scandal <https://en.wikipedia.org/wiki/Payola>`__ or Tivo or pop-up blockers. But I doubt it.

So. Could ad blockers damage or destroy some publishers? Yeah, this seems possible, particularly for niche publications with geeky audiences.

Could ad blockers hasten Facebook's ingestion of the media industry? Sure, maybe. Kind of seems like a long-shot but I know a lot of people are freaking out about this.

Could ad blockers shift spending to TV or print, overwhelming trends toward mobile and away from cable? Kind of implausible, don't you think?

Finally, will ad blockers reduce the size of the ad dollar pool, shrinking the total resources available to content creators? Flatly: no.

**ALSO:** `Matt's post is characteristically excellent <http://www.vox.com/2015/9/18/9351759/ad-blocking-controversy>`__.

.. |ADS_gdp_vs_spending| image:: https://tomlee.wtf/wp-content/uploads/2015/09/ADS_gdp_vs_spending.jpg
   :class: aligncenter size-full wp-image-2966
   :width: 630px
   :height: 550px
.. |ADS_percent_GDP_b| image:: https://tomlee.wtf/wp-content/uploads/2015/09/ADS_percent_GDP_b.jpg
   :class: aligncenter size-full wp-image-2967
   :width: 630px
   :height: 550px
