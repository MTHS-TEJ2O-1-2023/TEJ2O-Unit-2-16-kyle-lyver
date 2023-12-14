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

radio.on()
display.show(Image.HAPPY)
# Event loop.
while True:
    # Button A sends a "flash" message.
    if button_a.was_pressed():
        radio.send("flash")
    # Read any incoming messages.
    incoming = radio.receive()
    if incoming == "flash":
        # If there's an incoming "flash" message display
        display.show(flash, delay=100, wait=False)
        # Randomly re-broadcast the flash message after a
        # slight delay.
        if random.randint(0, 9) == 0:
            sleep(500)
            radio.send("flash")
