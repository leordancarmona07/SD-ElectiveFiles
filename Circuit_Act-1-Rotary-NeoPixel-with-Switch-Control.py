"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Getting started with CPX and CircuitPython intro on:
https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library

Find example code for CPX on:
https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples
"""

# import CPX library
import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = 1
neopix = 9
while True:
    cp.red_led = 1
    print("switch is ", cp.switch)
    print(neopix)
    cp.pixels[neopix]= (0,0,255)
    time.sleep(.5)
    cp.pixels[neopix] = 0
    if cp.switch:
        neopix += 1
        if neopix > 9:
            neopix = 0
    else:
        neopix -=1
        if neopix < 0 :
            neopix = 9

    
    
