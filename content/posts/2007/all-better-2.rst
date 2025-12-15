all better
##########
:date: 2007-11-04 22:30
:author: admin
:category: internal affairs
:slug: all-better-2
:status: published
:save_as: 2007/11/04/all-better-2/index.html
:url: 2007/11/04/all-better-2/
:private: true

Back online! See, the new machine uses CGI and suexec instead of mod_php, and so files with permissions greater than 0755 throw an error, but Movable Type creates files at 0666 by default. It's obviously all pretty fascinating, but the short version is that everything should now be fixed.
