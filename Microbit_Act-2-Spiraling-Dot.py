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
    sleep(200)
    display.clear()
    if x < 4 and y == 0:
        x += 1
    elif( x == 4 and y < 4):
        y += 1
    elif( x > 0 and y == 4):
        x -= 1
    elif( x == 0 and y > 1):
        y -= 1
    elif(x< 3 and y == 1):
        x += 1
    elif(x == 3 and y < 3):
        y +=1
    elif(x > 1 and y == 3):
        x -=1
    elif(x == 1 and y > 2):
        y -= 1
    elif(x < 2  and y == 2):
        x +=1
    else:
        x = 0
        y = 0
            
            
            