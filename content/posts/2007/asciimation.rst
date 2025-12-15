asciimation
###########
:date: 2007-01-17 21:12
:author: admin
:category: tech
:slug: asciimation
:status: published
:save_as: 2007/01/17/asciimation/index.html
:url: 2007/01/17/asciimation/
:private: true

Well, that was kind of a waste of time. But it was fun, and I suppose I learned a few new things.

I decided, for no particular reason, to try turning a video clip into an ascii art version of itself. In theory, this can be [STRIKEOUT:easily] accomplished via a number of different open source projects:

- `Handbrake <http://handbrake.m0k.org/>`__ rips the video from the DVD
- `ffmpeg <http://ffmpeg.mplayerhq.hu/>`__ pulls the video frames out, one-by-one, and turns them into JPEGs
- `jp2a <http://jp2a.sourceforge.net/>`__ turns each frame into an HTML, ASCIIfied version of itself
- Something turns the resulting HTML back into a graphic file. I would have liked to use `khtml2png <http://khtml2png.sourceforge.net/>`__, but I couldn't get it to work. I tried a few other things, but none of them worked, either. I ended up using `webkit2png <http://www.paulhammond.org/webkit2png/>`__. But it was still a pain in the ass to get working, and it only works on OS X. Bah!
- Used the convert tool from the `ImageMagick <http://www.imagemagick.org/>`__ package to crop and convert the file back to a JPEG.
- ffmpeg puts everything back together

All of the above occurs in different phases on my mac and a linux machine, and various parts are held together by some Perl.

I chose the opening scene of *The Big Lebowski* for my test, but it ended up being a bad choice: I thought that the closeups of all the bowling paraphenalia would be easy to recognize, but something with a lot of human faces might've been a better idea. Also, ffmpeg seems to fail at putting audio back onto Flash video — I'm not sure what that's all about, since I was able to add the audio back when trying it with different formats. If anybody's got any idea what's going on, let me know.

At any rate, here are the fruits of my labor. It's somewhat neat, but probably not something I'll waste a lot more time on. The effect would probably look a lot better on fullscreen, uncompressed video — but that's not really my arena. For what it's worth, the effect works best during the scenes in the middle of the clip.

Oh! The embedded flash video player I'm using is from `here <http://www.jeroenwijering.com/?item=Flash_Video_Player>`__, and seems to be fairly slick. Also: if you can't see the video, it's because I'm hosting it through the coral CDN. If your firewall at work doesn't let port 8090 through, you're SOL. Don't worry: like I said, it's not exactly life-changing.

I think I'd probably get much better results with a cartoon, especially if I did some preprocessing to crank up the video's saturation and brightness before feeding it to jp2a. But until I've got a clean linux system (or a genuine need) I don't think I'll bother — the khtml2png solution is the right way to do screencaps. webkit2png not only requires me to pull all the files onto a mac, it makes the system's dock undulate in an oddly sensual manner as the related icon pops in and out of it for every file that's processed. It's disturbing.
