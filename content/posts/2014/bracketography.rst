bracketography
##############
:date: 2014-03-20 10:16
:author: admin
:category: Uncategorized
:slug: bracketography
:status: published
:save_as: 2014/03/20/bracketography/index.html
:url: 2014/03/20/bracketography/
:private: true

Reentering an NCAA bracket across multiple sites drives me nuts -- it's an obvious data format problem that could be solved very simply.

I used to think the incompatibility was deliberate, designed to capture audiences and keep them staring at a given sports site. Now I'm not so sure. The bracket functionality doesn't try to extract all that much value from us, to be honest -- these things are sponsored, sure. But there's a definite whiff of sports fan developers taking advantage of principal agent dynamics to simply build sportsy things.

But even if the incentives for compatibility aren't completely backward, the mayfly lifespan of bracket sites makes coordination difficult. Last year, after the tournament ended, I spent a few minutes emailing and tweeting at developers who seemed to have worked on the highest-profile bracket sites, but I received no responses.

So for now, bracket compatibility remains a pipe dream. It's a shame, though, because the problem is a simple one. I used to think about this in terms of JSON data formats, files that you would download and upload between sites. But it can be handled much more efficiently. There are only 64 + 32 + 16 + 8 + 4 + 2 + 1 = 127 games, after all (let's ignore the play-ins for a moment, since most bracket sites do). Each game has a binary outcome. That's 127 bits of data.

Decisions about encoding that data can be made arbitrarily; they just have to be agreed upon. Getting the order of games correct, from 0 to 126, is essential. It doesn't really matter how you do it, but here's one scheme that would work.

For each region (ordered alphabetically, A-Z); then for each round (low to high); assume the highest-ranked seed wins -- no upsets -- and assign games consecutive numbers, from highest seed to lowest. Tiebreakers fall back to the alphabetical region name ordering.

You now have 127 ordered slots to fill with ones and zeros. 1 encodes a win for a higher-numbered seed; 0 an upset. In cases of identical seeding, 1 encodes the team from the region with the alphabetically-first name.

Here's some Python that demonstrates how the resulting sequence of bits could be assembled and encoded into an easily transportable string:

.. raw:: html

   <p>

.. raw:: html

   <code>

import random, base64

.. raw:: html

   </p>

| def retrieve_winner(game_number):
| return random.choice((0, 1))

| picks = 0
| pick_bytes = []
| for i in xrange(0, 128):
| picks = (picks << 1) \| retrieve_winner(i)
| if (i % 8)==7:
| pick_bytes.append(picks & 255)
| picks = 0

print base64.b64encode(''.join(map(lambda x: chr(x), pick_bytes)))

This just makes random picks, but you could easily connect retrieve_winner() to a web interface. The output is something like "IXNcAyp72iGVl9iGE4i4FA==" (those trailing equal signs can be dispensed with), which is easily portable through email or twitter or copying and pasting. If you want it to be easily readable over the phone, you could change that "b64encode" to "b32encode" and get an all-caps string like "EFZVYAZKPPNCDFMX3CDBHCFYCQ======" -- that's only four meaningful characters longer (you have to chop off a few more ='s). Bracket tiebreakers -- usually the total score of the championship game -- could be added for a cost of 4 or 5 more characters.

In conclusion, I hate CBSSports.com
