oh, MT
######
:date: 2008-08-13 11:12
:author: admin
:category: tech
:slug: oh-mt
:status: published
:save_as: 2008/08/13/oh-mt/index.html
:url: 2008/08/13/oh-mt/

Around work I'm known as something of a Movable Type apologist. I can't help it — it's how I was raised. MT was the first thing I tried to install `six years ago <http://www.zunta.org/blog/archives/2002/08/28/narcissism_what/>`__ when I decided to check out the burgeoning blogging phenomenon, back when the media was merely interested in, rather than terrified of, the whole business.

Movable Type's greatest strength is handling traffic, which of course is not something I've ever really needed it for. When you make a change to a site MT picks up all the data you've entered, passes it through your templates and generates a plain ol' HTML file, which it then plops in the appropriate directory. It also updates a few other files, like your site's main page. But these are similarly static (by "static" I mean a page that doesn't ask the server to do any computation as it's served). As you might imagine, serving static pages is a relatively easy task for a webserver — all the computational cost of composing a page is incurred once, when it's created, and the result is saved. The overhead for each subsequent page-serving is consequently as small as it can be. This is what makes MT good at dealing with traffic.

But the system that does this is built on unappealingly old, slow technology. And besides, there are good reasons for wanting dynamic functionality on a page. You can create a hybrid sort of site — this blog is an example, as it uses a lot of PHP in its MT templates — but it's a little awkward to build and maintain. You can extend the core MT system, too, but it's not always well-suited to the task. Over the past few years I've watched as the folks at Gothamist, with the help of `Apperceptive <http://apperceptive.com/>`__, have done this time and again, cajoling MT into accomplishing things that it really has no interest in doing. Sometimes I've been frustrated by this process; other times I've been impressed. Either way, their efforts can be fairly described as heroic. But if they were using a different platform there wouldn't be a need for quite as much heroism. I suspect this wouldn't be a bad thing.

Now `Ars <http://arstechnica.com/news.ars/post/20080813-movable-type-pro-to-meld-blogging-and-social-networking.html>`__, acting uncharacteristically like a press release proxy, brings word of MT 4.2 Pro. Despite the enthusiastic writeup, the announcement leaves me about ready to call it a day on MT. Not that I'll stop using it, mind you — porting this blog would be a pain — but it's clear that its time is done. Six Apart is already retreating from the stab at openness that they made with MT4. And the warmed-over social networking features that they're now offering feel just a bit desperate. There is nothing here that can't be easily accomplished with `Wordpress MU <http://mu.wordpress.org/about>`__ or `Drupal <http://drupal.org>`__.

And that's alright. I'm glad to see those other (free) projects ascendant: Wordpress has managed to harness its community's enthusiasm for writing some of the world's worst PHP code and turned it into a successful, professional product that's actually well-engineered (if subject to more security bulletins than I'd like to see). With the caching technologies it has available, there's no longer a great reason for using MT.

And Drupal — well, I spend so much time with Drupal that my feelings are inevitably mixed. But I'd take it any day over Movable Type (and Wordpress, for that matter).

I'm glad to keep a hand in MT. It's a very different system than those other blogging platforms, and that's probably good for me. But it's no longer possible to make a great case on its behalf. The only thing it has going for it is the company behind it: if you buy a commercial license you can call up Six Apart and yell at them in a way that isn't possible with non-corporate projects. That's certainly enough to build a business on — ask Redhat. But in terms of total yelling *period*, I'm ready to concede defeat on behalf of MT proponents everywhere.
