"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

To learn more about the CLUE and CircuitPython, check this link out:
https://learn.adafruit.com/adafruit-clue/circuitpython

Find example code for CPX on:
https://blog.adafruit.com/2020/02/12/three-fun-sensor-packed-projects-to-try-on-your-clue-adafruitlearningsystem-adafruit-circuitpython-adafruit/
"""

from adafruit_clue import clue
from time import sleep

clue_data = clue.simple_text_display(text_scale=2)
message = "This is a message. "
while True:
    for i in range(len(message)):
        s = message[i + 1:len(message): ]
        clue_data.show()
    # clue_data[0].text = "This is the 1st line"; clue_data[0].color = clue.BLUE
        clue_data[2].text = s + message[ :i]
        clue_data[2].color = clue.AQUA
        sleep(.5)
        clue_data[2].color = clue.BLACK

    # clue_data[2].text = "This is the 3rd line"; clue_data[2].color = clue.BLUE
    # clue_data[3].text = "This is the 4th line"; clue_data[3].color = clue.GOLD
    # clue_data[4].text = "This is the 5th line"; clue_data[4].color = clue.GREEN
    # clue_data[5].text = "This is the 6th line"; clue_data[5].color = clue.MAGENTA
    # clue_data[6].text = "This is the 7th line"; clue_data[6].color = clue.PINK
    # clue_data[7].text = "This is the 8th line"; clue_data[7].color = clue.PURPLE
    # clue_data[8].text = "This is the 9th line"; clue_data[8].color = clue.ORANGE
   
