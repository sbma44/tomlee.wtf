fear of a black hat
###################
:date: 2009-12-07 14:18
:author: admin
:category: tech, Uncategorized
:slug: fear-of-a-black-hat
:status: published
:save_as: 2009/12/07/fear-of-a-black-hat/index.html
:url: 2009/12/07/fear-of-a-black-hat/
:private: true

Earlier this week my old boss, JP, sent me a note saying that the full-text RSS script I'd written was being shut down.  EchoDitto was nice enough to continue hosting it on their servers, but it had been consuming an increasing share of resources, and finally it needed to be killed.  Sad.

Then, horrifying.  JP had mentioned it idly, but until I saw the Google Alert for `this <http://www.blackhatworld.com/blackhat-seo/blackhat-lounge/145882-echodittolabs-down.html>`__ I didn't quite realize what had been going on.  The self-described black-hat search engine optimization crowd -- the folks who assemble sites peppered with ads that are designed to attract search engine traffic, aka "link farms" -- had been using my script to steal other people's content and republish it on their own sites.  Using this sort of genuine content helped them snag traffic more effectively than they could with the gibberish that you sometimes see in spam, so they were sorry to see the script go.

Well, I appreciate the attention, but it's not exactly what I had in mind for my work when I released it.  So I explained the situation, and bid them adieu:

|blackhat_seo_lg|

I was at least somewhat aware of this danger, and consequently didn't open-source the code (thank goodness).  It was still a bit of a shock to see the reality of what I'd wrought, though.

I still believe what I wrote in that `initial post <http://echodittolabs.org/blog/2007/05/full-text-rss>`__: it's pointless for online publishers to try to control how their readers consume content.  If you wish to publish digitally, you need to accept the realities that come with doing so.  Pretending otherwise is just going to inconvenience your readers and slow your business's necessary evolution.  Prolonging that process seems likely to increase the painfulness of the process, not eliminate it.

For those curious, the algorithm was exactly what many in comments had guessed.  I used some regular expressions to build a hierarchical structure representing all the <div> and <td> elements in each page associated with an RSS item.  These tags are the ones most often used to provide a page's layout, and the full text of an entry can usually be found in a single instance of such a container.  I then traversed this structure, looking for the text excerpt from the original RSS item.  Once found, the rest of that container's contents could be pulled out.  It's a simple idea, though the realities of HTML -- and the difficulty of preserving byte offsets between a sanitized working copy and the original -- made the actual implementation require quite a bit more cleverness (and caching) than it may sound like.

The result worked pretty well. Still, there were a few problems with the approach.  For one thing, comments were frequently included in the same container as the main entry.  For another, the script would fail if the RSS entry text was a summary of the item rather than an excerpt. I think that both of these are surmountable problems: a better approach would examine the "textiness" of each container using a variety of scoring metrics.  Something similar could be used for detecting the start of comments (which tend to be peppered with timestamps, quotations of the original text, and occur after a big <h[1-6]> containing the word "comment").  I took a stab at a new, Pythonic implementation using Adrian Holovaty's `templatemaker <http://www.holovaty.com/writing/templatemaker/>`__ and a few other tools, but a lack of immediate success (and much higher computational demands than the original script) made the project fall by the wayside.  Now that I know how it might be used, I'm even less likely to pick it back up.

But I'd still love to see my algorithm adapted by the people who make RSS readers, and would be happy to talk to any interested and qualified parties about making that happen.  Those SEO morons don't appear to be particularly technically proficient -- I'm not too worried about them managing to steal content via a client-side app (though certainly some thought should be given to the matter before giving the store away, say via Applescript).

.. |blackhat_seo_lg| image:: /static/2009/12/blackhat_seo_lg-96x300.png
   :class: aligncenter size-medium wp-image-1118
   :width: 96px
   :height: 300px
   :target: /static/2009/12/blackhat_seo_lg.png
