unfoggedbot!
############
:date: 2007-07-12 23:08
:author: admin
:category: tech
:slug: unfoggedbot
:status: published
:save_as: 2007/07/12/unfoggedbot/index.html
:url: 2007/07/12/unfoggedbot/

Tech project the second! I aspire to participate in the comment threads over at `Unfogged <http://www.unfogged.com>`__. There's really no better place on the internet for listening to people with PhDs talk about such weighty topics as `fat celebrity paramours <http://www.unfogged.com/archives/week_2007_07_08.html#007138>`__ and `bizarre Japanese pornography <http://www.unfogged.com/archives/week_2007_07_08.html#007148>`__.

But it's tough. The comments come in quick bursts. The only real way to participate in a thread is to keep it open in a browser window, manually refreshing every few seconds. Unless I'm stuck on a bus, I get bored when a slow spell hits. I move to a different web page or task. I come back and thirty messages have gone by, and the conversation has moved past a point where I would've liked to participate. Crap. There's comment RSS, but the interval at which RSS readers update is much too slow for it to be very useful.

What I need is push technology — something that does the checking for me, only bothers me when there's new content, and does so *fast*. So hey, I built something. It's a pretty simple IM bot hooked up to a script that checks the comment RSS a few times a minute (hopefully this is okay by the Unfoggitburo — I figure one script that resyndicates content could ultimately serve to *reduce* load).

Based on my not-very-rigorous testing, it seems to work fairly well. If you're interested, give it a shot and let me know what you think, and any improvements that you'd like to see.

#. Add "Unfogged" to your AIM buddy list. Having the bot as a buddy loosens some of the rate limits that might otherwise prevent it from sending messages.
#. Send the bot a message containing the URL for a particular Unfogged thread. You can use either the entry's permalink or the comment thread's link. You should get back an IM saying you're subscribed to the thread.
#. From this point on you'll get an IM whenever someone posts to the thread. To toggle your subscription off, send the URL again. You should get another message confirming that you've been unsubscribed.

Disclaimers! The script is pretty rough:

- it doesn't daemonize
- the Net::OSCAR package apparently can't deal with rate limits, so if it hits one who knows what'll happen
- if it crashes it won't relaunch, and it's running off a somewhat flaky server in my living room
- it won't send IMs faster than once every three seconds in order to avoid rate limits, so it may get backed up during peak periods
- and of course, it could always go crazy and start sending you floods of IMs (if that happens, I suggest just blocking the AIM user — send me an email or comment, while you're at it)

But at the moment it seems okay! If folks find it useful I'll polish it up, post the code and find it a better home.

**UPDATE:** Already found a bug! If the RSS parser finds an empty feed (which can occur if it queries it at the same moment as the feed's being rebuilt by MT), it craps out. I think I fixed the script, but I could be wrong. I'll have to have a closer look in the morning. I can confidently say I restarted it, which should let it work for a while, at least.
