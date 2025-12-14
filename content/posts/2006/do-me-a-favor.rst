do me a favor
#############
:date: 2006-12-19 11:18
:author: admin
:category: tech
:slug: do-me-a-favor
:status: published
:save_as: 2006/12/19/do-me-a-favor/index.html
:url: 2006/12/19/do-me-a-favor/

And help me test out a project I'm working on. The number of excerpt-only RSS feeds in my reader has finally hit the point where it began gnawing away at me. So I've taken a stab at writing a utility to automatically turn partial RSS feeds into full-text ones. If you've got any partial-text feeds that have been bugging you, I'd appreciate your giving it a try. If you run into problems, leave them in comments.

.. container::

   .. raw:: html

      <form action="http://www.metamonkey.net/fulltextrss/" method="get">

   RSS Feed URL

   .. raw:: html

      </form>

Be forewarned: it's far from perfect. There are some sites that it can't figure out — perhaps unsurprisingly, `Wizznutzz <http://www.wizznutzz.com>`__ is one of them. In other cases it'll include duplicate titles, or unnecessary dates, or irrelevant parts of the site design. And sometimes it reports that full-text retrieval has failed when in fact it was just a very short entry. Oh! It also won't be able to tell when an item has been updated.

But ignore all of that. I'm interested to know the cases (like Wizznutzz) where it fails completely. Functionality first, then beauty. Well, actually, functionality then optimization then *maybe* beauty — a general-purpose solution isn't likely to ever make every feed look lovely. More important is the fact that it's dog-slow when it's not serving cached content. If I leave it running on this server all hell will eventually break loose. So consider this just for testing — I'll get it to a stable point sometime soon, then move it to a more permanent residence.
