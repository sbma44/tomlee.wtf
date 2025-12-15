the Washington Post talks to bloggers
#####################################
:date: 2007-01-09 21:32
:author: admin
:category: DC
:slug: the-washington-post-talks-to-bloggers
:status: published
:save_as: 2007/01/09/the-washington-post-talks-to-bloggers/index.html
:url: 2007/01/09/the-washington-post-talks-to-bloggers/
:private: true

I just got back from `the Post's blogger summit thingy <http://www.dcist.com/archives/2007/01/02/washington_post.php>`__. How was it? Well, there wasn't any booze. But it was pretty interesting. The Washington Post has plans for you, little blogger.

Among them:

- They've `already launched <http://adv.washingtonpost.com/blogroll/2006/11/about_blogroll_1.html>`__ and will be continuing to build upon a hyperlocal AdWords competitor that only shows ads when it can beat the AdWords `CPM <http://en.wikipedia.org/wiki/Cost_Per_Mille>`__. The assembled bloggers seemed most interested in this, despite the fact that it'll likely mean a difference of a fraction of a cent per click. Nobody who was in that room is going to become rich off of this (although you'd never know it from the volume and pugnacity of the questions that it prompted). But it's interesting from the Post's perspective: it's a forward-thinking way of reclaiming ground from Craigslist. That's pretty smart.
- More interestingly, they plan to launch a directory of DC blogs. Of course, `we've already got a good one <http://dcblogs.com/>`__. But the Post seems certain to become the canonical index. It'll be good to have this stuff in one high-profile place, and even better to have it exposed to the Post's massive readership. On the whole, it seems certain to be a win for the DC blogosphere.

But there are some downsides:

- They intend to rip off the already-much-ripped-off DCist Flickr pool idea. C'est la vie. But credit where due: I believe it was `Rob <http://www.goodspeedupdate.com/>`__'s idea originally, and it was a great one. But they may get more than they're bargaining for: they're a family newspaper — I suspect spam and griefers will be a problem for something as high profile as this. I got the distinct impression that they don't have a full-time staffer available to run this thing.
- They didn't seem very receptive to the idea of providing an API. I think that's a shame — directories of this kind ought to be open and accessible. I suppose I'll write some Perl to turn it into an OPML file every day and serve it up somewhere. Still, it would be nice if they embraced the spirit of openness. They'll be offering some RSS feeds, but I don't think that's enough.
- Similarly, despite their goal of by-neighborhood categorization, they seemed nervous about precisely geocoding the participating blogs. `Nikolas Schiller <http://nikolasrschiller.com/>`__ kept pushing for it, and I joined him, but they claimed to be worried about the privacy implications — and eventually turned the word "geocoding" into a running joke, as if they didn't know what it meant. Now, I do think that Nikolas is a bit map-happy, but he's absolutely right about this. There are pretty simple ways to collect and use precise data without exposing it to dangerous weirdos.

But I'm sure that privacy is only part of their concern. Finding someone to write the API and geocoding stuff is probably the bigger stumbling block. They seem like they're building a pretty basic Yahoo-style directory (right down to trying to settle on a fixed taxonomy for participating bloggers to use), and I imagine they don't want to complicate anything. But the API could consist of a handful of simple REST calls, and geocoding is just a Google Maps mashup away (it's a lot easier than it looks). The front page will just be a little fun, flashy stuff thrown on top of their crawled RSS database.

As for their motivation, I think it must primarily be out of the goodness of their hearts — and wanting to be the center of the DC blogosphere. Other than attracting participants to their ad program, I don't see how they're going to monetize it. So call it a good thing for the blogs of DC — but not as good a thing as it could be.

Oh! They're also going to begin geocoding their `RSS feeds <http://www.washingtonpost.com/wp-dyn/rss/index.html>`__ soon. That was probably the most exciting thing I heard all night.
