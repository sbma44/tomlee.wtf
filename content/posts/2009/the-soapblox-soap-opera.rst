the SoapBlox soap opera
#######################
:date: 2009-01-08 09:28
:author: admin
:category: politics, tech
:slug: the-soapblox-soap-opera
:status: published
:save_as: 2009/01/08/the-soapblox-soap-opera/index.html
:url: 2009/01/08/the-soapblox-soap-opera/
:private: true

I've been watching the SoapBlox saga, and its coverage, with morbid fascination — my interest and the vehemence of my reaction to it all are probably a sign of the increasingly provincial nature of my expertise, I suppose, and that's a little depressing. But still, I feel compelled to point out that most of the reaction to it is idiotic.

Here's the story: DailyKos runs on a system called Scoop. It's kind of a monstrosity, but large swaths of the netroots are used to it, terrified of change, and have consequently convinced themselves that the system they started using first happens to be technically superior to all the ones they encountered thereafter. This isn't a novel delusion by any means; most of us do it all the time, myself included.

One developer decided there were some things he didn't like about Scoop and elected to rewrite it in a different language. You can find the project announcement `here <http://www.dailykos.com/story/2005/3/27/61120/4863>`__, and it should immediately set off warning bells:

- There's no indication that he's envisioning his efforts as an open source project.

- He clearly hasn't bothered to learn much about Scoop, given that he misidentifies the language it's written in as PHP rather than Perl. If he'd opened a single source file, he could not have made this mistake.

- | He said this:

     | I am not a language snob. I know all languages have their place. And I see php as the language for a small to medium sized operation. Java is an Enterprise solution and a complete, robust language, capable of interacting with just about anything computer.
     | If we want to take blogs to the next level, we have to take our blogging software to the next level.

  | This is the kind of meaningless bullshit that salespeople say when they know nothing about anything except that they have something written in Java that they'd like to sell. Java's great, it's fine, but PHP powers sites like Digg and Facebook, so don't tell me it can't run your blog about Rhode Island politics. Perl, can, too — obviously it powers dKos and other Scoop sites, but it also manages to keep Slashdot afloat. It's not the loveliest language around, and aside from Scoop and Movable Type, web development has pretty much moved on to faster and/or cleaner languages. But it can clearly get the job done.
  | Also: "capable of interacting with just about anything computer"? What does that even mean?

- His email address is *pacified69@yahoo.com*. Come on.

Despite this, the sorry state of Scoop hosting and the netroot throngs in its thrall seem to have been enough to push jScoop to some success as a proprietary host for political communities. The hosted effort was branded as SoapBlox, it acquired a few machines, and it charged reasonable rates. Then it got hacked.

I haven't seen the code; it's not open source. And it's been years since I wrote any Java, so I might not be able to make heads or tails of it even if I did see it. But my guess is that the author didn't just reinvent the wheel in terms of Scoop, but also in terms of forms processing, sanitizing input, session handling and who knows what else. Some vulnerability was left exposed, and someone took advantage of it.

Hey, we all make mistakes. Bugs happen. But it's our responsibility to make sure that our mistakes happen in places that are unlikely to lead to catastrophic problems. That means building on other people's work. Googling for existing projects and reading old mailing list archives is less fun than firing up TextMate and starting to type, but you've just gotta grit your teeth and do it.

One of SoapBlox's servers went offline, and the dev abruptly declared defeat. The users were understandably freaked out. Unfortunately, that's leading them to make some bad judgments. Here, from a Kos diary entitled "`Why SoapBlox Matters <http://www.dailykos.com/story/2009/1/7/121323/7371/193/681191>`__":

   SoapBlox includes all the major features of a community blog -- namely, user diaries and other community-building features. These features are NOT readily available in any other software platform WordPress, MoveableType and others make it exceedingly difficult to do things like diaries and frontpage promotions, and SoapBlox makes it easy.

This just isn't true. There are plenty of projects that can match the requirements of SoapBlox's users. I've used Drupal a lot, and can say with confidence that it offers the diary, threaded-commenting, rating, voting and front-page-promotion features that seem to be at the heart of Scoop. And hey, `this guy seems to like it <http://scoop.kuro5hin.org/comments/2006/6/1/41757/36255/9#9>`__. SoapBlox doesn't matter because of its software; it matters because of the bloggers and diarists that use it. Writing blog software is much, much easier than running a successful online political community. There's plenty of software out there, and the SoapBlox community ought to set its priorities accordingly.

Right now parts of the netroots are rallying around SoapBlox, trying to get it back online in a sustainable way. This speaks well of them, but it's a mistake. This one-off of a project should never have been trusted with anything worth saving. Who knows what other exploits lurk in its codebase? Or what business problems might take it offline in the future? You can say that opensourcing the project will help resolve these problems, but that's only true if you can also find developer manpower willing to continue reinventing this particular wheel. Frankly, you're not going to find high-quality talent that's willing to donate its time to a cause this pointless.

`TechPresident suggests another path <http://www.techpresident.com/blog/entry/33526/soapblox_burnout_points_to_vulnerability_in_left_s_infrastructure>`__:

   Options now for SoapBlox include [...] wrapping the platform into the services offered by one of the bigger progressive tech firms like Blue State Digital, EchoDitto, or Advomatic.

Speaking as a someone who until recently worked at EchoDitto, and whose boss is now one of Blue State's founders, this is also a stupid idea. If one of these firms wants to do this work for free, then sure, the SoapBlox bloggers should jump at the chance. But hiring a consultancy is an option that's vastly more expensive than what's needed by these sites — sites which are, frankly, not particularly sophisticated from a technical or design perspective.

Here's what I would suggest. First, make sure the SoapBlox admin is content to keep the sites up, at least temporarily. Second, find a college-age technical wunderkind who's interested in politics and willing to work for cheap. These guys are a dime a dozen — I used to be one myself. Third, convince him to write an exporter for the SoapBlox data that puts it in a standardized format. Hooking into `this project <http://code.google.com/p/google-blog-converters-appengine/>`__ (found via `al3x <http://del.icio.us/al3x>`__) might not be a bad idea. Getting the data into a portable form is the priority.

Then, find someone at a consultancy like one of the aforementioned ones who's willing to help you figure out your requirements and specifications for a new suite of software. The simplest, best option is probably to just run Scoop. It's what you want anyway; might as well stop nosing around it. I'm not intimately familiar with Scoop, but a quick look at its installation procedure makes it look like the complexity of installing and running it has been vastly overstated. If you don't do that (or just want to help get the netroots off Scoop — a noble cause), then I'd suggest a hard look at Drupal and maybe Wordpress MU, or maybe Slashcode if for some reason you want to head toward Perl-land. You may have to get someone to develop a custom module or two to make the solution maximally Scoop-y, and you'll certainly need someone who knows their way around the system to help configure it.

But given where the aesthetic bar has been set, this is not a particularly tough problem, and it shouldn't cost that much money. If this community can afford to send people to Netroots Nation or the DNC, it can surely afford a minor investment in its critical infrastructure. Oh, and one more thing: when users inevitably raise a hue and a cry because the order of links on the sidebar has changed, or because they have to reconfirm their email address, or because of some other stupid thing, you should ignore them. They just want attention. Learning new systems and habits is a pain, but not nearly so painful as continuing to limp along in a system that never should have been used in the first place.
