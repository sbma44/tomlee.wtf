we love to build
################
:date: 2007-02-07 12:44
:author: admin
:category: music, tech
:slug: we-love-to-build
:status: published
:save_as: 2007/02/07/we-love-to-build/index.html
:url: 2007/02/07/we-love-to-build/

Holy crap. That Swimmers album is better than I'd expected — is it too early to start nominating candidates for Album of the Summer? The last few years' poor, belated crops of AoTSes makes me think that it'd best to get way out ahead of this thing. Anyway, you can listen to the whole album over at `their website <http://www.theswimmers.com/>`__. I particularly like "We Love To Build" and "St. Cecilia".

Relatedly, thanks to their use of the XSPF player the following super-nerdy\* command is possible. I normally wouldn't post it, but I think it's the first time I ever actually got sed to do what I wanted.

   ::

      wget -q -O - http://theswimmers.com/player/playlist.xspf | sed -e '/annotation/d' -e '/playlist/d' -e '/track/d' -e '/encoding/d' -e 's/<\/*location>//g' | xargs wget

A similar technique should be possible with the `Hype Machine <http://hype.non-standard.net>`__, but their failure to use line breaks in their XSPF files makes the regex composition a bit harder, so I haven't bothered to figure it out yet.

\* Admittedly, it's not even *close* to being as nerdy as `this <http://stevenf.com/2007/01/zeppl_1.php>`__, which is awesome (via `Miller <http://www.allthegooddomainsweretaken.com/>`__'s `del.icio.us feed <http://www.allthegooddomainsweretaken.com/>`__).
