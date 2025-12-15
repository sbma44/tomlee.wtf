command line rock
#################
:date: 2007-07-27 16:03
:author: admin
:category: DC, music, tech
:slug: command-line-rock
:status: published
:save_as: 2007/07/27/command-line-rock/index.html
:url: 2007/07/27/command-line-rock/
:private: true

..

   ::

      curl http://barsukmusic.blaireau.net/player/bark067/bark067.xspf | grep "<location" | perl -ple "s/<.*?>//igx" | xargs curl -O

Thanks for the heads-up, `G <http://pygmalioninablanket.blogspot.com/2007/07/news-world.html>`__/`Catherine <http://outtamindouttasite.typepad.com>`__.
