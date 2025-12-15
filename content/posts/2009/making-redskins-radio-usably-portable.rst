making Redskins Radio usably portable
#####################################
:date: 2009-09-10 22:51
:author: admin
:category: tech
:slug: making-redskins-radio-usably-portable
:status: published
:save_as: 2009/09/10/making-redskins-radio-usably-portable/index.html
:url: 2009/09/10/making-redskins-radio-usably-portable/
:private: true

Surely any Redskins fan will agree that foremost among Dan Snyder's sins is his selection of a broadcast outlet that only provides its audio stream in Flash.

See, I'm going to be heading back from Philly this Sunday, and many Sundays besides, and I'd rather not miss the whole goddamn football season.  If WTEM provided an MP3 stream this would be no problem -- the FStream iPhone app would let me listen to the game on stretches of I-95 well beyond the anemic reach of 980 AM.

That's not the case, though.  WTEM uses a Flash-based streaming system, apparently through a vendor called streamtheworld.com.  That's fine for the web browser, but the iPhone's too stupid to deal with Flash.

So I set out to provide an alternate stream.  Amazon offers on-demand virtual servers through its EC2 service, and my first thought was to fire one of those up for each game.  At ten cents an hour it would be affordable, and I could use the more-competent server to transcode the Flash stream into a more iPhone-compatible MP3 stream.

I got far enough along this path that I might as well share my work.  Here's a quick recipe for setting up a VLC-transcoding-capable server on EC2:

#. Launch the following Ubuntu AMI: ami-ed46a784

#. Make sure that you've opened port 8080 in the relevant security settings.

#. | Execute these commands:

      | apt-get -y update
      | apt-get -y install libmp3lame-dev
      | apt-get -y install ffmpeg libavcodec-unstripped-52
      | apt-get -y install vlc vlc-plugin-esd mozilla-plugin-vlc

#. | Execute something similar to, but not quite this:

      sudo -u nobody vlc -vvv "http://208.80.52.80/WTEMAM" --sout '#transcode{acodec=mp3,ab=64}:standard{access=http,mux=asf,dst=}'

This is close.  It's *really* close.  If you run this and then load up `VLC <http://www.videolan.org>`__ -- the amazingly useful media player -- and connect to the AMI on port 8080, you'll get a 64 kbps transcoded MP3 stream of the WTEM flash audio stream.  It works well!

Unfortunately, I don't know the specific incantation that makes this MP3 stream compatible with `FStream <http://phobos.apple.com/WebObjects/MZStore.woa/wa/viewSoftware?id=289892007&mt=8>`__ on the iPhone.  I tried various playlist formats.  I tried various audio formats.  I tried various container formats.  There doesn't seem to be any decent documentation on the internet telling me what to do.  It just says it's connecting, forever.

But while searching for a solution I discovered something interesting: there's an iPhone version of VLC!  True, it's 13 megs, and yeah, it's only available on jailbroken phones (via the Cydia package manager).  But it works great!  I pointed it at http://208.80.52.80/WTEMAM and it started spitting out incomprehensible sports radio babble almost immediately.  Admittedly, that was over wifi.  But I see no reason to expect it to perform any worse over 3G than an equivalent MP3 stream would.  I'll be giving it a shot on Sunday during the Giants game. And while I'm sorry to not be providing an MP3 stream for other fans, I'm glad to offer another reason to jailbreak your phone.
