a poor use of my time
#####################
:date: 2012-12-08 16:35
:author: admin
:category: Uncategorized
:slug: a-poor-use-of-my-time
:status: published
:save_as: 2012/12/08/a-poor-use-of-my-time/index.html
:url: 2012/12/08/a-poor-use-of-my-time/

Still, the lingering shreds of my 14 year-old self couldn't help wasting a few hours writing a convenience utility for extracting snippets from the Simpsons for throwaway-gag social media use. I did this despite realizing that, yes, quotation is a low and basically irritating form of humor -- it's basically the same as the bully with the audio-playing jacket in *Back to the Future II* . Still, if you've got a library of video you want to pull snippets from, `perhaps you'll find it useful <https://github.com/sbma44/simpclip>`__.

Important notes/caveats to this important work:

- Having to upload to an FTP endpoint sucks. Using a video service would be great, not least because they'd handle the tedious ffmpeg tweaking I wasted a bunch of time on. And, in fact, I had this working with YouTube. But their copyright infringement detection algorithms are too good. It's a shame; I feel that quotation of this kind is fair use.
- Quicktime is a real jerk, and ffmpeg is a mystery. For an embarrassingly long time I couldn't get Apple's default OS X codecs to play the H.264 file I was making (VLC played it no matter how badly I mangled the parameters, of course). Using the .mov contained was the trick. Bah.
- Is there really no URL shortener that will work without an API key? Weird. Weird and stupid.

Mostly this saves me a minor amount of trouble -- the command line is faster and more flexible than the VLC/SimpleMovieX/CyberDuck workflow I used to employ. But my real motivation has more to do with a pie-in-the-sky featureset I've daydreamed about for a while:

#. Enter text phrase
#. Search database of extracted subtitles for timestamps and surrounding text.
#. Select desired quotations.
#. Search for moments of audio silence surrounding the window indicated by the rough subtitle timestamping.
#. Potentially repeat the process with `video scene transition <https://ffmpeg.org/trac/ffmpeg/ticket/442>`__ data.
#. Plug results into today's script, automating the gap from remembering a line to pulling the video for it.

Again, a huge waste of time. I don't even have a torrent with subtitles yet! And I have a ton of projects I ought to get to before then, not least of all my mom's website. But if I were a collective of infinite monkeys, I'd certainly tackle this. Hell, one could conceivably connect it to work, if you ignored C-SPAN's copyright and pulled all their video and transcription.

A more tractable next-step is probably adding animated GIFs as an output option.
