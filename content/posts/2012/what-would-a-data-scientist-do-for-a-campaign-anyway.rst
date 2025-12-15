what would a data scientist do for a campaign, anyway?
######################################################
:date: 2012-01-16 12:31
:author: admin
:category: Uncategorized
:slug: what-would-a-data-scientist-do-for-a-campaign-anyway
:status: published
:save_as: 2012/01/16/what-would-a-data-scientist-do-for-a-campaign-anyway/index.html
:url: 2012/01/16/what-would-a-data-scientist-do-for-a-campaign-anyway/
:private: true

I take it that `this <http://www.slate.com/articles/news_and_politics/victory_lab/2012/01/project_dreamcatcher_how_cutting_edge_text_analytics_can_help_the_obama_campaign_determine_voters_hopes_and_fears_.html>`__ is what the Obama campaign `was hiring <http://www.politico.com/blogs/bensmith/0711/Obama_campaign_hiring_data_mining_scientists.html>`__ "data scientists" to do.  It's an interesting project, but I think the Slate writeup fails to make a few important connections.

First: how likely is it that the campaign actually needs a new method of gauging supporters' opinions and priorities? Not very, I'd say. Surveys and focus groups are well-developed methodologies that don't suffer from the obvious selection effect problems that a "share your story" feature on a website does.

Second: pay attention the the bits of the article recounting Rayid Ghani's resume. The work he did for Accenture sounds legit -- applying classic machine learning techniques to product classification and sales projections.  But how much of it dealt with expressed opinion ("share your story") versus observed behavior ("was this product purchased?").  The answer: lots of the latter, none of the former.

And this is important. By themselves, personal expressions are not terrifically useful. People don't know their own minds all that well. But personal expressions can be a useful signal when correlated with objective observations.

I think "[this project is] about us being better listeners" is an pretty generous gloss on what's being done here. The odds of this being an input to the platform or priorities of an incumbent president's campaign seem certain to be low.

I expect that the campaign is using this corpus of personal essays to classify supporters into better-segmented subgroups, so that more specifically customized appeals can be made to them. It's conceivable that this will be deployed for GOTV efforts, but that's a tricky experiment to run since you only get to do a trial once every few years.  More likely this is about fundraising, with classic A/B testing used to hone the model and refine the system of segmentations and corresponding appeals. If that approach delivers better results than existing methods, they'll try to use whatever demographic characteristics are available in the voterfile to segment potential supporters who haven't helpfully supplied personal essays ("he's a middle-aged white guy from Detroit--put him in the 'the bailouts worked' email group"). Whether you can generalize from someone engaged enough to contribute a "share your story" entry to someone who isn't seems like a big if, but hey, it's worth a shot.

That's my guess, anyway. None of this is nefarious; it's just what campaigns do.  But I think it's important for people to understand that, rather than a triumph of democracy-enabling technology, this is just a quantitative approach to squeezing even more money out of voters and into our political system.  It's necessary work, but I wouldn't say it's exactly noble work. If you want your political opinion to shift the policy needle, you should probably start by calling or writing your representatives, not by pouring your heart out to barackobama.com.
