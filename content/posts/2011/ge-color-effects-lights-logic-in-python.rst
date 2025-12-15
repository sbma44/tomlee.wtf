GE Color Effects Lights logic in Python
#######################################
:date: 2011-12-22 19:36
:author: admin
:category: Uncategorized
:slug: ge-color-effects-lights-logic-in-python
:status: published
:save_as: 2011/12/22/ge-color-effects-lights-logic-in-python/index.html
:url: 2011/12/22/ge-color-effects-lights-logic-in-python/
:private: true

I've been playing with `these holiday lights <http://www.amazon.com/Color-Effects-Changing-Remote-Control/dp/B004A354B8>`__ recently. They're very neat: each bulb has RGB LEDs embedded in it and is individually addressable (albeit with only 4 bits of resolution per color channel). Some wonderfully talented folks have `reverse-engineered <http://www.deepdarc.com/2010/11/27/hacking-christmas-lights/>`__ the protocol that the light controller uses; `others have written Arduino code <http://scottrharris.blogspot.com/2010/12/controlling-ge-color-effects-lights.html>`__ making it possible to snip the light's control line, connect it to an Arduino, and begin programming your own animations. Still others are doing various `neat and unusual things <http://blog.jgc.org/2011/11/turning-ge-color-effects-g-35-christmas.html>`__ with the result. Personally, I just want to have some interesting light displays for New Year's.

These other folks' work makes this possible, but not as convenient as it could be: developing new animation routines on the Arduino is a pain in the butt. To do so you write your code in the Arduino's irritating development environment, then flash it to the chip and hope that everything worked right. There's a small risk of damaging the lights, and a large chance of things going wrong.

So! I wrote some bridge code that moves the light control logic into Python, which can run and be manipulated on a regular ol' computer. The state of the lights is then sent to the Arduino many times per second (though not as many as I'd like -- still, only about 1FPS slower than the string's theoretical max) and the Arduino dutifully updates the state of the lights. This should make development of animations easier, and make it simpler to trigger or modulate them in response to network events or other things that the computer can detect.

`If you have any use for this code, you can find it here <https://github.com/sbma44/cheerlights-arduino-python>`__. For me, there are two challenges remaining: creating some interesting animations, and connecting a second string to the Arduino.

This latter issue is a bigger problem than you might think: the lights' address space is only 6 bits -- too small to simply connect the two strings together and retain the ability to control individual lights (bulbs can share addresses, but I'd rather not do that). So the two strings need to be treated as individual entities. That's easy enough on the Arduino side. But the Arduino is going to live at one end of this double-string, not in the middle. That means that the signal to the far string will have to be transmitted along the length of the near string. This is too much distance for a fast serial connection to traverse without being spread out into illegibility.

The solution, I'm told, is to shift the serial signal to RS-422, a higher-speed and more ethernet-like standard, then back to serial at the light string (it will travel along a twisted pair of conductors that I'll run along the already-too-heavy first string). I have the chips to do this, and it all \*looks\* pretty simple. Fingers crossed...
