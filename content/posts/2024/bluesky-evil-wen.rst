bluesky evil wen?
#################
:date: 2024-12-04 14:18
:author: admin
:category: Uncategorized
:slug: bluesky-evil-wen
:status: published
:save_as: 2024/12/04/bluesky-evil-wen/index.html
:url: 2024/12/04/bluesky-evil-wen/

One of the reasons I've been slow to leave Twitter is my default skepticism about new services. I enjoy my ruts: I didn't want to leave ICQ, or AIM, or blogs, or the Instagram photo feed. I linger around these digital ghost towns even as my friends move on to more vibrant locales. That those friends sometimes abandon their new homes, years later, in disgust, is cold comfort. I should have followed them, enjoyed their company while I could, suppressed my misgivings about our new digital landlords. Instead, too often, I indulge my aversion to change and watch my RSS software's "unread" count tick upward ever more slowly.

Well, now my friends are moving to Bluesky, having finally reached apparent consensus on it rather than the unpleasantness of Mastodon or the temptation(?) to hand yet more cultural power to Mark Zuckerberg, for some unfathomable reason. `I am following them <https://bsky.app/profile/tjl.bsky.social>`__! But I am bringing my opinions with me, to everyone's great sorrow. I can't help it. Bluesky is the best option, I agree, it's hard to deny. But I also can't deny my tendency to play Cassandra.

There is a lot to like over there. Forgotten acquaintances. Plausible (temporary) freedom from professional scrutiny. Silliness. A sense that you are in a place that is still manageably small, and which feels comfortingly real in its capacity to delight, or not: there are no perfectly-tuned systems to optimize engagement, no robot arm to shove you back into your cage at the ad impression factory farm. When you put your phone down it's not so far past bedtime, and you've been talking to people you sort of know, and your brain doesn't feel like it's been twisted dry for every drop of arousal and outrage.

It is also a little unbearable. Maybe it was hard to notice Twitter growing tepid, then cold. Stepping into Bluesky's freshly drawn bath is momentarily painful, I'm overcome with prickles. Everyone seems very sure of their opinions despite having just received a crushing repudiation from most of their countrymen. But humility does not drive engagement, not on old sites or new ones, and I'm not confident that my opinions are any better than theirs.

Except about Bluesky itself. Bluesky users are mostly very pleased with themselves for having left Twitter, consistently overestimate the novelty of the features they're enjoying, and are quite certain that Bluesky has a good plan to avoid Twitter's fate. I am at least sort of sorry to tell you: this is naive.

I think Bluesky does have a genuine opportunity to break the wheel of social media history. But good intentions will not be enough.

Let's run through the advocates' arguments.

**Corporate Structure**
-----------------------

Bluesky is a `benefit corporation <https://en.wikipedia.org/wiki/Benefit_corporation>`__--a different and more meaningful designation than `B Corp <https://en.wikipedia.org/wiki/B_Corporation_(certification)>`__. But not *that* meaningful. It comes with some reporting requirements and a mandate to consider social impact when making decisions. The supposed duty of normal corporations to maximize shareholder value is `basically imaginary <https://www.nytimes.com/roomfordebate/2015/04/16/what-are-corporations-obligations-to-shareholders/corporations-dont-have-to-maximize-profits>`__, but it does seem that being a benefit corporation might insulate executives from some classes of legal action brought by shareholders.

But let's get real. Bluesky is not a public company. Barring some truly pyrotechnic malfeasance, shareholder lawsuits will not be a problem any time soon. The company has raised at least $15 million and has given the funder a seat on the board. If a board wants to get rid of an executive, they can find a pretext for doing so without announcing that it was due to insufficient levels of evil or anything else that might invite a lawsuit.

**Jack was bad, Jay is nice**
-----------------------------

I admit: the current board composition is notable and encouraging. Blockchain Capital, the money folks, have a seat. But they also gave one to `Mike Masnick <https://knightcolumbia.org/content/protocols-not-platforms-a-technological-approach-to-free-speech>`__ and the inventor of Jabber/XMPP. Mike is an ideologue (in a good way). And Jay Graber, the CEO, sits on the board, is reportedly the largest shareholder, and seems to say and believe the right things.

But you should expect the board to change. Twitter had at least five major fundraising events prior to its IPO, and these typically come with changes to a board's structure and, inevitably, dilution of its existing participants' influence.

More important, though, is to note the obvious fact that having good people running a company is no guarantee of its future path. I knew a couple of early Twitter employees. They were and are very nice, thoughtful folks. The tech press has taught us to detest him since, but once upon a time `Jack Dorsey was the subject of fawning profiles in places like The New Yorker <https://www.newyorker.com/magazine/2013/10/21/two-hit-wonder>`__. Media coverage of these figures is the only way most of us know them, and it turns them into heroes or monsters because those are compelling narratives. But the truth is that they're mostly just normal human beings who have borrowed millions of dollars.

You should remain open to the possibility that one day those normal people will need more money to sustain the enterprise they've fought hard to build, to preserve their friends' and subordinates' jobs, to pay for their kids' schools, to keep doing the good they believe themselves to be doing in the world. To manage this they will have to disappoint some of the strangers to whom they've been providing free stuff. But wouldn't those strangers be more disappointed if the whole enterprise just collapsed? Because that will be the alternative, as they see it. And what do they owe those strangers, anyway? The board members they've been working to charm for the last few years turned out to be perfectly nice people, but they have understandable obligations to their bosses and the people who subscribed to their fund. We never said we were running a charity!

**ATProto**
-----------

When I raise this concern, people often point to the open foundation upon which Bluesky is built, and I agree that this is an important consideration. But I think very few people have bothered to read `the ATProto spec <https://atproto.com/>`__ and learn what it does--and, more importantly, what it does not do.

ATProto defines an approach to creating an interoperable streaming ecosystem of independent data stores, specifying how they should talk to each other, name things without coordination, authenticate participants, and perform related tasks.

ATProto is mostly agnostic about what data you put into it. Like an empty hard drive, it has complex systems of interfaces and protocols to define how it will store data. But the structures that give the data *meaning* exist elsewhere. Bluesky is one of them, defined by the *app.bsky* namespace/lexicon for things like feeds and posts, and by client applications to manifest those things in forms humans can use. `Bluesky is open source <https://github.com/bluesky-social/social-app?tab=readme-ov-file#are-you-a-developer-interested-in-building-on-atproto>`__, and you can run your own copy. But Bluesky is in charge of the codebase and--most importantly--is in charge of *their* copy.

Listen to how they talk about it:

   Bluesky is an open social network built on the AT Protocol, a flexible technology that will never lock developers out of the ecosystems that they help build. With atproto, third-party integration can be as seamless as first-party through custom feeds, federated services, clients, and more.

   \ https://github.com/bluesky-social/social-app?tab=readme-ov-file#are-you-a-developer-interested-in-building-on-atproto\ 

ATProto will always be available to everyone. ATProto will never lock you out of what you build with it. You can put whatever you want into ATProto.

But ATProto makes no promise that Bluesky-the-app will accept what you want to put into it. Why would it? Nor are there guarantees that everything Bluesky-the-app does will always be put into ATProto for your delectation. It would be shocking to me if there weren't already caching layers, logging systems, and metrics tools on Bluesky's servers that exist beyond open public scrutiny. It's simply how you build a service for millions of users.

`Twitter aspired to be, and initially was, quite open <https://cybercultural.com/p/twitter-in-2007-the-open-platform/>`__. This was a manifestation of the beliefs and values of the smart, stylish technical people who worked there. At the time, APIs and third party integrations were very much in vogue among developers. We got excited about them. They weren't just badly-documented, locked-down plumbing like they are today. They were a dramatically novel way to integrate your work with the coalescing digital world. Even better, OAuth didn't yet exist.

Here's a sad truth: people spend money on things they need from you, which means things they can't get more easily elsewhere, which means things that are scarce. If you build an amazing, complex project in the open, and then start making money by charging people to use some part of it, it is very likely that other people will eventually notice and realize they can do the same thing using your work. And since you still have to invest in the work's continued development and maintenance, those new competitors can undercut you on price! Even more amazingly, if you express frustration about this, internet norms dictate that *you* are the bad guy (you should have known better before you started).

Here's another one: users may enjoy focusing on the minutiae of blocking and discovery tools, but what makes a social network truly valuable is *scale*. They call them network effects for a reason! To be the best, you need to be the biggest. To be the biggest, you need to be free. To be free, you will probably need to make your money with ads.

I know that Bluesky has announced plans to offer subscription features. I don't think this will work: there's always a tension between gating value and keeping barriers to entry low. Elon's selling an insane subscriber bundle, doing completely unethical things (priority for bluecheck reply-guys) and very expensive things (hour-long video uploads, access to a novel LLM model), and it doesn't seem like it's working. Lots of internet companies have experimented with subscriptions, or digital goods, or whatever else. They either become niche players or wind up back at ads, with all the associated privacy tensions, incentives for engagement-maxxing, and unquenchable thirst for scale.

ATProto doesn't include anything about advertising or even making money in general. Financial support for your implementation seems to be left as an exercise for the reader. But this is a very important detail. It's a shame that a project motivated by Twitter's failures didn't put sustainability and the pitfalls of the venture model front and center.

I think Bluesky should probably try to fundraise, like Wikipedia, even though they're not a nonprofit. I think they should change their terms to lock down a monopoly on monetized search. I think they should mandate support for ad inventory among third party clients.

Above all, they need to keep headcount down: minimize the number of mouths they have to feed. This will almost certainly mean some unpopular tradeoffs around moderation.

**Reasons for optimism**
------------------------

(**and precedents no one wants to talk about**)

Despite all this, I am not pessimistic. I am making this argument not to convince you that Bluesky is doomed to be bad, but to convince you to embrace the urgent and fragile possibility that it could remain good--but that this is far from guaranteed.

They have the wind at their back. The users are here. There's money in the bank. The board and CEO are aligned. The press is glowing. *This is the time to bind your future self*. Only real constraints, applied soon--ones so deeply structural that untangling them would be ruinous--can foreclose distasteful decisions against a set of future choices that, we must assume, will some day arrive.

Other people have done this. No one wants to hear it, but the web3/dApp blockchain people have thought about it a *lot*. I may be the only person who believes it, but fact that Jay and Bluesky's funders have connections to the crypto world could be a pretty good sign. Nostr, too, has tackled the issues that ATProto is designed for, and actually has multiple cooperating relays live today. But it's threadbare, it's associated with Jack, and the vibes are bad. Mastodon has a genuine federated ecosystem, but it's built and policed by people who learned social graces from Linus Torvalds, and its search will never work (on purpose, supposedly).

Bluesky's got the functionality, it's got the vibes, it's getting the users. It's got the opportunity.

Fifteen years ago, people thought Twitter was not just good, but figuratively and literally revolutionary. Hard to believe, I know, but it's true. `It made me uneasy <https://prospect.org/article/cost-hashtag-revolution/>`__, and I'm sorry to say that I was eventually proven right.

I don't think things had to turn out the way they did. They don't have to turn out that way for Bluesky, either. But they easily could, and if you don't believe that, you're fooling yourself.
