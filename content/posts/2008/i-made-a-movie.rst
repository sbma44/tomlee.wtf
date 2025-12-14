I made a movie
##############
:date: 2008-05-22 11:45
:author: admin
:category: DC, tech
:slug: i-made-a-movie
:status: published
:save_as: 2008/05/22/i-made-a-movie/index.html
:url: 2008/05/22/i-made-a-movie/

Inspired by `Robert Hodgin <http://www.flight404.com/blog>`__'s `impressive work <http://www.flight404.com/blog/?p=121>`__, I decided I wanted to take a crack at making animations in Processing. Inspired by `Rob Goodspeed <http://goodspeedupdate.com/>`__'s thoughtful experiments, I figured I might as well try to make it about something interesting.

The DC `Office of the CTO <http://dcstat.octo.dc.gov/dcstat/site/default.asp?dcstatNav=%7C30914%7C>`__ makes a lot of interesting data available, so I decided to take a crack at doing something with it. Here's my first pass: it's a visualization of every reported crime incident in 2007.

Blue means property crime — robbery, larceny, etc. Red means violence — assaults, murders and the like. Green means sex crimes. The color-coding is obviously less than perfect, but is at least sort of interesting. Each frame in the video represents 8 hours — one police shift. Colors gradually fade to a dark, translucent gray after two weeks' worth of time has elapsed. You can view a larger version of this video by clicking through to the movie's `Vimeo page <http://vimeo.com/1049199>`__, and an even better-quality version by then scrolling down to the lower right for a Quicktime download link. You'll need to log in or create a Vimeo account for the Quicktime — but you should! Vimeo is the best videosharing site I've used by a mile.

At the moment I'm trying to figure out where I should go from this point. A few ideas:

#. Add graphs and a calendar display to help users see the relative levels of crime over the course of the movie
#. Identify and place a street map under the crime visualization
#. Produce a static, high-resolution render showing the differences in location of crime between 2007 and 2008 (YTD)
#. Do it all over again with the city's pothole data (also geocoded!)
#. Add a jaunty soundtrack

If you have any other suggestions, please let me know. Those of you interested in the geeky details should keep an eye on `EchoDitto Labs <http://labs.echoditto.com>`__ — if I can find time I'll be posting an accounting of the tools I used over there.

*City-mandated disclaimer after the jump*

   The data made available here has been modified for use from its original source, which is the Government of the District of Columbia. Neither the District of Columbia Government nor the Office of the Chief Technology Officer (OCTO) makes any claims as to the completeness, accuracy or content of any data contained in this application; makes any representation of any kind, including, but not limited to, warranty of the accuracy or fitness for a particular use; nor are any such warranties to be implied or inferred with respect to the information or data furnished herein. The data is subject to change as modifications and updates are complete. It is understood that the information contained in the dataset is being used at one's own risk
