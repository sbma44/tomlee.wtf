generating the Affective Norms for English Words (ANEW) dataset
###############################################################
:date: 2010-06-16 00:41
:author: admin
:category: Uncategorized
:slug: anew
:status: published
:save_as: 2010/06/16/anew/index.html
:url: 2010/06/16/anew/

So!  At work we've been spending a couple of days working on off-the-wall projects -- it's a change of pace, a chance to work with folks not on our usual teams, an opportunity to try out new ideas, and a venue for some friendly competition.

One of the projects that my team considered but ultimately discarded was some sentiment analysis on on press statements made by legislators about the BP oil spill.  I figured we could pull some press releases, scan them for their level of aggression (or whatever) and compare the results to the level of oil industry support enjoyed by that legislator (thanks, `Transparency Data <http://transparencydata.com/>`__!).  The result probably wouldn't have set the world aflame, but if it turned out the way I expected it might've made for a fun and topical visualization.

As I said, we didn't end up pursuing that idea.  But I did get far enough in researching sentiment analysis to realize that I'd like to use the ANEW dataset -- a spatial model of various emotionally-charged words that would help me classify arbitrary texts.  Now, Emily says that she thinks sentiment analysis is "kind of bullshit", and I'm not sure I disagree.  But I think it might still be interesting to run the numbers and see what comes up.

Unfortunately, the folks who created ANEW `don't want to give their data away <http://csea.phhp.ufl.edu/media/anewmessage.html>`__.  Well, that's not quite right: they'll give it away, for free, if you're a researcher.  A researcher who has a .edu email address.  And who isn't a student.

This seems a little silly to me.  And it seems *really* silly when you consider that their `widely-available 1999 paper introducing ANEW <http://scholar.google.com/scholar?q=Affective%20norms%20for%20English%20words%20%28ANEW%29%3A%20Instruction%20manual%20and%20affective%20ratings&um=1&ie=UTF-8&sa=N&hl=en&tab=ws>`__ contains a complete data set.

`You can probably see where this is going </2007/10/16/hypem-revivified-then-vivisected/>`__.

`Here's the data in CSV format </static/2010/06/anew-1999.tar.gz>`__.  `Here's the code used to generate it <http://github.com/sbma44/begin_anew>`__. `Here's a paper that shows how to use ANEW <http://www.springerlink.com/content/757723154j4w726k/fulltext.html>`__.

Given the age of the paper its widespread availability, I can't imagine there'll be any objections to transforming its contents slightly into a more useful format. If there are, I'd be happy to hear them in comments -- and if any are made by the folks responsible for ANEW, I'll be happy to remove the link to everything here that contains even a whiff of their copyright.

And of course this is pretty old data.  I'm sure that ANEW's gotten better in the last decade (`this page <http://www.sci.sdsu.edu/CAL/wordlist/>`__, for example, refers to ANEW as containing 2000 words; my copy has just over a thousand).  But it's something to start with.  It'd be great if its creators decided to remove some of the hoops surrounding their list -- there are lots of research efforts that exist outside of the .edu TLD.
