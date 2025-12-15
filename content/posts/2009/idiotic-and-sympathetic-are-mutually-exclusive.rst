"idiotic" and "sympathetic" are mutually exclusive
##################################################
:date: 2009-07-24 10:36
:author: admin
:category: Uncategorized
:slug: idiotic-and-sympathetic-are-mutually-exclusive
:status: published
:save_as: 2009/07/24/idiotic-and-sympathetic-are-mutually-exclusive/index.html
:url: 2009/07/24/idiotic-and-sympathetic-are-mutually-exclusive/
:private: true

Via `Tim <http://www.cs.princeton.edu/~tblee/>`__, `here's the AP's new plan <http://www.nytimes.com/2009/07/24/business/media/24content.html>`__ for protecting its content from the depredations of those who would seek to promote it. Apparently they'll be adding a "digital wrapper" to each story, which will contain some sort of invisible watermark, or something, and will be able to communicate with the AP's servers in order to track unauthorized use -- including, astoundingly, use that is nothing more than a linked headline. A few points:

#. This plan is technologically hopeless.  It is essentially an effort to install DRM into plain text.  That's impossible.  DRM schemes fail even when added to executable, binary file formats that are read by systems under the control of the content publisher.  Neither of those conditions apply here, nor will they, unless the AP attempts to eschew the web browser entirely.  Presumably they're counting on some Javascript to phone home.  That'll work fine for AP member sites, but it will not survive the copy-and-pasted trip into a HuffPo blockquote.

#. This plan is dishonest.  It's interesting that the AP thinks its headlines contain so much unique value that they deserve protection -- very interesting indeed, given that member organizations habitually rewrite those headlines (without penalty from the AP, of course).

#. | Even if the plan could work, it wouldn't work the way they seem to think.  From the article:

      “If someone can build multibillion-dollar businesses out of keywords, we can build multihundred-million businesses out of headlines, and we’re going to do that,” Mr. Curley said. The goal, he said, was not to have less use of the news articles, but to be paid for any use.

   Similarly, if a lemonade stand starts charging $1000 per glass, their intent is probably not to reduce lemonade purchases. It's simply to create an industry-sustaining level of revenue. And who can argue with that?

It's really kind of astounding.  I can't claim to know much about econ -- once I figured out that "where the lines cross" was the answer to every exam question in 101, I pretty much tuned out -- but the realities of the situation should be apparent to anyone who's thought about these questions for even a moment.

**CLARITY!:** Also via Tim, `a diagram of how the scheme will work <http://www.ap.org/media/images/APnewsregistry.jpg>`__.  I was wrong!  All this talk about "sending signals back" pointed toward Javascript, but that "hNews format" label gives the game away: they're going to use `microformats <http://en.wikipedia.org/wiki/Microformat#Specific_microformats>`__.  Microformats are a beautifully simple idea: adding meaningful data to HTML markup in the form of specific class tags. They were big with the semantic web crowd before they got confused and started spending all their time reinventing XML and relational database technology.

Microformats won't actively cause signals to be sent back, but the AP can run a spider to look for instances of them.  And the information might survive a copy and paste! If the copier doesn't paste into Notepad in between! And they don't block the AP spider!

So yeah, it's still hopeless.  These guys need to start lobbying for substantial expansions of copyright law -- that's the only way I can see this working.  Or maybe they'll put clickwrap licenses around every AP news site that mandate preservation of the microformat data in all subsequent use.  Either way it'd prompt a very interesting legal fight.
