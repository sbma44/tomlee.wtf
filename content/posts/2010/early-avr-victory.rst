an early AVR victory
####################
:date: 2010-04-12 12:17
:author: admin
:category: Uncategorized
:slug: early-avr-victory
:status: published
:save_as: 2010/04/12/early-avr-victory/index.html
:url: 2010/04/12/early-avr-victory/

For the past few Sundays I've been heading over to HacDC for some intro-to-AVR classes run by Nikolas C. It's something I've wanted to learn for a while. Yesterday I actually got the toolchain working and managed to reprogram the `Game of Life doohickey <http://www.youtube.com/watch?v=F6OMX9pvuwo>`__ that Kriston and I built to do something of my own design. Not anything as cool as the GoL code, admittedly, but still: it's a start. Now the door's open.

.. container::

   .. raw:: html

      <object type="application/x-shockwave-flash" width="400" height="300" data="http://www.flickr.com/apps/video/stewart.swf?v=71377" classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000">

   .. raw:: html

      <embed type="application/x-shockwave-flash" src="http://www.flickr.com/apps/video/stewart.swf?v=71377" bgcolor="#000000" allowfullscreen="true" flashvars="intl_lang=en-us&amp;photo_secret=679df8454f&amp;photo_id=4514855732" height="300" width="400">

   .. raw:: html

      </embed>

   .. raw:: html

      </object>

The AVR is a particular brand of microcontroller ("uCs" for short) -- the same one that powers the Arduino, in fact. I should maybe explain what that means. Microcontrollers aren't very useful by themselves. They need power supplies, things to interact with, and sometimes some supporting components to protect the relatively delicate chip. The Arduino platform adds a bunch of commonly-used circuitry around an AVR chip. It also provides a software environment -- both on the chip and on the computer you use to write code -- that's easier to work with than vanilla AVR code. With Arduino you don't have to worry about binary arithmetic or anything like that -- the metaphors in use are similar to the ones employed when programming a full-sized computer system. The software environment abstracts that stuff away. It makes for a much less daunting experience, particularly for those who have taken an introductory CS class.

As you might expect, Arduino has to make some sacrifices to achieve this ease of use. The AVR has some interesting features that aren't exposed, or aren't fully exposed, by the Arduino environment. Things like interrupts (a useful way to increase the responsiveness of your application and avoid messy loop structures), variable clock speeds (a good way to save power) and sleep modes (another good way to save power) are more easily worked with through direct manipulation of the AVR. Plus there's the fact that, for many applications, an Arduino is overkill. It's physically larger, it has circuitry for features you may not be using, and it costs $15 bucks or so, instead of as little as a dollar or two for an AVR.

The AVR/Arduino system is actually a great example of the power of abstraction: not only does Arduino make AVR development easier, but AVR taken by itself also represented something of a landmark in the simplification of microcontroller development. That's because you can write programs for the AVR in C, instead of the `inscrutable assembly code <http://www.virtualdub.org/blog/pivot/entry.php?id=84>`__ demanded by most other architectures (the PIC family of uC is also popular with hobbyists because it let them program in a flavor of BASIC -- but AVR is supplanting it).

Of course, to a scripting language-oriented CS fraud such as myself, programming in C is still daunting. I haven't really worked with compiled languages since college, and I certainly wasn't any good at them -- there's a `threshold of understanding </2010/01/29/the-stack/>`__ that I didn't cross until years after graduation; I'm still years away from the sophistication on these matters that people like `Alex <http://al3x.net>`__ and `Tim <http://timothyblee.com>`__ possess.

But even they would probably find AVR programming to be a bit bizarre. It mostly involves the manipulation of the specific bits located in specific places in memory. There are helpful macros for this stuff exposed by avr-libc, but figuring them out still involves trudging through `novel-length PDFs <http://www.atmel.com/atmel/acrobat/doc2467.pdf>`__. And since there's obviously no monitor attached to the chip, debugging presents some unique challenges.

My advice to anyone starting down this path would be to find a class, like I did. Having someone who can supply you with a working Makefile counts for a hell of a lot.

For those curious, here's what my code looks like:

| [cc lang="c"]#include
| #include
| #include

| // convenience function
| int min(uint8_t a, uint8_t b)
| {
| return (a }

| int main() {
| DDRB = 0xff; // set data direction on Port B to OUTPUT
| DDRD = 0xff; // set data direction on Port D to OUTPUT

| // x goes from 0 to 15, then loops. the same number of LEDs is illuminated (connected to ports B & D)
| uint8_t x = 0;
| while(1)
| {
| x = (x + 1) % 16;

int y;

| // turn off all LEDs on port B
| PORTB = 0x0;
| for(y=0;y {
| // LEDs are turned on by setting a bit of the port register/byte to 1
| // the \_BV() macro returns a byte with a single bit in the specified position turned to 1
| PORTB \|= \_BV(y);
| }

| // do the same thing, but with port D, and with the top half of the 0..15 range
| PORTD = 0x0;
| for(y=8;y<=x;y++)
| {
| PORTD \|= \_BV(y-8);
| }

| // wait 100 milliseconds
| \_delay_ms(100);
| }

| return 0;
| }[/cc]
