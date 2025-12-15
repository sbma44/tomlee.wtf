whoops!
#######
:date: 2007-03-17 21:17
:author: admin
:category: tech
:slug: whoops
:status: published
:save_as: 2007/03/17/whoops/index.html
:url: 2007/03/17/whoops/
:private: true

I should've seen this one coming: I had a problem with my math in the similarity matrix stuff. I didn't think through the problem carefully enough, and failed to realize that a given representative might vote several times on a piece of legislation as various amendments and procedural votes come up. That resulted in a screwed-up data model, which resulted in taking dot products of vectors of variable length, which shouldn't have worked at all (Perl is apparently pretty forgiving about referring to variables that don't exist).

It still *sort of* worked, as you can tell from the graph. But it wasn't accurate, and most of the CPU time I had spent so far went to waste.

I think I've got it all sorted out, but I'll have to rerun all of those cosine comparisons (I've improved the algorithm's efficiency; it might take less than a day this time). But progress continues: I've also written the infrastructure for segmenting the votes by issue. I'll beat this goddamn thing yet.

Things aren't helped by Sunlight's data being somewhat messy. Some voting histories have multiple vote-records that have identical bills numbers, descriptions and dates. The only thing that varies, in fact, is the value of the vote that's stored. That's pretty goddamn confusing, so I'm just using the one that the page's order implies to be chronologically first and hoping for the best.
