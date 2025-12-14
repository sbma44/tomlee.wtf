still better full-text RSS
##########################
:date: 2007-04-23 11:25
:author: admin
:category: tech
:slug: still-better-full-text-rss
:status: published
:save_as: 2007/04/23/still-better-full-text-rss/index.html
:url: 2007/04/23/still-better-full-text-rss/

I've taken another crack at my full-text RSS script, polishing it up for a release over at `EchoDitto Labs <http://labs.echoditto.com>`__, and in the process I finally got around to adding a much-needed feature: letting users kill excess HTML with regular expressions. This isn't a feature for the non-geeky, but it only takes a single nerd a few minutes to work out the necessary expressions and share them with the class. The result is cleaner functionality: the algorithm used to leave some feeds with duplicate titles, comments, or other cruft. This allows you to strip them out automatically. As a side effect, your RSS reader stop thinking that old posts are new just because another dope added a comment calling for impeachment hearings.

My intention is for this project to be somewhat disruptive, forcing publishers and advertisers to realize that RSS is a legitimate way for people to read a site and not just a syndicated form of advertising. And the sooner everyone gets this through their head the better: if you publish free content on the internet, you will not be able to control how people will consume it.

But I do recognize that in the short term it's likely to be a pain in the ass for the bloggers I like and whose bosses don't understand how to count or sell RSS impressions. So let's start off by picking on someone who deserves the headache: `here's a full text feed for Michelle Malkin <http://www.metamonkey.net/fulltextrss2/?url=http://michellemalkin.com/index.xml&regex=%2F%3C%21%5C-%5C-%5Cs%2A%3D%7B5%2C%7D.%2A%24%2Fsmi>`__. It uses the new regex functionality to chop off the "digg this post" junk that would otherwise be at the bottom of every entry.

The way to use this new feature is pretty simple: pass URL-encoded regexes as GET parameters named "/regex\\d*/i" (if you're going to use this, that made sense to you). Have at it, fellow geeks. I'll get things rolling and suggest the del.icio.us tag "`fulltextrss <http://del.icio.us/search/?fr=del_icio_us&p=fulltextrss&type=all>`__" for the fruits of your labors.

**UPDATE FOR REGEX AUTHORS:** Looks like PHP's magic quotes and/or URL encoding are screwing up the use of the + character in regexes. D'oh. I'll have to see what I can do to fix that. In the meantime, both \* and {} seem to work. For now just use {1,} as a substitute and you should be okay.
