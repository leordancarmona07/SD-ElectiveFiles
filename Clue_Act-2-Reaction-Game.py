"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

To learn more about the CLUE and CircuitPython, check this link out:
https://learn.adafruit.com/adafruit-clue/circuitpython

Find example code for CPX on:
https://blog.adafruit.com/2020/02/12/three-fun-sensor-packed-projects-to-try-on-your-clue-adafruitlearningsystem-adafruit-circuitpython-adafruit/
"""

from adafruit_clue import clue
from random import randint
from time import sleep

clue_data = clue.simple_text_display(title="Reaction Game",title_color=clue.GOLD, text_scale=2)
a_score = 0
b_score = 0
while True:
    clue_data.show()
    my_range = 3
    while my_range != 0:
        clue_data[1].color = clue.GREEN
        clue_data[2].color = clue.WHITE
        clue_data[3].color = clue.WHITE
        clue_data[4].color = clue.SKY
        clue_data[5].color = clue.SKY
        clue_data[6].color = clue.RED
        clue_data[1].text = 'Instructions:'
        clue_data[2].text = 'Player A presses A'
        clue_data[3].text = 'Player B presses B'
        clue_data[4].text = 'Press if the number'
        clue_data[5].text = 'is divisible by 2'
        clue_data[6].text = f'starts in : {my_range}'
        sleep(1)
        my_range -= 1
        if my_range == 0:
            clue_data[1].color = clue.BLACK
            clue_data[2].color = clue.BLACK
            clue_data[3].color = clue.BLACK
            clue_data[4].color = clue.BLACK
            clue_data[5].color = clue.BLACK
            clue_data[6].color = clue.BLACK
            my_range = 0
    
    while my_range == 0:
        clue_data[2].color = clue.BLACK
        clue_data[3].color = clue.BLACK
        clue_data[4].color = clue.GREEN
        clue_data[5].color = clue.SKY
        clue_data[6].color = clue.BLACK
        clue_data[4].text = f'Player A : {a_score}'
        clue_data[5].text = f'Player B : {b_score}'
        randomInt = randint(0,100)
                
        if a_score == 3 :
            clue_data[1].color = clue.RED
            clue_data[1].text = "Player A wins"
        elif b_score == 3:
            clue_data[1].color = clue.RED
            clue_data[1].text = "Player B wins"
        else:
            ctr = 0
            while ctr < 40:
                ctr += 1
                clue_data[1].color = clue.SKY
                clue_data[1].text = "         "+ str(randomInt)
                if clue.button_a:
                    if randomInt % 2 == 0:
                        a_score += 1
                    else:
                        a_score -= 1
                    break
                elif clue.button_b:
                    if randomInt % 2 == 0:
                        b_score += 1
                    else:
                        b_score -= 1
                    break
            clue_data[1].color = clue.BLACK
                    
                    


