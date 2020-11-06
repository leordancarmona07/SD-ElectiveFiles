from adafruit_circuitplayground import cp
import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    if rc == 0:
        cp.red_led = True
        client.subscribe("leordan-switch")
        

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload)
    
    if payload["checker"] == "true":
        #here I coverted the string value of payload["pixel"] into int to make it a real index
        cp.pixels[int(payload["pixel"])] = (255, 255, 255)
    else:
        cp.pixels[int(payload["pixel"])] = (0, 0, 0)

cp.red_led = False

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

client.loop_forever()

# Broker for online client: https://iamelijah2016.github.io/
# wss://mqtt.eclipse.org:443/mqtt
# wss://test.mosquitto.org:8081/mqtt