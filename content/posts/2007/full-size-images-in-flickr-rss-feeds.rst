full size images in Flickr RSS feeds
####################################
:date: 2007-04-02 16:44
:author: admin
:category: tech
:slug: full-size-images-in-flickr-rss-feeds
:status: published
:save_as: 2007/04/02/full-size-images-in-flickr-rss-feeds/index.html
:url: 2007/04/02/full-size-images-in-flickr-rss-feeds/
:private: true

Something that JP and I just figured out at work: how to change a Flickr RSS feed so that it returns images larger than the default, using Yahoo Pipes. `Here's <http://pipes.yahoo.com/pipes/pipe.run?_id=8je0aFnh2xG9imFFJxOy0Q&_render=rss>`__ a feed of my photos demonstrating the functionality. `Here's <http://pipes.yahoo.com/pipes/pipe.info?_id=8je0aFnh2xG9imFFJxOy0Q>`__ the pipe in question, so that you can adapt it to your own feeds. And `here's <http://www.flickr.com/services/api/misc.urls.html>`__ Flickr's documentation on its URL formats — if the 1024 pixel size is too large for you (or you want a smaller-than-normal image for some reason) consult that link and replace the "\_b" in the first regex block with the appropriate underscore + letter combination (or remove it entirely for the default size of 500 pixels on the longest side).

Now that it's got a regex module Pipes is even more powerful. It does seem at least slightly buggy, though: the regexes to strip out the width and height really should be able to be combined into a single operation (e.g. /(width|height)=['"]\\d+['"]/), but that didn't work for some reason and I had to break them out. Ah well.

The only major broken thing about Flickr's RSS that remains is the fact that if your contacts add photos too quickly, Flickr won't show them all to you. It's sad but true — if your contacts post more than 20 photos in the interval between Flickr's RSS regeneration (or your feedreader checking your contacts feed), some will simply never appear. Drag. I can think of ways to solve this, but not with Pipes, unfortunately. In fact, given that Pipes is likely to query your feed less frequently than your feedreader, this solution may suffer even more from that limitation. I haven't tested it carefully, but suggest that you try it out side-by-side with the default Flickr feed for a while to ensure that it's not dropping photos.

**UPDATE:** Looks like there's a bug in Pipes that makes the Regex module default to operating on the "title" field when you load this pipe and edit it. Be sure to change that to point to "description" instead, otherwise the pipe won't process the right part of the RSS and won't alter the feed at all.

**UPDATE 2:** I made a modified version that lets you plug in your own contacts feed RSS URL (and delivers 500px images, not the 1024 versions). You can find it `here <http://pipes.yahoo.com/pipes/pipe.info?_id=HHvHTP7h2xGPZ1tDdbq02Q>`__. Just get the URL you currently use for your contacts feed out of your RSS reader (or Flickr) and paste it into the text box. Submit the form, then scroll to the bottom of the page for the link to the RSS version of the pipe's output.
