the killer app
##############
:date: 2008-10-23 12:37
:author: admin
:category: tech
:slug: the-killer-app
:status: published
:save_as: 2008/10/23/the-killer-app/index.html
:url: 2008/10/23/the-killer-app/
:private: true

|image1|\ For a while now I've been trying to convince Charles that he ought to jailbreak his iPhone. I'm not sure why I feel compelled to do so, exactly, and the reasons that might motivate Charles to take my advice have been even murkier. Getting a free terminal app is reason enough for me, and running Bittorrent off my phone has a certain novelty. But these days most users' needs are pretty well taken care of by the App Store.

Well, I've got a better justification now: comics. As you might imagine, there's a robust trade in pirate scans of comics on the Bittorrent tracker sites. It's easy to partake, and, for me at least, a fairly guilt-free experience: downloading back issues has propelled me to dramatically increase my actual comic purchases. For instance, I'd been a little curious about Hellboy when I first heard of the series. But after downloading the complete run, I find myself buying every new BPRD TPB the moment it's in stores (and slowly but surely picking up physical copies of the older books that I'd first read electronically). In my case, at least, the net effect is clear: comic piracy has allowed the industry to extract much more money from me than it otherwise would have.

We're still a ways off from digital comics competing with their physical counterparts — much further than for books, I'd say. But it's still nice to be able to catch up on storylines that you'd otherwise only hear about on Wikipedia (or text boxes signed "– ED"). And having a huge collection of idle reading on your phone is pretty great. It's hard to make myself suffer through an ebook on a tiny screen, but for some reason the prospect of a comic seems more appealing.

The iPhone turns out to be surprisingly well-suited to the task, too. I won't claim that it isn't a little tough on the ol' eyeballs, but the resolution of the screen makes it *just* possible to read issues in landscape mode without zooming. And of course you can always do the normal pinch-to-zoom operation that's offered by mobile Safari.

Enough evangelizing: how do you do this?

**1. Unlock your phone.**

These days, it's simple. You'll probably want to use QuickPwn, which is available in `Windows <http://blog.iphone-dev.org/post/50888951/redmond-we-have-a-pwnapple>`__ and `Mac <http://blog.iphone-dev.org/post/49988701/pwnagetool-and-quickpwn-for-2-1-firmware>`__ flavors. Just launch the utility; it'll walk you through the procedure.

Once you've jailbroken, you'll notice a few changes on your iPhone. For one thing, the startup graphic will be a pineapple instead of an apple. For another, there'll be a new application called Cydia — it's got a brown icon. This is one of the programs used to install software on jailbroken iPhones. Run it; download whatever updates it wants to install; then install the following packages:

- OpenSSH
- Toggle SSH
- iComic

The first package installs SSH, the lingua franca of secure inter-machine communication. It's a behind-the-scenes sort of thing. The second package makes it easy for you to turn SSH access to your phone on and off — important for both security and battery reasons. The third is the actual comic-reading program. If you'd like, you can install the program called ComicViewer, too — it's by the same author, and, aside from some UI differences, virtually identical. I haven't found much reason to favor it over iComic, though, and it's easier to distinguish books with long filenames under iComic. Both are flaky in various ways, so it's probably worthwhile to occasionally check back for upgrades and figure out which one you prefer.

**2. Get Some Comics**

This is also easy. You just need to visit `IsoHunt <http://isohunt.com/>`__ or `TPB <http://thepiratebay.org/browse/602>`__ and find some comics. Keep an eye out for multi-packs — frequently a lot of issues are bundled together into large files centered around a theme — say, Dark Horse's output for a given month, the complete collected works of Alan Moore, or all of a crossover event like Civil War. Sometimes it'll be a cross-house monthly update. Just browse around, taking time to note the lists of files available by clicking through to each individual torrent's file description page.

Then download. On OS X you'll want to use `Transmission <http://www.transmissionbt.com/>`__, I think. On Windows folks seem to like `ÂµTorrent <http://www.utorrent.com/download.php>`__.

**3. If Necessary, Convert Your Comics**

Comics are generally distributed as CBR or CBZ files. It's interesting, actually — no, really. These are extremely simple formats — ad-hoc standards arrived at by groups of people who have more patience for tedious scanning than they do elite technical expertise. The formats are just zip or rar files, basically — that's why one ends in z and the other in r (sometimes you'll see them with .zip or .rar extensions instead of the CBR or CBZ convention — it's the same thing). Inside each archive is a bunch of JPEG files, the names of which determine the order in which they'll be displayed. It's a simple standard built on existing, open formats. A little metadata might be nice, but that could be easily solved by including an XML or YAML file in the archive. Anyway, let's not get ahead of ourselves.

Both of these formats are easily read by desktop software like `Jomic <http://jomic.sourceforge.net/>`__. iComic and ComicViewer can only handle CBZs, though, so if you end up with CBRs — and you probably will — you'll need to convert them. This is pretty easy to do manually: download `WinRAR <http://www.rarlab.com/download.htm>`__ (Windows) or `UnRarX <http://www.unrarx.com/>`__ (Mac), uncompress the file, then compress its contents back into a zip. Simple.

If you'd like to automate the process and aren't afraid of the command line, here's a little Ruby script that'll automatically convert your CBRs. This could probably be done with a single clever line of bash scripting, but hey, this is easier to figure out. It should work right away on OS X if you install UnRarX to your Applications folder. If the unrar executable lives elsewhere, though, you'll have to edit the variables at the top. Also, there's a line near the bottom that you can uncomment if you'd like to delete the source CBRs when you're done with them. I don't trust my script enough to use it before seeing how its handiwork turns out, though.

   ::

      #!/usr/bin/ruby
      require 'Time'
      # change this to point at a command line unrar utility, if necessary
      UNRAR = '/Applications/UnRarX.app/Contents/Resources/unrar'
      # same thing here
      ZIP = '/usr/bin/zip'
      while (path = STDIN.gets)
      exit if (path==nil)
      path.strip!
      new_filename = path.sub(/cbr$/i,'cbz')
      working_dir = ('/tmp/' + Time.now.to_i.to_s)
      `mkdir #{working_dir}`
      `#{UNRAR} e "#{path}" #{working_dir}`
      `#{ZIP} "#{new_filename}" #{working_dir}/*`
      `rm -rf #{working_dir}`
      # uncomment the following line to automatically delete your old CBRs
      #`rm -f "#{path}"`
      end

You invoke the script like this (assuming you're in the top-level directory housing the comics that need to be converted):

   ::

      find . -type f -name "*.cbr" | ruby /path/to/cbzify.rb

If you're on Windows you probably shouldn't bother with all this. There are some PC-based conversion options discussed in `this thread <http://www.ipodtouchfans.com/forums/showthread.php?t=23759>`__. I'm afraid I don't have any first-hand experience with them, though.

**4. Copy the files to your phone**

Alright. Time to actually move the files over. First things first: make sure your phone and computer are on the same wifi network. Then head into the iPhone's settings screen. Under "General", temporarily turn off the Auto-lock feature. Now go into your wifi settings, to the network selection screen, and hit the blue arrow next to the name of the network you're on. Scroll down and find the phone's current IP address. Write it down.

Okay, now head back to the home screen. Find the "Toggle SSH" application, launch it, and turn SSH on. You can then exit back to the home screen — SSH will remain enabled until you come back here and disable it. Any open SSH connections will break whenever the phone goes to sleep, though, which is why we turned off Auto-lock.

We're going to need to do two things, both over SSH. The first is to create a directory called /var/mobile/Media/Comic. The second is to copy the comic files into that directory (or subfolders under it). If you're on windows, both of these tasks can be accomplished using `WinSCP <http://winscp.net/eng/index.php>`__. The address of the phone is the IP you wrote down earlier. The login is "root". The password is "alpine" (yes, on all iPhones — this is why you should turn off SSH when we're done).

On a Mac we already have the software necessary to do the copying. Open up an instance of Terminal and do the following, substituting your phone's appropriate IP address, typing out "yes", and entering the password "alpine" when prompted:

   ::

      $ ssh root@192.168.0.xxx
      The authenticity of host '192.168.0.xxx (192.168.0.xxx)' can't be established.
      RSA key fingerprint is ab:cd:ef:12:34:56:78:90:ab:cd:ef:12:34:56:78:90.
      Are you sure you want to continue connecting (yes/no)? yes
      Warning: Permanently added '192.168.0.xxx' (RSA) to the list of known hosts.
      root@192.168.0.xxx's password:
      localhost:~ root# mkdir /var/mobile/Media/Comic
      localhost:~ root# logout
      Connection to 192.168.0.xxx closed.

Then just use the rsync utility to copy over the files. Again, from the directory with the comics in it:

   ::

      rsync -v -r --exclude=*.cbr . root@192.168.0.xxx:/var/mobile/Media/Comic/

This may take a while. But once it's done, you just have to launch iComic and everything should be there. Disable SSH, turn Auto-lock back on, delete the source files — you're all set. Actual navigation through the comics is done by tapping the lower right or left corner of the screen. Returning to the main menu is accomplished by tapping the upper left corner. Be patient — it takes a second or two to turn pages.

`Lots more information about iComic can be found in this thread <http://www.ipodtouchfans.com/forums/showthread.php?t=23759>`__. Enjoy!

.. |image1| image:: /static/2008/10/23/20081022_ultimateironman-20081022-141238.jpg
   :class: right
