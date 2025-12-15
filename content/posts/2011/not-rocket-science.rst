not rocket science
##################
:date: 2011-08-05 13:14
:author: admin
:category: Uncategorized
:slug: not-rocket-science
:status: published
:save_as: 2011/08/05/not-rocket-science/index.html
:url: 2011/08/05/not-rocket-science/
:private: true

I mostly really like The Awl these days -- contra `Quinn <http://www.quinnnorton.com/said/?p=559>`__, I think the site started strong, had a rough patch, and now is back to publishing a lot of great stuff. `But this is not a very good article <http://www.theawl.com/2011/08/was-aaron-swartz-stealing>`__. It's credulous about things that call for skepticism, and skeptical about things that are perfectly reasonable.

   A lot of people seem to believe that it doesn't cost anything to make documents available online, but that is absolutely not so. Yes, you can digitize an academic journal and put it online, but if you mean to offer reliable, permanent availability, it costs a huge amount of money just to keep up with the entropy. Plus you have to index the material to make it searchable, not a small job. Everything has to be backed up. When a hard drive fries, when servers or database software become obsolete or break down, when new anti-virus software is required, all this stuff requires a stable and permanent infrastructure and that does not come cheap. Finally, the more traffic you have, the more it costs to maintain fast, uninterrupted server access; you can see this whenever some little blog is mentioned in a newspaper and its server crashes five seconds later. In the case of JSTOR you are looking at many millions of hits every month, and they can't afford any mistakes.

Actually, `all this stuff really is pretty cheap <http://aws.amazon.com/s3/#pricing>`__. And then there's the other nice thing about the internet: digital content of genuine utility can be more-or-less counted on to self-perpetuate.  Release a valuable DRM-free file onto the network and its preservation *somewhere* is more or less funded automatically by the people who exchange it. Besides, costs continue to fall while the size of scanned documents remains constant.

It's true to some extent that dealing with large-scale distribution and managing bitrot in any particular centralized location does involve costs.  So it's not that JSTOR doesn't need money.  It's more that we don't need JSTOR.

   There are nearly 19,000 documents in this 33GB download [of out-of-copyright JSTOR documents uploaded in protest by Greg Maxwell], and anyone can take them off The Pirate Bay—and then what? It will tax an ordinary home computer quite a lot to search just this one file, the archives of a single journal of the 1,400-plus currently distributed by JSTOR; that's the tiniest drop in the bucket. The practical futility of Maxwell's gesture only demonstrates that JSTOR is providing an invaluable service to the public, even with respect to documents in the public domain—one that could be improved upon, maybe, but completely impossible for individuals to duplicate using existing technologies.

This is just flat-out wrong. Someone who knows what they're doing will need to OCR those PDFs and dump the results into Solr or something like it, but the actual language-to-be-searched will be a fraction of that 33GB total.  This was a big but tractable problem for a home computer a decade ago.  Today it's basically trivial; my rough guess is that the task is on par with searching through a decade's worth of email.  Besides which, people who actually need this data -- researchers, for instance -- can deal with not-that-much-more-inaccessible tools to get at it.

I'm sure JSTOR's system is impressive.  But you know what?  There are a lot of people on the internet who can build impressive systems, and many of them are willing to do so and make the results available for free if it's for a halfway decent cause.

   It seems far more likely that if he meant to distribute any JSTOR articles on a file-sharing site, he would have stripped out any copyrighted material first (1.7 million of the 4.8 million articles he downloaded, according to the indictment.) That would be child's play for someone like Swartz to do, and it would certainly have decreased his chances of landing in the soup.

Spoken like someone who's never had to figure out if a document is in copyright (much less do so programmatically). Unless JSTOR had already done the work of figuring this out, it would've actually been a very difficult task.  That 1.7 million number is likely representative of documents that can be positively said to be in copyright.  It is much harder to positively say that something is out of copyright.

   Still, `the government's indictment alleges <http://www.scribd.com/doc/60353785/Untitled?secret_password=1pnh76ns7nc9cnonp1sg#full>`__ that he intended to distribute the stuff to the public "through one or more file-sharing sites," without offering any details as to why they think he was going to do that. If they hope to prove this allegation based solely on the 2008 Guerrilla Open Access Manifesto, it would seem that they have got an uphill climb.

   For one thing, Swartz has been working for years on analyzing huge data sets at Harvard and elsewhere. He has a longstanding professional interest in the study of large data sets. Sure, it's a little bit fishy that he didn't use the network at his home institution in order to access JSTOR. If the allegations in the indictment are true, it would also appear that Swartz took steps to cover his tracks in order to escape detection. I could think of a zillion possible reasons for this with one lobe tied behind my back: Did Swartz want to keep the nature of his work secret from a colleague for some professional reason? Had the Harvard IT department refused to permit him to take that much data down?

I don't really know what to say about this other than it seems like a stretch to me.  Occam, etc.

From that point on, the article is actually pretty good, discussing the strangeness of the government's decision to indict, the specific charges being brought, and ending with a very nice wrapup that appropriately and respectfully invokes Lessig and Malamud.  Still, while you all know I'm usually as cranky as anyone about internet utopianism, it really is the case that digital technology is both incredibly powerful and incredibly cheap.  JSTOR and the journals are more rentiers than humble archivists struggling to cover costs.

 
