well, that was much harder than it needed to be
###############################################
:date: 2011-12-21 00:16
:author: admin
:category: Uncategorized
:slug: well-that-was-much-harder-than-it-needed-to-be
:status: published
:save_as: 2011/12/21/well-that-was-much-harder-than-it-needed-to-be/index.html
:url: 2011/12/21/well-that-was-much-harder-than-it-needed-to-be/

I just spent some time banging my head against this problem; let me save people wandering in from Google similar trouble.

So: you're trying to use pySerial to speak to your Arduino. It's not working. Or sometimes it is, but only when you have the Arduino Serial Monitor window open! This makes no sense.

Here's the deal: the Arduino's fancy "you can flash new programs onto me without pressing my reset button!" functionality works by resetting the damn thing whenever a new serial connection is made. With the serial monitor open, the connection's already open, so no reset happens and your script might actually work. When the monitor is closed, the Arduino resets when Python connects to it -- and the Arduino might still be busy booting up when your script begins shoving bits across the link.

So! You can disable this auto-reset behavior (you'll have to ask the Arduino people about that), but it seems simplest to just make your python script long-running and wait patiently for a beat or two after opening the serial link. Here's a dead-simple example:

| [cc lang="python"]import serial, sys
| from time import sleep

| SERIAL_PORT = '/dev/tty.usbmodem621'
| SERIAL_RATE = 9600

| ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
| sleep(2)
| val = int(sys.argv[1])
| ser.write(chr(val))[/cc]

Here's the Arduino sketch. It just blinks the LED on pin 13 however many times you sent as a byte (I'm working on sending binary-ish data over the serial link; hence the use of raw byte values):

[cc lang="java"]byte inByte = 0;

| void setup()
| {
| Serial.begin(9600);
| pinMode(13, OUTPUT);
| }

| void loop()
| {
| if (Serial.available() > 0) {
| inByte = Serial.read();

| for(int i=0;i digitalWrite(13, HIGH);
| delay(500);
| digitalWrite(13, LOW);
| delay(500);
| }
| }
| }
| [/cc]

There! That was irritating.
