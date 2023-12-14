"""
Created by: Kyle Lyver
Created on: Dec 2023
This module is a Micro:bit MicroPython program
"""

# A micro:bit Firefly.

# By Nicholas H.Tollervey. Released to the public domain.
import radio
import random
from microbit import display, Image, button_a, sleep

# Create the "flash" animation frames. Can you work out how it's done?
flash = [Image().invert() * (i / 9) for i in range(9, -1, -1)]


# sonar class
class HCSR04:
    # this class abstracts out the functionality of the HC-SR04 and
    #   returns distance in mm
    # Trig: pin 1
    # Echo: pin 2
    # choose pins
    trig = pin1
    echo = pin2

    def __init__(self, tpin=pin1, epin=pin2, spin=pin13):
        self.trigger_pin = tpin
        self.echo_pin = epin
        self.sclk_pin = spin

    def distance_mm(self):
        spi.init(
            baudrate=125000,
            sclk=self.sclk_pin,
            mosi=self.trigger_pin,
            miso=self.echo_pin,
        )
        pre = 0
        post = 0
        k = -1
        length = 500
        resp = bytearray(length)
        resp[0] = 0xFF
        spi.write_readinto(resp, resp)
        # find first non zero value
        try:
            i, value = next((ind, v) for ind, v in enumerate(resp) if v)
        except StopIteration:
            i = -1
        if i > 0:
            pre = bin(value).count("1")
            # find first non full high value afterwards
            try:
                k, value = next(
                    (ind, v)
                    for ind, v in enumerate(resp[i : length - 2])
                    if resp[i + ind + 1] == 0
                )
                post = bin(value).count("1") if k else 0
                k = k + i
            except StopIteration:
                i = -1
        dist = -1 if i < 0 else round(((pre + (k - i) * 8.0 + post) * 8 * 0.172) / 2)
        return dist


sonar = HCSR04()

radio.on()
display.show(Image.HAPPY)
# Event loop.
while True:
    # Button A sends a "flash" message.
    if button_a.was_pressed():
        if sonar.distance_mm <= 10:
            radio.send("Too Close")
        else:
            radio.send("Hi Clara")
    # Read any incoming messages.
    incoming = radio.receive()
    if incoming == "Hi clara":
        # If there's an incoming "Hi Clara" message display
        display.scroll("Hi clara")
    if incoming == "Too Close":
        # If there's an incoming "Too Close" message display
        display.scroll("Too Close")
