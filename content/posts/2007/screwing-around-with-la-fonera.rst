screwing around with La Fonera
##############################
:date: 2007-12-13 10:41
:author: admin
:category: tech
:slug: screwing-around-with-la-fonera
:status: published
:save_as: 2007/12/13/screwing-around-with-la-fonera/index.html
:url: 2007/12/13/screwing-around-with-la-fonera/
:private: true

I put up a `rather long post over at EchoDitto Labs <http://labs.echoditto.com/hacking-la-fonera>`__ about this, but here's the teaser version: you can get routers from the `FON <http://www.fon.com>`__ project for very little money — sometimes free, or about $10 on Ebay. With some effort, you can load them with a custom firmware that gives you a Linux environment that can connect to wifi networks. This *also* gives you a set of four or five general purpose input/output pins and a (somewhat more accessible) serial port, all of which you can, in theory, connect to an Arduino. Put together, this equals a very cheap wifi interface for your microcontroller project — the fact that it comes with powerful Linux capabilities is just icing on the cake.

It's pretty small, too. So aside from probably consuming electricity faster than a $125 wifi module designed for embedded systems would, it's really a very, very slick solution.

Of course, this is all still kind of theoretical. I've gotten the wifi interface working, and am able to control an LED from the Linux shell. That's enough to interface with the Arduino meaningfully, but I haven't yet tackled the job of connecting it to the serial port.
