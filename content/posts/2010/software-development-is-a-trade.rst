software development is a trade
###############################
:date: 2010-11-27 02:32
:author: admin
:category: Uncategorized
:slug: software-development-is-a-trade
:status: published
:save_as: 2010/11/27/software-development-is-a-trade/index.html
:url: 2010/11/27/software-development-is-a-trade/
:private: true

Earlier tonight I tweeted something snide about "Big Data."  Some people actually replied!  This was a useful reminder that Twitter is not just a black hole into which bile can be thrown.  It also made me realize that I should probably explain my thinking a bit more.

At this point, I consider software development to be a trade.  It's easy to pretend otherwise, what with so many of us having degrees in computer "science" and the fact -- often only apparent to practitioners -- that a program's implementation can reflect an aesthetic sensibility.  But in truth those of us who work in the industry perform tasks that are a lot more like the work of an electrician or plumber than that of a sculptor or theoretical physicist. We apply a relatively small number of solutions to an almost infinite landscape of problems.  There's still plenty of room for variation and artistry in the execution -- there's more than one way to skin a cat -- but it really is about deploying specialized tools to solve applied engineering problems.

Ted Dziuba once wrote something like "scalability is the problem that every software engineer wishes he had, and ten actually do."  There's something to this, but it's a bit unfair to the people who wish they had the problem.   A run-of-the-mill web developer studying scalability is a bit like a construction carpenter studying Amish furniture making techniques.  Is it relevant to his work?  Well, strictly speaking, no.  He just needs to be able to tack up frames so the drywall guys can come by.  Still, if you're choosing which carpenter to hire to help build a townhouse, it might not be a bad idea to pick the guy who's interested in learning about dovetail joints and how to build a dresser without using any nails or screws.  To be clear: this is not where the guy's talents are actually needed.  He could be rebuilding houses in Haiti, or New Orleans, or wherever.  There are plenty of problems that need his skills.  Still, there's nothing wrong with a guy taking pride and interest in his craft.

And that's about where we are with software developers interested in scalability, or Big Data, or whatever.  Interest in esoteric topics is healthy!  It shows that a person is engaged and anxious to learn.  A very few of those people actually will need to build dovetail joints someday.  And yeah, they could probably just learn once the need arises.  But it's not a particularly grievous misallocation of resources for them to learn now instead of later.

But things get a little dodgier once you get beyond this circle of technologist self-betterment.  It is not particularly helpful, for instance, to start writing news stories about how the future of carpentry is the phase-out of screws, and how in the future no firm that hasn't prepared itself and its employees for the screwless economy is going to be able to compete.  It's just not true.  Some smart people are interested in this stuff, but that doesn't mean it's about to transform the industry.

So, look: Big Data.  Do some people genuinely deal with this class of problem?  Yes, some do.  Many more, myself included, wish they did: I get as excited as anybody else by the idea of marshaling huge quantities of information to reach interesting conclusions!  The problem here is really just the "big" part.  Computers are *so* powerful.  How big does a problem need to be before a single machine is an impractical solution?  The answer is: very, very, VERY big.  For instance, I've got the last ten years of federal spending data on the laptop on which I'm typing this.  That's about 31 million rows of data.  That's a lot!  But it's still nowhere near the point where I'd need to pursue exotic optimizations for my queries.  Most startups do not do as much business as the federal government; and most well-designed systems don't need to constantly query a huge working set of data.  I can't help but wonder whether we'd be better off spending more time teaching each other how to run regressions, or just calculate a confidence interval (how big do you need that data to be before you can arrive at a decent answer, anyway?).

But this is just my own sense of the matter.  The fact is that I don't do a ton of work in this area.  Perhaps I'm way off-base here!  But I kind of get the sense that engineers are getting excited about interesting things, and others are concluding that those interesting things are *broadly important* things.  It's not always so.
