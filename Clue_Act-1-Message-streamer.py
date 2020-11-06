"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

To learn more about the CLUE and CircuitPython, check this link out:
https://learn.adafruit.com/adafruit-clue/circuitpython

Find example code for CPX on:
https://blog.adafruit.com/2020/02/12/three-fun-sensor-packed-projects-to-try-on-your-clue-adafruitlearningsystem-adafruit-circuitpython-adafruit/
"""

from adafruit_clue import clue
import time

clue_data = clue.simple_text_display(title="Message Streamer", title_color= (255,0,0), text_scale= 2)
toLeftText = "Hello Left, this is from Right! "
toRightText = "Hello Right, this is from Left! "
blinkingText = "Hey! I'm Blinking!"
ctr = 0
ctr1 = 0
ctr2 = 0
while True:
    
    if (ctr1 == len(toRightText)):
        ctr1 = 0
    else:
        slice1 = toRightText[-ctr1-1: len(toRightText): ]
        clue_data[3].text =  slice1 + toRightText[ :-ctr1]
        clue_data[3].color =  clue.WHITE

    if (ctr == len(toLeftText)):
        ctr = 0
    else:
        slice1 = toLeftText[ctr + 1:len(toLeftText): ]
        clue_data[1].text =  slice1 + toLeftText[ :ctr]
        clue_data[1].color =  clue.YELLOW

       
        
    clue_data[5].text = blinkingText
    if ctr2 % 2 != 0 :
        clue_data[5].color = clue.BLACK
    else:
        clue_data[5].color = clue.SKY
    ctr2 += 1
    ctr += 1
    ctr1 += 1
    clue_data.show()
    
    
    
    

    
