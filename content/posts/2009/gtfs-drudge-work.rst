GTFS drudge work
################
:date: 2009-04-02 10:08
:author: admin
:category: DC, tech
:slug: gtfs-drudge-work
:status: published
:save_as: 2009/04/02/gtfs-drudge-work/index.html
:url: 2009/04/02/gtfs-drudge-work/

Last night I finally found a moment to begin playing around with the WMATA GTFS data. Well, that's not quite right: I tried to use the Django ORM to load the dataset when it was first released, but a memory leak killed the process when I left it to run overnight — something that doesn't bode particularly well for our use of the ORM `at work <http://www.subsidyscope.com>`__.

Last night I shoved the data it into a barebones MySQL database and added a few convenience columns to make it easier to work with the embedded time and date information. The scripts I used to do this take a little while to run (a few hours, perhaps, on the index-creation step — this could doubtless be sped up by moving the math into the SQL itself). And my use of MySQL is somewhat dumb, as the GIS capabilities of Postgres make it a more obvious choice. But if you're just looking to get started with this stuff, this will at least save you from having to write the CREATE TABLE statements yourself. It's all up on GitHub — `have at it <http://github.com/sbma44/py-gtfs-mysql/tree/master>`__.

The next step for me is to generate a second-by-second snapshot of where every bus in the city is throughout the day, then feed that into `Processing <http://processing.org>`__ to make a movie like `this one </2008/05/22/i-made-a-movie/>`__. Maybe I'll even add a soundtrack this time — anybody feel like doing some field recordings of Metrobuses?
