er, sorry about that
####################
:date: 2007-12-03 14:54
:author: admin
:category: tech
:slug: er-sorry-about-that
:status: published
:save_as: 2007/12/03/er-sorry-about-that/index.html
:url: 2007/12/03/er-sorry-about-that/

To all you kind, lovely people who follow user "DCist" on Twitter, helping me debug a project or just expressing an interest: I apologize. I've been working on a Ruby reincarnation of my `LastCall <http://dcist.com/2006/05/09/introducing_las.php>`__ service.

As part of that I've been using the `jabber-bot <http://socket7.net/software/jabber-bot>`__ Ruby Gem, which does most of the grunt work of setting up an IM bot. You define the patterns it recognizes, then it hands those off to your script. If it doesn't recognize an incoming IM, it helpfully responds with a message saying "I'm sorry but I don't recognize '<your message here>'. Type 'help' to get a list of the commands I do recognize."

The second contributing factor is Twitter's habit of sending a message saying "Whoops! Your message was too long. You can only send 140 characters at a time." if you send overly long tweets.

The third was that `Alex <http://www.al3x.net>`__, in an attempt to make my debugging effort easier, was nice enough to whitelist the bot so that it's not subject to any of Twitter's abuse-prevention routines. See where this is going?

The bot was only up for about ten seconds, but in that time it sent an overly long message to Twitter, which responded with a message about how it couldn't send a message that long, to which the bot responded that it didn't understand a message of the format "your message is too long". But of course that was also too long. And that's when your cell phone went crazy.

So! Needless to say, I'll be a little more careful going forward. Please don't stop following DCist (I need you there for testing!), but please do turn off SMS updates from it until the app launches.
