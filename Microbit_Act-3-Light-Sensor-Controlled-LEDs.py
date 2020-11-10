"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Get started with micro:bit and MicroPython on:
https://microbit-micropython.readthedocs.io/en/latest/.
"""

from microbit import *

while True:
    light = display.read_light_level()
    x = 0
    y = 4
    if light % 10 == 0 and light != 0:
        light = light - 1
    
    if light > 0 and light < 10:
        display.set_pixel(x,y,light)
    elif light > 10 and light < 20:
        x = 1
        light = light - 10
    elif light > 20 and light < 30:
        x = 2
        light = light - 20
    elif light > 30 and light < 40:
        x = 3
        light = light - 30
    elif light > 40 and light < 50:
        x = 4
        light = light - 40
    elif light > 50 and light < 60:
        x = 0
        y = 3
        light = light - 50
    elif light > 60 and light < 70:
        x = 1
        y = 3
        light = light - 60
    elif light > 70 and light < 80:
        x = 2
        y = 3
        light = light - 70
    elif light > 80 and light < 90:
        x = 3
        y = 3
        light = light - 80
    elif light > 90 and light < 100:
        x = 4
        y = 3
        light = light - 90
    elif light > 100 and light < 110:
        x = 0
        y = 2
        light = light - 100
    elif light > 110 and light < 120:
        x = 1
        y = 2
        light = light - 110
    elif light > 120 and light < 130:
        x = 2
        y = 2
        light = light - 120
    elif light > 130 and light < 140:
        x = 3
        y = 2
        light = light - 130
    elif light > 140 and light < 150:
        x = 4
        y = 2
        light = light - 140
    elif light > 150 and light < 160:
        x = 0
        y = 1
        light = light - 150
    elif light > 160 and light < 170:
        x = 1
        y = 1
        light = light - 160
    elif light > 170 and light < 180:
        x = 2
        y = 1
        light = light - 170
    elif light > 180 and light < 190:
        x = 3
        y = 1
        light = light - 180
    elif light > 190 and light < 200:
        x = 4
        y = 1
        light = light - 190
    elif light > 20 and light < 210:
        x = 0
        y = 0
        light = light - 200
    elif light > 210 and light < 220:
        x = 1
        y = 0
        light = light - 210
    elif light > 220 and light < 230:
        x = 2
        y = 0
        light = light - 220
    elif light > 230 and light < 240:
        x = 3
        y = 0
        light = light - 230
    elif light > 240 and light < 250:
        x = 4
        y = 0
        light = light - 240
    elif light > 250 and light <= 255:
        light = 9
    else:
        display.clear()
        
    display.set_pixel(x,y,light)


        

    
   
 
    


    
