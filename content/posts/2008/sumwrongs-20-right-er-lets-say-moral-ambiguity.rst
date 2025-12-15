((sum(wrongs) % 2)==0) ? right : er, let's say moral ambiguity
##############################################################
:date: 2008-08-06 16:56
:author: admin
:category: DC, personal
:slug: sumwrongs-20-right-er-lets-say-moral-ambiguity
:status: published
:save_as: 2008/08/06/sumwrongs-20-right-er-lets-say-moral-ambiguity/index.html
:url: 2008/08/06/sumwrongs-20-right-er-lets-say-moral-ambiguity/

It's that time of year again: the FishbowlDC Hottest Media Types contest is upon us. And frankly, I'm a bit disappointed: due to last year's... `irregularities <http://machinist.salon.com/feature/2007/08/22/fishbowl_bots/>`__, Patrick Gavin promised new and improved technology. And I was ready! I checked `Crowbar <http://simile.mit.edu/wiki/Crowbar>`__ out of SVN and into a virtualized environment; I created a custom screen-scraper script for it, and got it working with XulRunner in such a way that it could be called by Ruby. I started looking into firing up a farm of Amazon EC2 instances to run the operation in parallel. I hit a snag when trying to find a decent RDF parsing gem for examining Crowbar's output, but then the poll went up and I saw it didn't matter.

It's the same goddamn PollDaddy crap as last year! And it's still just as vulnerable to a looped one-liner shell script. Fire up Firebug to grab the AJAX call's URL, then set curl to keep loading it. You don't even need to fake your user agent.

Ah well. We can still have some fun with this. Thanks to `this <http://arantius.com/misc/greasemonkey/script-compiler>`__ handy GreaseMonkey script compiler I've put together a little Firefox extension that should help this year's voting arrive at the appropriate result: namely, one that puts Mr. Brian Beutler at the top.

For those who question the propriety of this enterprise or (gasp) Brian's hotness — well, there's probably no hope for you. But look, maybe an analogy will help: Fifty Cent got shot a bunch and it made people start acting like he can rap. Now he's a millionaire with access to unlimited supplies of Vitamin Water. A public acknowledgment of Brian's post-shooting beauty is a pittance in comparison. It's the very least we can do.

And it should be really easy, too. All you have to do is click the link below, say OK to whatever security warnings come up, and install the extension. I think it'll work in Firefox 2 and 3; I've only tested it in the latter, though. After it's installed and you've restarted Firefox, navigate over to the `appropriate page <http://www.mediabistro.com/fishbowlDC/hottest_media_types/hottest_media_types_get_voting_male_off_air_90977.asp>`__. A message should pop up, then the robovoting will begin. You'll get feedback, too, and the total number of votes you've cast (and your associated rank) will be displayed as it proceeds (it should remember the total even if you stop and restart the process).

And if you *really* want to demonstrate your love for Brian, you can leave proof of your vote total here in comments by pasting the tiny hexadecimal garbage displayed under it (along with the vote total you're claiming) — each total has a unique code. No cheating!

`Install the Beutlerator </static/2008/08/06/beutlerator.xpi>`__
