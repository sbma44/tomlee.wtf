fortress: shed
##############
:date: 2016-06-19 21:30
:author: admin
:category: Uncategorized
:slug: fortress-shed
:status: published
:save_as: 2016/06/19/fortress-shed/index.html
:url: 2016/06/19/fortress-shed/

I am already failing badly at Iron Blogger. Should I hit publish on that post in *drafts* that I wrote months ago but which might upset my family? Is that valuable self-expression or just narcissism?

Well, we're going to ignore that question for another week, because it turns out I haven't introduced you to my shed.

Some of you may not realize this, but when you get close to completing the process of purchasing a house your realtor will prompt you to issue some ridiculous demands to the seller, as if you have encountered an unusually boring genie. Typically your request will be for a novelty appliance the seller secretly regrets purchasing, or maybe some furniture. It's considered impolite to ask for pets, and requests for children should only be attempted when buying from particularly large families.

Well, Steph and I asked to build a shed. The place came with a parking spot, but we don't have a car or much desire to haul our bikes up a flight of stairs every day. The building is a duplex, so we had to get the neighbors' okay to build a hulking bike receptable. They are kind people and, better still, maybe did not quite realize what they were agreeing to.

We built a mighty shed, thanks in large part to help from Charles, Kriston and Ben. And yes, we used a kit. But that was just the beginning.

|image1|

First, the physical security layer. Some steel pipe, threadlock, wood screws and creative reuse of the "SOLD" sign our realtor repeatedly failed to pick up produced a serviceable indoor bike rack.

|bike rack|

But obviously my heart lies with the electronics.

|led strips and infrared sensor|

`LED strips <http://www.ebay.com/itm/5M-3528-5050-RGB-300-SMD-Flexible-LED-Strip-Light-44key-Remote-12V-Power-Supply-/311428103508?var=610488541894&hash=item48828fbd54:m:mvMj5kRkoi-JS2yUS_AD3Xg>`__ are affordable and already have resistors and adhesive backing in place. All you need to do is supply twelve volts. That happens to be the voltage of most automotive and marine electrical systems, and consequently also a lot of battery technology. But more on that in a second.

The white dome zip-tied to the cross bar is a `passive infrared motion sensor <http://www.ebay.com/itm/HC-SR501-PIR-Motion-sensor-Passive-Infrared-IR-for-Arduino-Fast-USA-seller-/122019991428?hash=item1c68f54f84:g:1m0AAOSwB4NWw9dv>`__. For $3, it works surprisingly well. The cable running up from there goes to a `photoresistor <http://www.ebay.com/itm/20pcs-Photoresistor-5MM-GL5537-LDR-Photo-Resistors-Light-Dependent-Resistor-/321890567952?hash=item4af22c4710:g:EdcAAOSw~bFWGn5w>`__. The apex of the shed's roof is made of translucent plastic to provide illumination during the day. The photoresistor and motion sensor ensure that the lighting system only activates when someone is in the shed and it's dark out.

|arduino/solar controller|

This gadgetry runs down to an Arduino and associated hardware like a MOSFET, a comparator, a trim pot. The Arduino spends most of its life asleep, consuming as little power as possible. But it wakes up a few times a second to see if there's any business it needs to attend to.

Above it is the solar charge controller. That's the gadget that sits between the solar panel and battery and the things you're powering with both. `This is a particularly cheap and crappy controller <http://www.ebay.com/itm/1PC-20A-12V-24V-Solar-Panel-Charge-Controller-Battery-Regulator-Safe-Protection-/231642840036?hash=item35eefd3be4:g:GRMAAOSw3xJVVXT8>`__, but it seems to work fine. It's connected to a sealed lead acid battery on the floor and, on the roof:

|shed roof|

This guy. My eBay history says I paid $50 for a 20 watt panel back in 2014. Honestly, it's hard to find units rated for so little power these days. But this is about enough to keep the battery topped up. The arrangement works well, though on the coldest days of winter I've learned I need to take the battery inside to keep it from freezing and suffering permanent damage.

The final ingredient is `an underwhelming electronic door lock <https://www.amazon.com/GE-45117-Deluxe-Wireless-Alarm/dp/B0014A4JWU/ref=pd_sim_60_1?ie=UTF8&dpID=31Wuglc1e4L&dpSrc=sims&preST=_AC_UL160_SR123%2C160_&refRID=3KQXRA9QXM8X7X21HTKM>`__. It wouldn't survive an intruder's boot heel for more than a stomp or two, but it might make enough ear-splitting noise before then to alert us. I have an old fire alarm bell from `Community Forklift <http://communityforklift.org/>`__ and an `RFID module <http://www.ebay.com/itm/MFRC-522-RC522-RFID-Radiofrequency-IC-Card-Inducing-Sensor-Reader-for-Arduino-BE-/191371999374?hash=item2c8ea8f88e:g:igAAAOxyBjBTRMCs>`__ waiting to be installed. But not every project can be a shed project.

If only it could! But they aren't all winners. Shed telemetry, in particular, has proven tricky:

|temp sensor|

The obvious need for real-time shed temperature readings, published to the internet, can no longer be ignored. But doing this without draining the battery turns out to be tricky. I've got some new `ESP8266 Arduino clones <http://www.ebay.com/itm/1PCS-D1-Mini-NodeMcu-4M-bytes-Lua-WIFI-Development-Board-ESP8266-by-WeMos-TMPP-/222153641786?hash=item33b9638f3a:g:rAwAAOSwMNxXWknT>`__ in hand. If shed telemetry proves to be viable, you'll be among the first to hear about it.

.. |image1| image:: https://c2.staticflickr.com/8/7432/27172377843_68693715d7_d.jpg
   :class: center
.. |bike rack| image:: https://c2.staticflickr.com/8/7101/27749075356_c3f9f09b51_d.jpg
   :class: center
.. |led strips and infrared sensor| image:: https://c2.staticflickr.com/8/7351/27708809331_349b28d807_d.jpg
   :class: center
.. |arduino/solar controller| image:: https://c2.staticflickr.com/8/7612/27172374493_818624abb9_d.jpg
   :class: center
.. |shed roof| image:: https://c2.staticflickr.com/8/7526/27708811911_4e59109788_d.jpg
   :class: center
.. |temp sensor| image:: https://c2.staticflickr.com/8/7349/27682801972_5a45c3971b.jpg
   :class: center
