smysteries revealed
###################
:date: 2007-02-07 12:29
:author: admin
:category: tech
:slug: smysteries-revealed
:status: published
:save_as: 2007/02/07/smysteries-revealed/index.html
:url: 2007/02/07/smysteries-revealed/
:private: true

Somebody emailed me for help setting up an SMS service, and I ended up spewing out enough words that I thought I might as well commit them to the web. If you want to do something cool and techy with SMS, here are the options that I know of:

- You could buy a shortcode and SMS service from a vendor like `Clickatel <http://www.clickatel.com/>`__, then interface with their API. That'd run you around $1000 a month, plus $2k to get it set up (and usage fees). It's how the pros do it, but I imagine it's overkill for your purposes. Let's move on.
- You could make a setup like `LastCall <http://www.dcist.com/archives/2006/05/09/introducing_las.php>`__, which uses an open source project called Gammu, a cracked-screen Nokia from ebay, an unlimited SMS plan from T-Mobile and a surprisingly hard-to-get-working phone » serial cable (it took me months to find one that would work under Linux). A bunch of perl scripts (and a little Python) powers it all. I wanted to do this for various reasons, but it ended up taking me months and was a huge pain in the ass. If your application is going to be simpler, I would advise against it.
- You could use the `MOZES <http://www.mozes.com>`__ service. This is a shared shortcode that provides an API (which is somewhat poorly-documented, as of the last time I checked). You pick a keyword and can use it for a certain number of messages. When you text the keyword followed by a command to the shortcode MOZES it can integrate with your MOZES account in various ways — one of them is to trigger scripts that you've written and which use the MOZES API. This is probably the most accessible way to start using real SMS service. You could probably do something similar with `Twitter <http://www.twitter.com>`__, too (and without the account running out of messages), but that's not what Twitter is designed for and they might shut you down.
- Finally, you could simply rely on the carriers' SMS-to-email gateways, which work pretty well. This is what `traincheck.com <http://www.traincheck.com>`__ does. It's easy to get a cheap webhost, hook it up to a domain, then create an email address that forwards incoming mail to a PHP, Perl or Python (or whatever else) script (PHP tends to generate bounce messages unless you vigorously suppress every line's output — I'd suggest one of the other two, if they're all the same to you). The only downside here is that the wireless carriers will eventually shut you down if your service becomes heavily-used. But if you just want to automate some part of your and/or your friends' lives with SMS, then this is simple, easy, cheap and works on nearly all phones.
