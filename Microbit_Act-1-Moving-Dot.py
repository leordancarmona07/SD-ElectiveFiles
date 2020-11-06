"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Get started with micro:bit and MicroPython on:
https://microbit-micropython.readthedocs.io/en/latest/.
"""

import microbit
from microbit import *

x = 0
y = 0

while True:
    display.set_pixel(x, y, 9)
    sleep(500)
    display.clear()
    x += 1
    if x > 4:
        x = 0
        y += 1
        if y > 4:
            y = 0

        