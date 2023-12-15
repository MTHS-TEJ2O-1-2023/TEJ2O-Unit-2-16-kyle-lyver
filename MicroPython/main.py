"""
Created by: Kyle Lyver
Created on: Dec 2023
This module is a Micro:bit MicroPython program
"""

import radio
from microbit import *
from machine import time_pulse_us

# Create the "flash" animation frames. Can you work out how it's done?
flash = [Image().invert() * (i / 9) for i in range(9, -1, -1)]


# sonar class
from microbit import *
import radio
from machine import time_pulse_us


# choose pins
trig = pin1
echo = pin2

# setup
trig.write_digital(0)
echo.read_digital()
radio.on()
radio.config(group=1)
display.show(Image.HEART)

# infinite loop
while True:
    if button_a.is_pressed():
        # output
        trig.write_digital(1)
        trig.write_digital(0)

        # Measure the echo pulse in miroseconds then convert to seconds
        micros = time_pulse_us(echo, 1)
        t_echo = micros / 1000000

        # Calculate distance in cm
        dist_cm = (t_echo / 2) * 34300
        display.scroll(str(int(dist_cm)))
        if dist_cm <= 10:
            radio.send("Too Close")
        else:
            radio.send("Hi Clara")
    # Read any incoming messages.
    incoming = radio.receive()
    if incoming == "Hi Clara":
        # If there's an incoming "Hi Clara" message display
        display.scroll("Hi Clara")
    if incoming == "Too Close":
        # If there's an incoming "Too Close" message display
        display.scroll("Too Close")
