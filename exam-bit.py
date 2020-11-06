"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Get started with micro:bit and MicroPython on:
https://microbit-micropython.readthedocs.io/en/latest/.
"""
from microbit import *
import time

while True:
    for i in range(9):
        time.sleep(.5)
        if i == 0:
            display.show(Image("00000:00000:00000:00000:90000"))
        elif i == 1:
            display.show(Image("00000:00000:00000:90000:09000"))
        elif i == 2:
            display.show(Image("00000:00000:90000:09000:00900"))
        elif i == 3:
            display.show(Image("00000:90000:09000:00900:00090"))
        elif i == 4:
            display.show(Image("90000:09000:00900:00090:00009"))
        elif i == 5:
            display.show(Image("09000:00900:00090:00009:00000"))
        elif i == 6:
            display.show(Image("00900:00090:00009:00000:00000"))
        elif i == 7:
            display.show(Image("00090:00009:00000:00000:00000"))
        else:
            display.show(Image("00009:00000:00000:00000:00000"))
       

