Metro and Google
################
:date: 2008-12-16 15:01
:author: admin
:category: DC, tech
:slug: metro-and-google
:status: published
:save_as: 2008/12/16/metro-and-google/index.html
:url: 2008/12/16/metro-and-google/
:private: true

Let's talk about Metro's recent decision to eschew Google Transit. This is a topic about which I have a small amount of inside knowledge, actually. At the end of August I wrote to WMATA's CTO, Suzanne Peck. I talked about some of the projects I'd done with WMATA data and expressed my affection for the agency. I explained that I was frustrated by the limits of the data available on wmata.com, and I requested a meeting. I received a response almost immediately (even though it was 11pm or so — a good sign in a CTO!). She thanked me for my interest, complimented me on my projects and directed me to Victor Grimes, her deputy, whom she instructed to meet with me.

I met with Mr. Grimes a week or two later. He was cordial but not too interested in what I had to say about opening up WMATA's data: according to him, the situation was well in hand. WMATA was already on its way to integrating with Google Transit. There were just a few lingering problems.

To discuss those properly, we first need to talk briefly about Google Transit. The heart of Google's system is their `GTFS format <http://code.google.com/transit/spec/transit_feed_specification.html>`__ — this stands for Google Transit Feed Specification, and it's quickly become an industry standard. It's not too complicated: basically a GTFS feed consists of a bunch of comma-delimited files with names like "routes.txt" and "stops.txt", which all get zipped up into one file and placed on the transit agency's website. You could open these up in Excel if you wanted. Google sucks this data down once a week or so, processes it and displays it within their own systems — but a transit agency doesn't have to worry about all that. They just need to make sure they get their GTFS file right, and that Google knows where to find it. Many other systems have adopted GTFS, and a lot of them make the data `available to the public <http://www.bart.gov/schedules/developers/open.aspx>`__, not just to Google.

The frequency with which Google picks up the GTFS data was an issue, according to Mr. Grimes. Google wanted to do it about once a week; that wouldn't cut it for Metro, he said. WMATA updates its data daily with bus detours, route changes and the like. It sounded like this had been worked out, though, and Google would simply arrange to pull the data every day.

The second objection involved the display of fare information. Google Transit couldn't manage this, apparently. The format does `make allowances <http://code.google.com/transit/spec/transit_feed_specification.html#fare_rules_txt___Field_Definitions>`__ for transferring fare information, but for whatever reason it wasn't up to the task of handling WMATA fares. That was fine, though; users could just be directed to the `RideGuide <http://www.wmata.com/rider_tools/tripplanner/tripplanner_form_solo.cfm>`__ website if they wanted to know fare information.

The final hurdle was bureaucratic. The various jurisdictions that make up Metro had to sign off on the release of the (already public) data. Last I heard, Maryland was the holdup. But Mr. Grimes thought this would be resolved soon. The GTFS dataset and Google Transit functionality would be released around September 23, he said.

Well, that didn't happen. I gave it a week, then wrote to ask what had happened. Here's the last I've heard, received on October 10:

   Anyway, the Google/WMATA transit integration project has come to a stand still for reasons I can't explain, but I expect things to get back on track in the near future. We are having a meeting to discuss our participation in the Google transit initiative next week and I'll let you know how that turns out.

Presumably that meeting didn't go very well. `We Love DC spots WMATA's explanation <http://www.welovedc.com/2008/12/16/wmata-says-no-to-google-transit/>`__ — it comes in the form of `a FAQ page <http://www.wmata.com/about_metro/news/faqs/preview.cfm?faqID=54>`__ put online yesterday, seemingly in effort to control the fallout surrounding their decision to ditch Google. Here's the meat of it:

   #. Google could not guarantee accurate and up-to-date Metro trip information and could not provide Metro fare information. Metro's own Web site provides near real-time travel and fare information to viewers.
   #. Many transit providers in the region are not part of Google Transit so Google's Web site viewers could not get a complete and accurate picture of their transit travel options in the Washington Metropolitan area when they use Google Transit. Metro has partnered with all the local transit providers in the Washington region to provide up-to-date and accurate information for Metro's Trip Planner. The Trip Planner factors in other area bus and rail providers, such as Fairfax Connector, DASH, ART and Ride On, and their schedules and fare information when giving customers travel options.
   #. Metro and Google have not yet come to acceptable terms regarding licensing agreements, which put Metro at a greater legal liability. Google is a for-profit company while Metro is a taxpayer subsidized public agency. Google wanted Metro's transit data at no cost and wanted the transit agency to open itself up to greater legal liability. Given financial constraints, Metro officials are exploring whether there is a way for the transit agency to generate revenue in such a partnership.

I think we can safely dismiss the second point — hearing about the ART bus might be nice, but it's hardly a sufficient reason for scrapping this project. Based on my conversation with Mr. Grimes, I also think point one is probably a red herring. Those limitations were known in August, and they weren't considered show-stoppers then. I suppose Google may have ultimately decided that they couldn't support a daily GTFS update, but this seems very unlikely to me — the Metro system is big, this technical problem is small, and enough people would find this integration useful that I'm sure they'd find a way to support it. I suppose point one could also be interpreted to mean that WMATA was insisting on some sort of service level/data accuracy guarantee that Google couldn't or wouldn't provide, but insisting on such a point seems a bit unreasonable.

So that leaves us with point three, which basically boils down to: Google needs to cough up some dough. I'm actually a bit more sympathetic to this idea than you might expect. "Google Transit Feed Specification" sure *sounds* like a proprietary format. It's easy to imagine a bureaucrat with sign-off powers seeing that and saying, "Wait a minute. We're doing all this work for a private enterprise and they're not even paying us for it?" Google is an awfully helpful company, but presumably it's offering transit information because it makes them money (or at least supports their brand). WMATA's in perpetual need of cash; there's no reason it should be giving Google freebies.

But this misses the larger point. GTFS may be unfortunately eponymous, but it's an open format. Exposing schedule data in useful ways should be part of WMATA's mandate — the current system of bulky PDFs used for bus schedules is downright inexcusable. I don't particularly care whether WMATA lets private firms like Google use its data for commercial ends, but it should certainly grant noncommercial rights to the public.

**THIS JUST IN:** More from Mr. Grimes:

   Yes, there is still an issue between WMATA and Google regarding the licensing agreement. However, we are in continuing discussions with Google and looking at other options for making the data available in GTFS format not only to Google but to others who have requested the information. You are correct in that much consideration has been given to this effort and it is not over. I will let you know as soon as a decision has been made regarding the direction WMATA will take to provide the transit data in GTFS format.

Also, `via DCist <http://dcist.com/2008/12/16/google_transit_here_come_the_excuse.php>`__ the Examiner `confirms <http://www.dcexaminer.com/local/Metro_involvement_with_Google_Transit_held_up_by_the_details.html>`__ that this is really about money. Well, good. WMATA should put the GTFS dataset online under a Creative Commons noncommercial license, and Google should cough up the $68k of online ad revenue that WMATA's afraid of losing. Lord knows they've got the money.

**FURTHER:** One of Ezra's commenters `points out <http://www.prospect.org/csnc/blogs/ezraklein_archive?month=12&year=2008&base_name=google_and_the_dc_metro#comment-6243029>`__ that Google Transit isn't actually all that great. I'm not that familiar with it, but I'm not too surprised — it's a hard problem. But even if Google can't do it, someone else can.

Also: it's worth mentioning that the real payoff here is for buses. Figuring out how to ride the train is dead simple; the bus, not so much. Right now it's easy for people to read the PDF bus schedules, but hard for them to figure out what the schedule means (or which schedule is the correct one); these difficulties are reversed for computers. If WMATA releases the GTFS dataset, riding the bus could become much easier for a lot of people.
