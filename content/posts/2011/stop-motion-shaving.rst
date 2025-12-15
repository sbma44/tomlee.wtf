stop motion shaving
###################
:date: 2011-03-19 17:25
:author: admin
:category: Uncategorized
:slug: stop-motion-shaving
:status: published
:save_as: 2011/03/19/stop-motion-shaving/index.html
:url: 2011/03/19/stop-motion-shaving/

I'm heading to the beach on Monday, which means that the beard had to go.  I don't know when it might return -- certainly not for a long time.  It was fun, but I think I'm probably just not cut out to operate a beard at a professional level.  Ah well.

Of course, there was still the question of how to shave it off.  Usually this is taken as an opportunity to briefly sport some funny or Wolverine-related facial hair configurations, but I decided I'd waste even more time and nerd it up a bit.

|image1|

I adapted one of the demo sketches that ships with `Processing <http://processing.org>`__ to facilitate lining the shots up; if you want to do something similarly dumb, you can find the code after the jump (you'll need to update the system path near the bottom).

I encourage those of you with access to small, gullible children to tell them that the above gif represents how beards actually grow in.

| 
| [cc lang="java"]
| /\*

a tool for creating an animated gif of yourself doing something dumb

based heavily on the background diff example that ships with processing

| displays diffs between frames over a threshold so that you can see where you've moved
| hit spacebar to take a snapshot
| all frames from a given run will have the same timestamp prefix, e.g. frame-1300552348-#.png

can then convert to an animated gif using eg http://www.lcdf.org/gifsicle/ or (w/ imagemagick) "convert -delay 13 -loop 0 \*.png output.gif"

\*/

import processing.video.\*;

| int numPixels;
| int[] backgroundPixels;
| Capture video;
| long startTime = 0;
| int counter = 0;

| void setup() {
| // Change size to 320 x 240 if too slow at 640 x 480
| size(640, 480, P2D);

| video = new Capture(this, width, height, 24);
| numPixels = video.width \* video.height;
| // Create array to store the background image
| backgroundPixels = new int[numPixels];
| // Make the pixels[] array available for direct manipulation
| loadPixels();

| Date d = new Date();
| startTime=d.getTime()/1000;
| }

| void draw() {
| if (video.available()) {
| video.read(); // Read a new video frame
| video.loadPixels(); // Make the pixels of video available
| // Difference between the current frame and the stored background
| int presenceSum = 0;
| for (int i = 0; i < numPixels; i++) { // For each pixel in the video frame...

| // flip the display horizontally -- makes it mirrorlike; easier to line yourself up with it
| int j = (i - (i%width)) + ((width-1) - (i%width));

| // Fetch the current color in that location, and also the color
| // of the background in that spot
| color currColor = video.pixels[j];
| color bkgdColor = backgroundPixels[j];

| // Extract the red, green, and blue components of the current pixel’s color
| int currR = (currColor >> 16) & 0xFF;
| int currG = (currColor >> 8) & 0xFF;
| int currB = currColor & 0xFF;
| // Extract the red, green, and blue components of the background pixel’s color
| int bkgdR = (bkgdColor >> 16) & 0xFF;
| int bkgdG = (bkgdColor >> 8) & 0xFF;
| int bkgdB = bkgdColor & 0xFF;

| // Compute the difference of the red, green, and blue values
| int diffR = abs(currR - bkgdR);
| int diffG = abs(currG - bkgdG);
| int diffB = abs(currB - bkgdB);

| // provide a "ghost" image to help line things up
| float c = 0.5;
| int newR = round((c*currR) + ((1-c)*bkgdR));
| int newG = round((c*currG) + ((1-c)*bkgdG));
| int newB = round((c*currB) + ((1-c)*bkgdB));
| float totalDiff = (diffR+diffG+diffB) / (255.0*3);

| if (totalDiff>0.3)
| pixels[i] = 0xFFFF0000;
| else
| pixels[i] = 0xFF000000 \| (newR<<16) \| (newG<<8) \| newB;

| }
| updatePixels(); // Notify that the pixels[] array has changed
| }
| }

| // When a key is pressed, capture the background image into the backgroundPixels
| // buffer, by copying each of the current frame’s pixels into it.
| void keyPressed() {
| video.loadPixels();
| arraycopy(video.pixels, backgroundPixels);

| PImage temp = createImage(width, height, RGB);
| temp.loadPixels();
| arraycopy(video.pixels, temp.pixels);
| temp.updatePixels();
| temp.save("/path-to-output-directory/frame-" + startTime + "-" + counter + ".png");
| counter = counter + 1;
| }

[/cc]

.. |image1| image:: /static/2011/03/enhanced-cropped-small.gif
   :class: aligncenter size-full wp-image-1748
   :width: 241px
   :height: 296px
   :target: /static/2011/03/enhanced-cropped-small.gif
