everyone has a right to their beliefs
#####################################
:date: 2011-01-14 14:00
:author: admin
:category: Uncategorized
:slug: everyone-has-a-right-to-their-beliefs
:status: published
:save_as: 2011/01/14/everyone-has-a-right-to-their-beliefs/index.html
:url: 2011/01/14/everyone-has-a-right-to-their-beliefs/
:private: true

|image1|

I'm sorry, but no. `It's a lousy polemic <http://www.slate.com/id/2281146/pagenum/all/>`__. Here's its structure:

#. SEO-friendly statement of controversy
#. Presentation of opinion A. Assertion that people who hold it are rubes.
#. Presentation of opinion B. Invocation of authority.
#. History lesson! Discussion of old technology; no mention of enforcement of author's preferred orthodoxy by newer technology (e.g. HTML rendering multiple spaces as one)
#. Rumination on beauty. Grecian urns, etc.

For now let's ignore the ignore the bullying nature of this argument (it should be obvious to anyone that those of us who believe in two spaces are a minority that's relentlessly and mercilessly persecuted by the bloodthirsty masses, both through jeremiads like Manjoo's and through the technological eradication of our ability to express our beliefs). Which of the points in the above argument are rhetorically meaningful?

Only point 3 really carries any weight with me. I'll take Manjoo's word that all typographers like a single space between sentences. I'm actually pretty sympathetic to arguments from authority, being the big-state-loving paternalist that I am. But, with apologies to friends and colleagues of mine who care passionately about this stuff, I lost my patience with the typographically-obsessed community when they started trying to get me to pay attention to which sans-serif fonts were being used anachronistically on *Mad Men*.

I love you guys, but you're crazy. On questions of aesthetic preference there's no particular reason that normal people should listen to a bunch of geeky obsessives who spend orders of magnitude more time on these issues than average. It's like how you probably shouldn't listen to me when I tell you not to use .doc files or that you might want to consider a digital audio player with Ogg Vorbis support. I strongly believe those things, but even I know they're pointless and arbitrary for everyone who doesn't consider "Save As..." an opportunity for political action.

Nor should we assume that just because typographers believe earnestly in the single space that their belief is held entirely in good faith. They're drunk on the awesome power of their proportional fonts, and sure of the cosmic import of the minuscule kerning decisions that it is their lonely duty to make. *Of course* they don't want lowly typists exercising their opinions about letter spacing. Those people aren't qualified to have opinions!

(For what it's worth, I don't think you rabble should be using Flash or Silverlight or anything other than plain text in your emails. You can't be trusted with it! And, not that this motivates me or typographers at all of course (we just want what's best for you), but when you do such things it makes my job slightly harder.)

Manjoo's argument about beauty, like all such arguments, is easy enough to dismiss: I disagree. I find it easier to read paragraphs that are composed of sentences separated by two spaces. Perhaps this is because I, like most technologists, spend most of my time working with (quite lovely!) fixed-width fonts for practical reasons. But there's also a deeper beauty to the two space rule -- a sort of mathematical beauty. Let me explain.

Consider the typical structure of writing. Letters are assembled into words, which turn into phrases, which are arranged into sentences -- at the same time being assigned to speakers, a neat trick -- which are then combined into paragraphs.

It's a chemical process, a perfect and infinitely flexible hierarchical system that should command our admiration. Being able to rationally examine, disassemble and interrogate the final product is a mark of the system's beauty. Anything less is settling for a sort of holistic mysticism.

It's disrespectful to let writing's constituent elements bleed into one another through imprecise demarcations. If you see me "making mistakes with comma placement", please rest assured that I'm doing it deliberately. In most cases the comma doesn't belong to the phrase delimited by the quotation marks that enclose it. Placing an exclamation point or question mark to the left or right of a close-quote is a weighty decision! That we violate the atomic purity of quotations with injected commas is an outrage.

And though I don't get quite as worked up about it, the same sort of thinking motivates my belief in the double space. Sentences deserve to be clearly delineated, but because of the complications of quotation, ellipses, interrogatives and exclamations (among others), there is no reliable punctuation that can be counted on as a terminator for sentences. Single spaces are already spoken for: they separate words. The double space is an elegant and subtle solution.

To operationalize it: I can split any of the paragraphs in this post (as composed, not as rendered) into its constituent sentences with a simple line of Python:

| [cc lang="python"]
| for x in paragraph.split(' '):
| print repr(x)

| "And though I don't get quite as worked up about it, the same sort of thinking motivates my belief in the double space."
| "Sentences deserve to be clearly delineated, but because of the complications of quotation, ellipses, interrogatives and exclamations (among others), there is no reliable punctuation that can be counted on as a terminator for sentences."
| "Single spaces are already spoken for: they separate words."
| "The double space is an elegant and subtle solution."
| [/cc]

Further disassembly is easy from there. I can't do that with the degenerate text that Manjoo prefers. As a journalist who makes his living on consumers' pageviews it's perhaps understandable that he would deliberately complicate news consumption for his non-human audience. But I hope the rest of us can make our aesthetic decisions a little less selfishly.

.. |image1| image:: /skitch/slate_tweet_20110114.png
   :class: center
   :target: http://twitter.com/Slate/status/25932689622179840
