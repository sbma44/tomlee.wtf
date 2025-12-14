everything is connected
#######################
:date: 2007-11-23 13:26
:author: admin
:category: music, tech
:slug: everything-is-connected
:status: published
:save_as: 2007/11/23/everything-is-connected/index.html
:url: 2007/11/23/everything-is-connected/

#. `As noted on their blog <http://noref.biz/?r=http%3A%2F%2Fblog.hypem.com%2F%3Fp%3D108>`__, some guy (not me; I wish I'd thought of it, although I wouldn't have published the MP3 URLs publicly) has written a script that pulls RSS from the HM, adds Last.fm popular tags to songs, and posts the MP3s' URLs to del.icio.us. The `result <http://del.icio.us/taggedhype/indie_rock>`__ is a huge, well-categorized stream of MP3s that represents most of the music blogosphere.
#. As you probably know, it's easy to filter a del.icio.us user's entries by tag — for instance, `here <http://del.icio.us/taggedhype/indie_rock>`__ are the HM entries tagged "indie_rock" (I should point out that the tags get considerably more granular than this example). Thanks to del.icio.us's cool `PlayTagger <http://del.icio.us/help/playtagger>`__ Flash audio player, this is already pretty useful. But it gets better.
#. It's also very easy to get an RSS feed of `all <http://del.icio.us/rss/taggedhype>`__ or `part <http://del.icio.us/rss/taggedhype/indie_rock>`__ of a del.icio.us user's entries.
#. It's only slightly harder to use Yahoo Pipes to turn an RSS feed of links to MP3s into an iTunes-compatible podcast feed. `Here's a pipe <http://pipes.yahoo.com/pipes/pipe.info?_id=_jSmNvCZ3BGZCNZWYEsBXw>`__ that lets you do exactly that to any given feed of MP3s.
#. Add this up and you get an ipod-ready podcast version of the HM. This is a feature that the site used to offer but no longer does (I could never get it working, anyway, although I think this was probably due to PC iTunes' suckiness at the time).

Incidentally, they also have a new flash MP3 player over there, which is very nicely done. It's based on `this guy's <http://www.jeroenwijering.com/?item=jw_mp3_player>`__ MP3 player — I've used his Flash video player on a project at work and can attest to its awesomeness (javascript bindings!). It's free for personal use, too, and cheap for commercial applications.

**UPDATE:** I should add that if you decide to try this out you should absolutely not set iTunes to update more often than once a day, as you'll be getting too much music to listen to and burning through HM's bandwidth for no good reason. Also, I should warn that the HM folks will probably shut this approach down shortly by disallowing iTunes' HTTP user agent string. I wish they'd just run the feed themselves, sticking advertising in the podcast entries to pay for the bandwidth. But it's probably pretty complicated to sell that particular kind of ad unit, so I'm not holding my breath waiting for it to happen.

Incidentally, this is yet another app that makes me wish Amazon's S3 storage service was free. That's a bit unrealistic, of course. But I'm increasingly convinced that we need an open P2P storage system. Something like `this <http://wua.la/en/what.html>`__ or an easier-to-use (and less porn-riddled) Freenet, but with a simple API. Ideally it'd be baked into some hugely-popular Firefox extension in order to garner sufficient levels of adoption.

**UPDATE 2:** At a cursory glance `Oceanstore <http://oceanstore.cs.berkeley.edu/>`__ looks about right, although it seems as though it hasn't been worked on for a couple of years.
