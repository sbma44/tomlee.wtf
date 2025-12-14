adding Airplay to a Sonos with Raspberry Pi
###########################################
:date: 2013-06-22 20:05
:author: admin
:category: Uncategorized
:slug: adding-airplay-to-a-sonos
:status: published
:save_as: 2013/06/22/adding-airplay-to-a-sonos/index.html
:url: 2013/06/22/adding-airplay-to-a-sonos/

I mostly like my Sonos system. The downsides: I had a controller die on me out of warranty; it's a bit pricey; and it doesn't have Airplay support. This last one, at least, turns out to be fixable, thanks to a few open source projects and the Raspberry Pi.

The ingredients:

- the `Shairport project <https://github.com/abrasive/shairport>`__, for providing Airplay
- the `SoCo <https://github.com/SoCo/SoCo>`__ project, for controlling the Sonos

This last one is important for making the Sonos start listening to its line-in when Airplay begins to be used.

Getting your Raspberry Pi on your wifi network is a bit of a pain. You'll need to compile Shairport's dependencies and install some modules from CPAN. SoCo's setup.py doesn't leave you with a working installation, but the codebase is fine if you use it directly.

With all the pieces in place, you just need a script like this to switch the Sonos:

.. raw:: html

   <p>

.. raw:: html

   <code>

| import re, sys
| from soco import SonosDiscovery, SoCo

.. raw:: html

   </p>

| def main():
| sd = SonosDiscovery()
| possible_matches = sd.get_speaker_ips()
| speaker_info = {}
| for ip in possible_matches:
| s = SoCo(ip)
| try:
| speaker_info[ip] = s.get_speaker_info()
| except Exception, e:
| speaker_info[ip] = {}

| for (ip, speaker) in speaker_info.items():
| if re.search(sys.argv[1], speaker.get('zone_name', ''), re.I) is not None:
| s = SoCo(ip)
| s.switch_to_line_in()
| s.play()

| if \__name\_\_ == '\__main\_\_':
| main()

and then to start the Shairport daemon like so:

``perl /home/pi/sonos-airplay/shairport.pl -d -w /home/pi/sonos-airplay/shairport.pid -l 100 --apname="Sonos" --play_prog="/home/pi/.virtualenvs/sonos/bin/python /home/pi/sonos-airplay/set_line_in.py bedroom"``

This will call the *set_line_in.py* script every time a new Airplay client connects.

For good measure, here's the /etc/init.d/shairport startup file I'm using:

| ``#!/bin/sh``
| ``# /etc/init.d/shairport``
| ``PIUSER='pi'``
| ``case "$1" in``
| ``start)``
| ``/home/pi/sonos-airplay/start_shairport.sh``
| ``echo "Starting Shairport Server for $PIUSER "``
| ``;;``
| ``stop)``
| :literal:`kill \`cat /home/pi/sonos-airplay/shairport.pid\``
| ``echo "Shairport Server stopped"``
| ``;;``
| ``*)``
| ``echo "Usage: /etc/init.d/shairport {start|stop}"``
| ``exit 1``
| ``;;``
| ``esac``
| ``exit 0``

It all works pretty well! The only real downside is the volume: Airplay's pretty quiet. I should be able to automate the volume adjustment on the Sonos -- SoCo exposes that functionality as well, and Shairport can call scripts upon client disconnect, too, to reset the volume. But I haven't had a chance to write that yet.

Anyway, if folks start wandering in from Google and find this useful or desirable, let me know. I could probably make this all a bit more reusable without a ton of trouble (distributing a Raspberry Pi filesystem image might be the easiest thing, really).

**UPDATE:** Hmm. Subsequent investigation of the Sonos's line-in level adjustment capabilities reveals that the SoCo portion of this might be unnecessary: there is indeed some capacity for adjusting amplification on the line-in. Better still, there's some sort of line-in activity detection! I think I might stick with my script anyway: I have a Sonos unit on the porch that's usually powered off; I'll probably just adjust the script's logic to pipe the line-in to it if it's activated. Still, for most users the Shairport stuff should be sufficient.
