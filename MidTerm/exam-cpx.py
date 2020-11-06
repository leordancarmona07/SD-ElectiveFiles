"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Getting started with CPX and CircuitPython intro on:
https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library

Find example code for CPX on:
https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples
"""

# import CPX library
from adafruit_circuitplayground import cp
import time
cp.pixels.brightness = 1
neopix = 0
temp = 1
while True:
    neopix -= 1
    temp -= 1
    if neopix < 0:
        neopix = 9
    if temp < 0:
        temp = 9
    
    if neopix == 9 :
        cp.pixels[temp] = (255,255,255)
        cp.pixels[neopix]= (255,255,255)
        time.sleep(.5)
        cp.pixels[temp] = 0
        cp.pixels[neopix] = 0
    elif neopix == 4:
        cp.pixels[temp] = (255,255,255)
        cp.pixels[neopix]= (255,255,255)
        time.sleep(.5)
        cp.pixels[temp] = 0
        cp.pixels[neopix] = 0
    else:
        cp.pixels[neopix]= (255,255,255)
        time.sleep(.5)
        cp.pixels[neopix] = 0
        
