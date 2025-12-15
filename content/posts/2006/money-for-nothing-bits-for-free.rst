money for nothing, bits for free
################################
:date: 2006-11-26 17:34
:author: admin
:category: tech
:slug: money-for-nothing-bits-for-free
:status: published
:save_as: 2006/11/26/money-for-nothing-bits-for-free/index.html
:url: 2006/11/26/money-for-nothing-bits-for-free/
:private: true

I'm embarrassed to admit that I initially clicked through to `this story <http://hardware.slashdot.org/article.pl?sid=06/11/26/140240&from=rss>`__ with interest rather than incredulity. In short: some guy claimed he had come up with a means of storing 450 gigabytes of data on a single sheet of paper through a special encoding system involving colored geometric shapes. Some of the tech press ran with it.

Well, it's `bullshit <http://itsoup.blogspot.com/2006/11/scam-of-indian-student-developing.html>`__, but that link doesn't really adequately explain why. It gets close, though. Here's my stab at an explanation, just for fun.

A laser printer can manage about 1800 dots per linear inch `according to Wikipedia <http://en.wikipedia.org/wiki/Dots_per_inch>`__. Treating each of those dots as a bit, that's 3,240,000 bits/inch\ :sup:`2`. Assuming no margins, 8.5" \* 11" \* 3,240,000 bits/inch\ :sup:`2` = a measly 302,940,000 bits, or about 295.8 megabytes (depending on which definition of megabyte you use). Allow for printing in different colors and you can multiply that by four, topping a gigabyte. Assume some sort of advanced printing technology that mixes colors in a way that provides each printed dot with 24 bits of color information like your computer screen (instead of just dithering dots of different colors to mix colors), and you're still stuck under 8 gigs/sheet.

At this point it's tempting to believe that the inventor's system of polygons introduces some sort of magic storage benefit. But it doesn't — fully compressed data looks like noise, not polygons, and pretty encoding schemes are doomed to be less efficient than ones that simply get down to the business of shoveling bits around. Think about how much data it takes to reproduce a colored triangle. There are probably more efficient ways to do it, but at a first glance it seems to me that you could accomplish it by storing two angles, the length of the longest side, and the color (for now, let's ignore how it's oriented in space on the page). The resolution and range you choose for these determines your ultimate storage requirements, but a reasonable guess would be 4 bytes for each number and 3 more for the color. Those 15 bytes comprise the descriptive capacity of that triangle — the rest of it can be figured out from those pieces of data, and consequently would be redundant to store. So, what's going to be a more efficient way of representing those 15 bytes? Drawing the triangle? Or using 0.00003704 square inches of paper to print 15 bytes?

Anyway, this is far from the first data compression scam (have a look at the fourth letter `in this Dan's Data column <http://www.dansdata.com/danletters165.htm>`__). It's not anything novel — I just find this stuff strangely fascinating. And it provides a handy opportunity for me to resume my periodic evangelism for `this book <http://www.amazon.com/Introduction-Information-Theory-John-Pierce/dp/0486240614/sr=8-2/qid=1164577747/ref=pd_bbs_sr_2/002-0432362-5412058?ie=UTF8&s=books>`__, which is short, accessible, and capable of teaching you important things about how technology works. The principles of information theory are just as important to understanding the online world as, say, conservation of energy is to understanding the physical world. At the very least, they're a big help when relatives ask you to expound in an authoritative-sounding manner about their planned digital camera purchases.
