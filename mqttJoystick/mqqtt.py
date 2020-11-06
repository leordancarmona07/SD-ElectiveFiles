"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.
Get started with micro:bit and MicroPython on:
https://microbit-micropython.readthedocs.io/en/latest/.
"""

from microbit import *
import paho.mqtt.client as mqtt
North = Image.ARROW_N
East = Image.ARROW_E
West = Image.ARROW_W
South = Image.ARROW_S
NorthEast = Image.ARROW_NE
NorthWest = Image.ARROW_NW
SouthEast = Image.ARROW_SE
SouthWest = Image.ARROW_SW

OFF = Image("00000:00000:00000:00000:00000")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe("mousemove")
        display.show(Image.YES)

def on_message(client, userdata, msg):
    if msg.payload.decode() == "N":
        display.show(North)
    elif msg.payload.decode() == "NE":
        display.show(NorthEast)
    elif msg.payload.decode() == "E":
        display.show(East)
    elif msg.payload.decode() == "SE":
        display.show(SouthEast)
    elif msg.payload.decode() == "S":
        display.show(South)
    elif msg.payload.decode() == "SW":
        display.show(SouthWest)
    elif msg.payload.decode() == "W":
        display.show(West)
    elif msg.payload.decode() == "NW":
        display.show(NorthWest)
    else:
        display.show(OFF)

        

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

client.loop_forever()

# Broker for online client: https://iamelijah2016.github.io/
# wss://mqtt.eclipse.org:443/mqtt
# wss://test.mosquitto.org:8081/mqtt