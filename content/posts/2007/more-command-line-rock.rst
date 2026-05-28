more command line rock
######################
:date: 2007-12-13 12:50
:author: admin
:category: music, tech
:slug: more-command-line-rock
:status: published
:private: true

Recording for posterity, because recreating Perl one-liners is a pain in the ass. If you're on a \*nix like system (including OS X), this will download all the MP3s linked from a given URL:

   ::

      curl -s http://somemusicblog.com/goodsongs.html | perl -nle 'print $1 while /\<a\b[^\>"]*?\bhref=\"?([^\>"]*)\.mp3/g' | xargs -I {} curl -O {}.mp3

**UPDATE:** `This URL <http://earfarm.blogspot.com/2007/12/ear-farms-top-ten-bands-to-emerge-in.html>`__ might be a good one to try it out on.
