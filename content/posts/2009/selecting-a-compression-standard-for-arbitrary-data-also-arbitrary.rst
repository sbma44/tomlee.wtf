selecting a compression standard for arbitrary data: also arbitrary!
####################################################################
:date: 2009-09-25 12:16
:author: admin
:category: Uncategorized
:slug: selecting-a-compression-standard-for-arbitrary-data-also-arbitrary
:status: published
:save_as: 2009/09/25/selecting-a-compression-standard-for-arbitrary-data-also-arbitrary/index.html
:url: 2009/09/25/selecting-a-compression-standard-for-arbitrary-data-also-arbitrary/

In keeping with this site's new ambition to become a J. Sanchez metablog:

   Randomly wondered when/why RAR supplanted ZIP as the default compression scheme. Internet knows: http://www.codinghorror.com/blog/archives/000798.html - @normative, `9/25/2009 <http://twitter.com/normative/status/4370570567>`__

The Coding Horror writeup is characteristically excellent, but the story is actually a little more complicated than it implies.  It provides good reasons why RAR is superior to ZIP.  But why hasn't RAR been beaten by something else?

As with many technologies, the answer lies in the balance between the advantages of the new technology and the costs of sacrificing the incumbent technology's network effects -- that, and simple timing.  To wit: 7Zip is a format that, in most situations, is `as good or better than RAR\* <http://kikizas.net/en/apps.7z.html>`__.  It's also an open standard, unlike RAR.

So why isn't 7Zip in use instead of RAR?  I think it comes down to timing.  The standardization of large-file trading on Usenet demanded a format that could be broken into chunks, as a single post can only carry a limited amount of binary data*\*.  ZIP can handle this sort of operation -- I have fond memories of spreading friends' EGA games across innumerable bitrot-ridden 1.44M floppies -- but it's a feature that had been ignored or intentionally dropped by many Windows 95-era ZIP clients.  RARs were also typically a few percentage points smaller than ZIPs at a time when the average home user's internet connection was several orders of magnitude slower than it is today.

There was a moment when piracy became professionalized, and at that moment RAR was the best thing going.  And it's still pretty good!  The situation is quite similar to that of the MP3 format: it's been beaten by better audio compression schemes like Ogg Vorbis and AAC, but MP3 is good enough -- and popular enough -- that it's not worthwhile to tear out out the infrastructure that's been built around it.

Admittedly, I doubt that RAR will remain in vogue as long as MP3 will.  A shift in audio codec means buying hardware players with new chipsets -- and, not infrequently, acquiescing to the DRM gimmicks of whatever corporation is pushing the new format.  Archive formats can be counted on to only matter in a flexible general-purpose computing environment, where those concerns don't really apply.  Also, archive formats can be selected in an ad-hoc manner by release groups made of technical users that are largely immune to network effects -- the popularity or usability of their release is much less important in their insular prestige economy them than is its timing.  For these reasons `it's not at all uncommon to run across 7Zip torrents <http://isohunt.com/torrents/7z>`__.

So RAR might fall out of fashion some day. But it owes more of its popularity to being the right technology at the right time than it does to its current technical merits.

\* This comparison asserts that RAR's dominance has to do with its "repair archive" functionality.  I disagree; I've never found that feature to be reliable enough to be worthwhile.  Usenet file-traders agree with me, and instead rely on a checksum metafile standard called SFV which helps both to correct errors and, in some situations, to replace missing files.

\*\* Torrents are presumably still broken into volumes because the releases have been plucked from Usenet, which remains the font of nearly all piracy. It's also handy to be able to download a single volume and run a checksum on it to look for malware before grabbing the whole archive, but this is a relatively uncommon thing for casual users to do.
