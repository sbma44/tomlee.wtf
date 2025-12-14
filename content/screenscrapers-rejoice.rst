screenscrapers, rejoice!
########################
:date: 2007-07-18 15:06
:author: admin
:category: tech
:slug: screenscrapers-rejoice
:status: published
:save_as: 2007/07/18/screenscrapers-rejoice/index.html
:url: 2007/07/18/screenscrapers-rejoice/

Adrian Holovaty has just released a Python library called `templatemaker <http://www.holovaty.com/blog/archive/2007/07/06/0128>`__ that promises to make screen-scraping much easier.

Some explanation: if you're trying to do something automatically with a website, it's best if it has an API. This is a reliable, documented interface that your program can use to interact with the other site. Flickr has an API; Google has an API; del.icio.us has an API. Lots of sites have APIs.

But lots of sites don't. WMATA, for example, has none. In that situation you're stuck writing a program to parse the HTML of the site, which was designed to be viewed by humans, not robots. Here's a very simple made-up example. This table:

======= ======
Time    Line
======= ======
9:00 AM Orange
1:00 PM Blue
======= ======

Looks like so in HTML:

   | <table align="center" border="1" width="300">
   | <tr><th>Time</th><th>Line</th></tr>
   | <tr><td>9:00 AM</td><td>Orange</td></tr>
   | <tr><td>1:00 PM</td><td>Blue</td></tr>
   | </table>

And I can write some regular expression-laden Perl (or whatever) to extract info from it like so:

   | while(my $l=<>)
   | {
   |    if($l =~ m/<tr><td>(.\*?)<\\/td><td>(.\*?)<\\/td><\\/tr>/i)
   |    {
   |       print "train time is $1 and color is $2\\n";
   |    }
   | }

This is a pain in the ass. Worse, if WMATA decides they want to make some minor cosmetic changes — altering the background color of each odd-numbered result row, or changing to 24-hour time notation, or even just adding some line breaks to make their HTML more readable — the regular expression will break and have to be meticulously redesigned. And this is just a simple example; in reality the initial regex will be much more unwieldy and the fixes much harder to identify and make.

Holovaty's templatemaker aims to automate this by matching similar stretches of text, allowing it to determine which portions of a set of documents vary and which remain constant, then plucking the variable data out on the basis of its analysis. Some of that will be junk — you probably aren't actually interested in the breadcrumbs or meta tags in a set of pages, although they're quite likely to vary across the set — but with an intelligent look at the results, this could greatly speed up the process of extracting data.

Check out the `sample usage <http://code.google.com/p/templatemaker/>`__ for a simple example of what I'm talking about. I'm not much of a Python-lover, but I'm looking forward to using this project.
