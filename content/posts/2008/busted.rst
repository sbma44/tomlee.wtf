busted
######
:date: 2008-02-20 15:59
:author: admin
:category: tech
:slug: busted
:status: published
:save_as: 2008/02/20/busted/index.html
:url: 2008/02/20/busted/

Whoops! We got a DMCA notice at work today from our ISP, and I'm to blame. It was an accident, honest! I had (allegedly!) been downloading episode five of The Wire's current season and neglected to shut off my Bittorrent app before leaving home. Apparently HBO took notice and didn't take kindly to it.

First: I'm currently an HBO subscriber, so I'm feeling pretty karmically okay about all of this.

Second: I may have been downloading a bunch of other season 6 eps at the same time (I had a plane ride ahead of me and catching up to do!) but HBO apparently only noticed the torrent for episode 5 — a lousy torrent made from an HBO screener DVD, incidentally, with horribly clipping audio throughout. It wasn't even the good stuff! It makes me wonder if they're particularly sensitive to leaked screeners.

Third: although I'm being flip, this is still an embarrassing and stupid mistake. The last thing I want to do was expose the company to liability so that I can timeshift my preferred crime dramas. The odds of dire consequences arising from this particular incident seem to be fairly nonexistent, but it's certainly something I want to avoid in the future. Having no faith in myself, I turn to technology.

OS X maintains an app called Kicker that does various things when network events occur — things like changing wifi access points. It also has an XML configuration file you can modify that'll allow you to run your own scripts. Scripts like this one:

   ::

      #!/bin/sh
      #get the ssid of the network
      ssid=`ioreg -l -n AirPortDriver | grep APCurrentSSID | sed 's/^.*= "\(.*\)".*$/\1/; s/ /_/g'`
      #fill in your own values for ssid and location below
      if [ $ssid = "YourWirelessNetwork" -o $ssid = "YourOtherWirelessNetwork" ]
      then
      `killall Transmission`
      fi
      exit 0

`Transmission <http://www.transmissionbt.com/>`__ is the name of the app I use for Bittorrent. You'll want to change that and the wifi network placeholders (capitalization matters!). Then you'll want to save that file somewhere safe and \`chmod +x *whatever_you_called_it*\ \`. Then follow `these directions <http://www.macgeekery.com/gspot/2006-05/hacking_kicker_and_configd_to_run_your_scripts>`__ for editing Kicker.xml so that it'll run your script. Voila! The script will run whenever you change networks. It'll check the name of the network and, if there's a match, terminate the Transmission application (potentially messily, I should add — this may be bad for your downloads in progress).

All in all, a pretty clever way to avoid my own stupidity. Hopefully someone else will find it useful, too.

**UPDATE:** Hmm. After installing this setup I began to experience some pretty weird system blocking errors — most noticeably Terminal.app freezing, but other weirdness, too. You may want to hold off on it for now. I'm giving it another go using a Ruby script that forks immediately in the hopes that this will prevent anything from sticking:

   ::


      #!/usr/bin/ruby
      pid = fork do
      #get the ssid of the network
      ssid = `ioreg -l -n AirPortDriver | grep APCurrentSSID | sed 's/^.*= "\(.*\)".*$/\1/; s/ /_/g'`
      #fill in your own values for ssid and location below
      if ((ssid =~ /YourWirelessNetwork/i) || (ssid =~ /YourOtherWirelessNetwork/i))
      `killall Transmission&`
      end
      end
