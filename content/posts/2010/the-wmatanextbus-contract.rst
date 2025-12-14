the WMATA/Nextbus contract
##########################
:date: 2010-02-02 16:02
:author: admin
:category: DC, news
:slug: the-wmatanextbus-contract
:status: published
:save_as: 2010/02/02/the-wmatanextbus-contract/index.html
:url: 2010/02/02/the-wmatanextbus-contract/

Every DC Metro rider owes Michael Perkins a debt of gratitude. For a while now he's been not only `covering WMATA <http://greatergreaterwashington.org/author.cgi?username=michaelp>`__ **[UPDATE: link fixed]**, but jumping through the hoops necessary to `uncover details of their contracts, budgets and other documents <http://www.scribd.com/perkinsms>`__ (and working on tech projects besides!).

Over the weekend he published his latest acquisition: `the WMATA/Nextbus contract <http://www.scribd.com/doc/26194581/Nextbus-Contract-Redacted>`__. As you might imagine, it takes the reader on a harrowing emotional rollercoaster. But before we get to that, let's build some dramatic tension.

**PREVIOUSLY, ON "LICENSING QUESTIONS RELATED TO NEXTBUS DATA"**

After pulling the service due to concerns about its reliability, WMATA finally redeployed Nextbus last year. This happened not too long after the release of WMATA's scheduling information in the open GTFS format -- combined, the two excited a lot of interest in transit-enthusiast developers like myself.

But under what circumstances could the Nextbus data be used? The answer was not at all clear. Fortunately, Nextbus representatives began to pop up in relevant comment threads. Unfortunately, it soon became clear that there are *two* companies called Nextbus -- one of them is "Nextbus, Inc." (which I'll call Nextbus) and one is "Nextbus Information Systems" (which I'll call NIS). I emailed back and forth with representatives from both. First, my emails with Alex Orloff from NIS:

Me:

   Alex, another question for you: there's a lot of online confusion surrounding the relationship between Nextbus, Inc. and Nextbus Information Systems. Can you clarify the relationship between the two? Do you both have contracts with WMATA? And am I right in thinking that you're the company responsible for the Washington, DC-centric Nextbus app in the iPhone store? I'm seeing folks show up in blog comment sections who claim to be affiliated with these two companies, and who are asserting contradictory things.

Alex:

   When the transaction that created NextBus Inc. as a wholly owned subsidiary of Grey Island Systems occurred, NextBus Information Systems kept what is called the "distribution business" piece of NextBus, which includes all the things you would associate with distribution of data - licensing to third parties, delivery to cell phones, etc. The NextBus DC app on the App Store is indeed ours. We understand that there is some confusion about the relationship and we have encouraged NextBus Inc. to put a web page on nextbus.com helping people to understand our role. We think that that would be the simplest way to clear up any confusion - don't you think ?

Me:

   Much of the conversation is occurring at the Greater Greater Washington blog. And yes, I agree that it would be helpful if Nextbus clarified its relationship to your organization and the bounds of its arrangement with WMATA.

   Am I right in thinking that Nextbus Information Systems has no formal arrangement with WMATA, but rather possesses the rights to license the distribution of some of the data emerging from the Nextbus/WMATA agreement?

   Sorry if this is muddying the waters -- just trying to get to the bottom of where I and other DC-area devs stand.

Me:

   Aha I see the discussion now, I had seen that post a few days ago but Mike Smith's comment was not up then. Did he send you any information directly ? I'm curious as to what he said if you have contacted him directly. We are definitely trying to get NextBus to be more open about our relationship with them and our rights. Many developers are asking the same questions, and like you, many are confused about what's what.

   We do not have an agreement with WMATA directly, our rights come from the agreement that was part of the sale to Grey Island, which reserved exclusive rights to distribution of the predictions, in particular to cell phones but also advertising, licensing, etc. in the United States (and UK). So our agreement covers any transit agency that NextBus tracks here in the US.

Next, my correspondence with Mike Smith of Nextbus.

Me:

   Thank you for contributing to the comment thread at Greater Greater Washington. I hope you won't mind clarifying the distinction between your organization and Nextbus Information Systems (NIS). I've been in touch with Alex Orloff of NIS, and from my discussions with him have developer the understanding that Nextbus Inc. is contracted with WMATA, but that Nextbus Information Systems -- a wholly distinct entity -- retains the rights to distribute the resulting data to mobile devices, via an API, and perhaps in other ways.

   I and others in the DC developer/transit community find all this quite confusing. I have a number of questions that I hope you won't mind answering. I think they'll go a long way toward clarifying the situation:

   1. Is the relationship between Nextbus Inc. and Nextbus Information Services that I have described correct?

   2. If NIS has the right to distribute the data, am I correct in assuming they have access to your servers? Mr. Orloff indicated a desire to have Nextbus Inc. clarify the relationship between the two firms at nextbus.com, leading me to believe that you have control over the domain; but surely he has \*some\* access to your systems if he is able to offer an API view of the data, as he indicated.

   3. If NIS owns the rights to distribute the data but does not control the servers, what steps is Nextbus Inc. obligated to take in order to restrict third parties' access to the publicly available data at e.g. wmata.nextbus.com?

   4. Does Nextbus assert ownership over non-predictive data produced as part of its contract with WMATA (e.g. routeconfig files)? What is its position on noncommercial use of such data?

   Thanks very much for your help in clarifying these issues.

Mike:

   It would be inappropriate for me to weigh in on what distribution rights that NextBus Information Systems (NBIS) does or does not have, since they are indeed a separate entity. But I can tell you that the transit agencies own the data and have legal control over it.

   Sorry I cannot be of more help.

   Mike

I wasn't able to get more out of either of them. So here's my understanding of the situation: at some point, Nextbus sold the main part of its business to Grey Island Systems. An independent portion remained, however, called Nextbus Information Systems, and it retained the rights to license prediction information generated by past -- and future! -- deals with the part now owned by Grey Island. The Grey Island/Nextbus folks say that the transit agencies they contract with own full rights to the data, same as NIS, but they're understandably hesitant to step on the NIS folks' toes (lest they get sued, presumably). Mr. Orloff was very helpful, but made it clear that I'd need to purchase a license before distributing any Nextbus-based application. Mr. Smith was also helpful, but not really empowered to speak about the licensing situation.

**WHICH BRINGS US TO THE CONTRACT**

First: Grey Island Systems is listed as the parent company of the Nextbus that did business with WMATA. So far so good. But then things take a discouraging turn:

|image1|

But wait! There's reason for hope: (WMATA is "the Authority" in this excerpt):

|image2|

And finally, vindication (CIS = Customer Information System, i.e. Nextbus):

|image3|

It's possible that I'm missing something, but at this point I think my pre-contract understanding has been validated: WMATA has full rights to the data, which means it can give the data away if it wants to. Now we just need WMATA to give the all-clear! We may also need them to mirror the data or otherwise ensure that Nextbus can't complain that we're unfairly hammering their servers. I've got some ideas about how to proceed, and I've got a serendipitous meeting happening in the next few days -- more soon, I hope!

.. |image1| image:: http://www.manifestdensity.net/wp-content/uploads/2010/02/nextbus11.png
   :class: aligncenter size-full wp-image-1232
   :width: 450px
   :height: 178px
   :target: http://www.manifestdensity.net/wp-content/uploads/2010/02/nextbus11.png
.. |image2| image:: http://www.manifestdensity.net/wp-content/uploads/2010/02/nextbus2.png
   :class: aligncenter size-full wp-image-1231
   :width: 500px
   :height: 714px
   :target: http://www.manifestdensity.net/wp-content/uploads/2010/02/nextbus2.png
.. |image3| image:: http://www.manifestdensity.net/wp-content/uploads/2010/02/nextbus3.png
   :class: aligncenter size-full wp-image-1233
   :width: 450px
   :height: 89px
   :target: http://www.manifestdensity.net/wp-content/uploads/2010/02/nextbus3.png
