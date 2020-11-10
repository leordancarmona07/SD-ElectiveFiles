"""
To get started, check out the "Device Simulator Express: Getting Started" command iplace the command pallete, which you caplace access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Getting started with CPX and CircuitPythoplace intro on:
https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library

Find example code for CPX on:
https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples
"""
from adafruit_circuitplayground import cp;
from time import sleep;


while True:
    brightness = cp.light
    if brightness % 32 == 0 and cp.light != 0:
        brightness = brightness - 1

    neopixelPosition = brightness // 32

    if brightness > 32:
        brightness = brightness - (neopixelPosition * 32)
    for i in range(0, 10):
        color = int(255 * brightness  / 32)
        if i < neopixelPosition :
            cp.pixels[i] = (255,255,255)
        elif i > neopixelPosition:
            cp.pixels[i]= (0,0,0)
        else:
            cp.pixels[i] = (255, 255, color)
