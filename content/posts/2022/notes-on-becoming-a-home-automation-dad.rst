notes on becoming a home automation dad
#######################################
:date: 2022-02-01 23:18
:author: admin
:category: Uncategorized
:slug: notes-on-becoming-a-home-automation-dad
:status: published
:save_as: 2022/02/01/notes-on-becoming-a-home-automation-dad/index.html
:url: 2022/02/01/notes-on-becoming-a-home-automation-dad/

When did the pandemic start? I remember returning from a vacation. My wife had to work but I took the week off. We hired a nanny. The hotel was unremarkable except it had a water park sort of thing with slides and a lazy river, and weed is legal in California. We had heard about a sickness in China before leaving. Now there were reports that it was nearby. Reason for concern! Our hotel seemed fine (what did that mean?), but it was something we thought about the last night when I went to pick up tacos. I am pretty sure the pandemic started during our drive home from the airport, back in D.C.

I can't tell you when I did everything described in this post, except to say I've been stuck in this house for years now but the mail still arrives, even from China. Precious little sachets entombed in packing tape and customs declarations language that could be generously described as inadequate.

I know I installed the projector around when my first daughter was born. I splurged on a motorized screen for it so I could flick a toggle switch to control its descent and retraction. Soon the sting of that purchase faded, and shouldn't I get the thing that puts it on a remote control? Of course I should.

Other pieces accreted over time. A smart outlet for the Christmas lights. A garage door opener with wifi. A light switch in the bedroom that Alexa mostly refuses to acknowledge. Before long this had become a bit of a mess: a tangle of apps on my phone, a house full of gadgets doing things that my wife couldn't control. This is the point at which a home automation platform becomes helpful. Too helpful, maybe. Once set up, the possibilities reveal themselves more fully. Did you know they have motorized window blinds now? The compulsive homeowner's task becomes not only automation, but seamless integration. I have been chasing this dragon ever since.

.. container:: float wp-block-image size-large

   |image1|

If you are a programmer, or really anything else, home automation software will probably frustrate you. It wants to empower users to construct complex integrations and processes. It also wants to shield them from details and the conventions of real programming. These conflicting imperatives inevitably lead to outcomes that are inelegant, complicated, and inflexible.

Most commonly, one component will not work with another. Not because of any technical limitation, but because the engineers with seats behind the velvet rope of consumer abstraction haven't gotten around to it. Or worse, their bosses might have told them they're not allowed to. There is not a lot of money in low-margin Chinese gadgets, or home automation software that ships free with your phone operating system, or even the voice assistants that connect to them. But if you weave them into a larger business narrative in which the sponsoring firm makes itself the exclusive clearinghouse for all human commerce and culture between now and the end of the sun's main sequence--well, that's starting to sound interesting. We could get executive support for that. Enough that we can probably put motorized window blind support on the product roadmap and staff it. For our partner firms' blinds, at least. Let's say half an FTE.

This is how business works, and you can either accept it and redirect your energy toward things you will not regret on your deathbed, or you can take it extremely personally and go to great lengths out of pique and a pitiable drive to express a kind of cramped technical mastery. I suspect you know which choice I am compelled to make.

The gadgets themselves are straightforward. So are the software tasks they perform. All of their functionality can be achieved by a competent hobbyist using open source software and commodity electronics, often without starting any fires in the process. But a tremendous number of people are working to polish, upgrade and maintain these various pieces. They're buying the hardware in vast quantities, making it cheap, testing it for reliability and safety. At work, we call this the "build or buy" problem, and it is at least sort of a fun puzzle.

So what have I actually built? What do I recommend? Let's go back to the projector screen.

ESP8266-HTTP-IR-Blaster
-----------------------

To watch a television show in my living room you must activate the projector, the receiver, and the motorized screen. You can plug the screen remote into the projector's 12V trigger port and it will send the "down" code when the projector activates, and the "up" code when it finishes its cooldown sequence. Still, two remotes. Not great.

An "IR blaster" is a device that sends arbitrary infrared remote control commands. It's the kind of thing home theater guys--the kind of guys who name things "blasters"--know how to buy and install and charge too much for. Fortunately, some kind soul has written an `extremely flexible IR blaster application that can run on the commodity ESP8266 <https://github.com/mdhiggins/ESP8266-HTTP-IR-Blaster>`__ chip. The ESP connects to wifi and can be had for about $5. You will need to solder on an IR receiver and wide-angle infrared LED, which will cost a few pennies and is about the simplest soldering project you will find. Load the software. Plug the ESP into a USB charger you've got kicking around. Join its wifi network, tell it about its new wifi family.

.. container:: float wp-block-image size-large

   |image2|

At this point the device will get down to its main task: publishing a diminutive web interface. This can be used to view logs of the IR codes it has recently perceived/had shot at it. And, drawing from those logs, you can tell it which codes to send on your behalf. You can do this through the web interface or a simple HTTP API. Congratulations: you can now send IR commands from the, er, command line.

The project helpfully includes an Amazon Alexa integration. Search for and enable the skill in the Alexa app. Name your devices and the URLs it should contact for each of their functions--volume up, switch input, etc. The idea is that those URLs will point to the ESP, carrying detailed instructions for each IR command. Doing this across the internet (the Alexa app lives out there somewhere) means you'll need to poke a hole in your router and get your home internet connection a reliable DNS name, perhaps by using one or another dynamic DNS service.

To this basic picture, I added a layer of indirection: rather than exposing the ESP to the internet, I expose a Raspberry Pi. That tiny computer runs a bare-bones web server, and when it receives a request at the correct URL it sends a local network request to the ESP for the projector activation command, then waits, then does the same for the stereo receiver. As it wakes, the projector triggers the motorized screen via its attached remote. When I say, "Alexa, turn on the projector," this Rube Goldberg contraption springs to life.

This worked fine, but was not entirely satisfactory. Executing the IR sequence with appropriately emphatic repetition and pauses made for a very slow API response. Alexa would sometimes take offense at this: it exceeded her timeout thresholds and she would report an error, loudly, even though everything was usually working fine. Sunny days or stray balloons (kids love balloons) could interfere with the screen's reception of its IR signal. And the remote connected to the projector--perched atop it, really--would occasionally run down its batteries, and it would then take me ages to realize what had gone wrong. I had previously upgraded the Pi's SimpleHTTPServer-based script to a proper Flask/nginx installation--more on that below--but I recently took two additional steps to improve these deficiencies.

Tasmota
-------

First, I wired another ESP8266 up to the projector's remote control receiver and flashed it with `Tasmota <https://tasmota.github.io/docs/>`__. Tasmota is similar to the IR blaster, providing a friendly web and API interface via the same low-cost wifi microcontroller. It performs a variety of functions. Instead of devoting itself solely to infrared codes, Tasmota controls the ESP's input and output connections in various ways. These are connected to the screen module's pinouts, which are `documented <https://elitescreens.com/static/color_coded_pin_assignments_for_rj45.pdf>`__ in ways that are more-or-less correct (thanks to my friend Matt V for pointing these out to me). The Tasmota ESP can now control the screen without the projector's involvement or any infrared transmission. As an added benefit, when I tell the system to turn itself off, it does so immediately rather than waiting several minutes for the projector to finish cooling down and deactivate its 12V trigger port.

Second, I did the right thing and moved the Flask web server to use a proper work queue. The long-running home theater activation tasks are dumped into a Redis-backed Celery queue, where they are picked up by a worker process and executed at its leisure. This is a lot of complexity for a modest requirement, but it allows the Flask web server to give Alexa the prompt responses she craves.

Homebridge
----------

HomeKit is Apple's home automation framework. It nice enough: baked into iOS devices and compatible with Apple's notion of your family and how to share things with them. I assume it's also relatively privacy preserving, at least compared to its competitors. But Apple's high price point and overall technical fussiness means it's not as well supported by low-end smart home devices.

.. figure:: /static/2022/02/image-1024x648.png
   :figclass: wp-image-3280
   :alt: Homekit accessories displayed via Homebridge

Homebridge helps with this problem. Install it on a Raspberry Pi; search for the brands of home automation garbage you have littering your LAN. Whatever they are, someone has probably written a Homebridge plugin for them. These plugins speak whichever dialect the device (or its cloud API) insists upon, while Homebridge translates to HomeKit-ese. Suddenly, you are not at the mercy of those velvet-rope devs. An army of weird home automation dads has crested the ridge to flank your enemy!

I installed Homebridge and was soon pleased to find a wide variety of dubious LED light bulbs newly accessible in the HomeKit app. Better still: my garage door. Opening that device's highly secured app with gloved hands had been tedious. Now I could ask Siri to do it via my wristwatch. I didn't even have to stop pedaling the cargo bike.

But only when Siri was connected to my wifi network. Apple wants you to have a Homepod or iPad to make any of this stuff work outside of your network. Nuts to that. I added a route to that Flask server that speaks to Homebridge and tells it to open the garage door. I created a routine in the iOS Shortcuts app to probe the very-hard-to-guess URL at which this route lives (Siri knows how to activate shortcuts, too).

This is also when I made the move to Flask and nginx. When an HTTP GET request grants access to part of your home, it's probably time to figure out how to configure TLS encryption. For those aghast at what is still, admittedly, a very replay-attack-susceptible integration: the garage door secures a parking pad that has no roof. So thieves planning a heist can either pull out Bettercap and commence tricking me into contaminating my phone's certificate store to steal this secret URL; or they can climb on top of the neighbors' trash bin and hop over the fence. Either will suffice.

Environmental Monitoring
------------------------

What is the fulcrum about which a father's life revolves? What is the axis of that eternal paternal orrery? It will vary by the man, by the age. The plow, the forge, the agora. The washing machine. For me: the dishwasher. I submit to you that the humble MQTT server belongs on this list.

What is MQTT? It is a pub/sub server technology. Various clients send data to "topics" -- hierarchically-arranged strings that might look like "sensors/home/bedroom/temperature". Clients can subscribe to these topics as well, at whatever level of selectivity they prefer. A script can listen to "sensors/home/bedroom/temperature", for instance, or get the whole home's sensor readings at "sensors/home/#".

MQTT is designed for embedded devices. It avoids the complexity and bandwidth overhead of HTTP. In my experience it's also quite low-latency, though of course my use is not asking very much of it.

I installed the `Mosquitto <https://mosquitto.org/>`__ MQTT server back when I was building a DIY car tracker/ambient display (you can watch that video `here <https://www.youtube.com/watch?v=cThO_1WxNlM>`__). MQTT soon revealed itself to be a bit of a Swiss Army Knife. It's very convenient to be able to shove data at an IP address from anywhere on your network and know that you can go pick it up from wherever you care to. The Tasmota-based screen controller discussed above gets its instructions via MQTT, for instance.

.. container:: float wp-block-image size-large

   |image3|

But a classic MQTT use case is sensor logging. Xiaomi makes a modestly-sized `temperature and humidity sensor <https://www.ebay.com/itm/363680804344?hash=item54ad10adf8:g:BTEAAOSwollh1r~Z>`__ that will run off a coin cell battery for a year or two. It's got Bluetooth as well, though that typically requires a somewhat laborious and battery-draining pairing operation. Luckily, some `brilliant hackers have devised custom firmware for these devices <https://hackaday.com/2020/12/08/exploring-custom-firmware-on-xiaomi-thermometers/>`__. You can install and configure this upgrade from your web browser, wirelessly. Frankly, it seems implausible. But it works.

Among other things, this firmware moves the temperature and humidity measurements into a few spare bytes of the BLE advertising beacon--the Bluetooth chirps that a BLE device makes pretty much all the time. This allows those measurements to be retrieved ambiently by any device that's in the area and paying attention. By examining the hardware MAC address from which the advertisement came, the measurement can be associated with a specific sensor.

I got four of these things, upgraded their firmware, then set about collecting their data. At first, this didn't go great. The Raspberry Pi has Bluetooth hardware, and Homebridge has a plugin for talking to it. In practice, I couldn't make it work.

.. container:: float wp-block-image size-large

   |image4|

Fortunately, I have many drawers brimming with microelectronic garbage. Among these items: some ESP32-based microcontrollers. The successor to the ESP8266, the ESP32 boasts Bluetooth in addition to wifi and, like its sibling, is programmable using the Arduino development environment. It was relatively easy to Frankenstein some `MQTT-client-publishing example code together with some BLE-advertisement-sniffing example code <https://github.com/sbma44/sensor_logging/blob/main/esp32_ble_mqtt_bridge.ino>`__. A small amount of experimentation was necessary to figure out which bytes of each advertisement held the sensor values and how. But before long I had a small chip stashed under the upstairs couch, patiently listening to the household's Bluetooth whispers and relaying a selection of them to my MQTT server.

.. container:: wp-block-columns

   .. raw:: html

      </p>

   .. container:: wp-block-column

      .. raw:: html

         </p>

      .. container:: float wp-block-image size-large is-resized

         |image5|

   .. container:: wp-block-column

      .. raw:: html

         </p>

      | 
      | From there, the Homebridge `MQTTThing <https://github.com/arachnetech/homebridge-mqttthing>`__ plugin allowed me to subscribe to arbitrary topics on my MQTT server and present them to HomeKit as if they were actual devices. Which I suppose they are, really. HomeKit supports temperature/humidity sensors in its spec, so this winds up looking rather seamless.

      I was emboldened by this triumph. I had some `air particulate sensor modules <https://learn.adafruit.com/pm25-air-quality-sensor>`__ in the aforementioned parts drawers. Why not connect them to ESP8266s running the same MQTT client code and send their values up? Why not order `a cheap CO2 sensor <https://emariete.com/en/sensor-co2-mh-z19b/>`__? Why not make a `water level sensor for the Christmas tree <https://twitter.com/tjl/status/1471250414314082305>`__, for fuck's sake?

I did all of this, using lightly revised versions of the above code--all I had to change was the MQTT topic name and the sensor library. Then I wrote a daemon for that same Raspberry Pi--which is hosting all of this stuff, by the way--to subscribe to all of these MQTT topics; take the median value over each 5 minute window; and, once a day, zip up the resulting CSV and put it on S3 (if you are considering doing this, please `take my code <https://github.com/sbma44/sensor_logging/blob/main/cfn-template.py>`__ and make IAM credentials to do this safely).

.. container:: float wp-block-image size-large

   |image6|

.. container:: float wp-block-image size-large

   |image7|

.. container:: float wp-block-image size-large

   |image8|

These logs can be retrieved at my leisure and processed to produce astounding insights like:

- Cooking things is bad for air quality
- Our household CO\ :sub:`2` levels are fine
- My family is wrong, it is not that cold in here and they should put on a sweater

For now, that's it. It is helpful to write all this out and ponder why I did it. It was sort of fun, I think.

But it was also a constrained challenge. It's not like when I built a plotter, or hacked together a router to open the office door at Sunlight. When I started those projects I wasn't sure I would finish them. These home automation projects have had many parts but few unknowns. To need a component and know it's already in an overstuffed drawer somewhere is a sublime pleasure. It's surpassed only by needing a skill and knowing it's already in your hands, your brain.

That I know how to do these things, and, better still, can foresee the pitfalls that might arise, makes them more compatible with parenthood's obligations than more speculative undertakings. Surprisingly large portions of these projects were completed just by thinking about the problem and, perhaps, stealing an occasional look at my phone between pushes of the playground swing or potty training disasters. In the moment, it feels irresistible. I worry that this habit means I am not always as present as I could be, should be. But I know myself well enough to realize that there's no real alternative to accepting my mind's itinerance.

And I have hope that these cold technical obsessions might add up to something human. A man's home is his castle, the saying goes. This is a condo, so its battlements are going to have to be built of software and affordable electronics. Even so, it is impractical to fortify your home in this way. There is no reason for it, except that once you become a father--during a pandemic or otherwise--the importance of everything outside of that home falls away. And anyway it's good to keep busy.

.. |image1| image:: /static/2022/02/image-4-1024x768.png
   :class: wp-image-3284
   :target: /static/2022/02/image-4.png
.. |image2| image:: /static/2022/02/image-2-1024x768.png
   :class: wp-image-3282
   :target: /static/2022/02/image-2.png
.. |image3| image:: /static/2022/02/image-3-1024x768.png
   :class: wp-image-3283
   :target: /static/2022/02/image-3.png
.. |image4| image:: /static/2022/02/image-1-1024x768.png
   :class: wp-image-3281
   :target: /static/2022/02/image-1.png
.. |image5| image:: /static/2022/01/image-4-473x1024.png
   :class: wp-image-3279
   :width: 237px
   :height: 512px
   :target: /static/2022/01/image-4.png
.. |image6| image:: /static/2022/01/image-1-1024x564.png
   :class: wp-image-3276
   :target: /static/2022/01/image-1.png
.. |image7| image:: /static/2022/02/image-8-1024x559.png
   :class: wp-image-3288
   :target: /static/2022/02/image-8.png
.. |image8| image:: /static/2022/02/image-6-1024x618.png
   :class: wp-image-3286
   :target: /static/2022/02/image-6.png
