be gentle to their servers and mean to their lawyers
####################################################
:date: 2016-04-04 21:49
:author: admin
:category: Uncategorized
:slug: be-gentle-to-servers-and-mean-to-lawyers
:status: published
:save_as: 2016/04/04/be-gentle-to-servers-and-mean-to-lawyers/index.html
:url: 2016/04/04/be-gentle-to-servers-and-mean-to-lawyers/

I didn't like `this article about ethical screen scraping very much <http://www.storybench.org/to-scrape-or-not-to-scrape-the-technical-and-ethical-challenges-of-collecting-data-off-the-web/>`__, and said so on Twitter.

   Whyso? https://t.co/xDIUDMlovZ

   — Storybench (@storybench) `April 5, 2016 <https://twitter.com/storybench/status/717150047775887360>`__

.. raw:: html

   <p>

.. raw:: html

   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

.. raw:: html

   </p>

Well, you asked for it.

Screen scraping is the automated collection of information from the web. For our purposes, let's assume it's public information. Stuff you can load in your web browser, using an incognito window and a pasted URL. Stuff meant for ungated human consumption.

When might it be unethical to systematically collect this information, which is being published freely? I can think of a few scenarios that might qualify. If your use of the resource makes it unavailable to others, that might be unethical. This could happen if you hammer the server, but it could also happen if you mirror and resell a database that someone has spent money amassing and maintaining, undercutting them and destroying the model that sustains the resource for others.

What if the owner simply doesn't like the way in which you use their information? Some people think this is a workable way of limiting how information is used. For example, they feel that public tweets shouldn't be quoted by journalists if the tweets weren't written with widespread distribution in mind. In a screen scraping context, a realtor site might be fine with you shopping for a home but less excited about your collecting price data to power an analysis of gentrification.

I think that these kinds of implicit rules about how information is used are at best impractical. Well, okay, that's my diplomatic framing. I really think the sentiment is prudish, illiberal and ludicrous. `The transfer of knowledge is not zero-sum <http://blog.gaiam.com/quotes/authors/thomas-jefferson?page=3>`__ and we should err on the side of preserving that miraculous quality. But some people do think along opposing lines.

And although there is very little legal support for their idea that such limitations should be the default way that our society works, it's certainly possible to impose arbitrary limits on what people do with information you give to them if you can get them to agree to a contract.

This brings us to screen scraping.

You have a right to use information you've been told
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Liberal society works because facts belong to everyone. Unless you have a very good reason not to, you need to believe in your right to use published information. You need to believe in your right to think and speak freely about the things you have perceived. This is how our civilization works; it's how our minds work; it's how reality works. Don't give up this belief without a fight.

Fuck their contracts
~~~~~~~~~~~~~~~~~~~~

Nearly every website has a terms of service document. These are typically `contracts of adhesion <https://en.wikipedia.org/wiki/Standard_form_contract>`__ that say you can't use the site at all unless you agree to a ton of fine print, which will often include a prohibition on automated data collection and probably other things you will do in the normal course of using the web and sustaining belief in a modicum of personal rights. They're also sometimes called "clickwrap" licenses, a rough category of legal agreements that people mindlessly agree to through implicit action when they use software (or when they broke a seal during unwrapping, back when software came in boxes).

This is fundamentally outrageous. You do not enter a contract when you walk into a store or open a book. But the law around websites was born in a later and worse age, when we let them get away with this kind of shenanigan. To a point.

Just because a company puts something in a TOS doesn't mean it's legally enforceable. Google probably can't require you to murder a stranger as a condition of accessing your email, for example. They may not even be able to force Gmail users to permanently forego their right to sue if a self-driving car runs over Fluffy (though Google's lawyers will certainly try). When the fight lands in front of a judge, who will determine which outrageous overreaches are allowable, Google's case will be stronger if its lawyers can prove you read and understood the contract terms prior to violating them. I am not a lawyer, and you should consult a real one rather than relying on my advice. But reading the TOS may not do you any favors.

The CFAA is bullshit
~~~~~~~~~~~~~~~~~~~~

Outside of any contracts you mistakenly agree to, the Computer Fraud and Abuse Act is the primary vehicle by which scraping might get you into trouble. `Let's let the EFF explain <https://www.eff.org/issues/cfaa>`__:

   The CFAA is the federal anti-hacking law. Among other things, this law makes it illegal to intentionally access a computer without authorization or in excess of authorization; however, the law does not explain what "without authorization" actually means. The statute does attempt to define "exceeds authorized access," but the meaning of that phrase has been subject to considerable dispute. While the CFAA is primarily a criminal law intended to reduce the instances of malicious hacking, a 1994 amendment to the bill allows for civil actions to be brought under the staute.

This is a stupid, arbitrary law, and you are potentially violating it every time you use the internet. You should be aware that it exists in the same way that you are aware sharks exist. But you shouldn't let them stop you from going in the ocean.

Not asking questions is a great way to avoid dumb answers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is tricky, I know. If a site operator might be excited about your project, getting their permission might unlock better data, save you time, and avoid subsequent fights. But if they're antagonistic or even just \*surprised\*, they will instead ask their lawyers how they should respond to your request and their lawyers will (eventually) tell them to say "no". Then you will have no plausible way to claim that you didn't know you shouldn't collect the information. Worse, the publishers will be on their guard.

If you think the site operator might want to work with you, you should ask for their help. If you're not sure, you should instead ask yourself if you have an ethical claim to the data. The site operator is not necessarily the appropriate arbiter of that question. At `Sunlight <https://sunlightfoundation.com>`__ we encountered endless situations where the site operator was not the information's rightful owner. Government sites, hosting public information, with robots.txt files forbidding automated collection? To hell with that. It's wrong.

The stakes matter
~~~~~~~~~~~~~~~~~

I say all of the above blithely and confidently, and I think it's good advice for the audience to which the original talk was aimed: journalists. It is decidedly not how I approach these questions in my professional life, at least not these days. I work for a private, for-profit enterprise. We're trying to make money. We have the resources to be careful, to buy licenses, to read contracts, and to be worth suing.

And while I'm proud of how much work our company does to add to the public good, we are not investigative reporters or nonprofit activists. Perhaps more to the point: if we callously take someone else's information and they come after us with a decent argument about it, no one will shed tears for us.

If you are acting on behalf of a corporation, talk to your counsel, then talk to their counsel, then work out an agreement. Take it from Gawker, getting deposed isn't as fun as it sounds.

If you are a journalist, a hobbyist, an activist, or really anyone seeking knowledge rather than wealth: scrape that site. Teach us something. Try not to be a jerk about it. It will probably be fine.
