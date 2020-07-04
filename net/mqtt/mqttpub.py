import paho.mqtt.client as mqtt #import the client1
import time
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message retain flag=",message.retain)
    print("\n")
########################################
broker_address="192.168.1.55"
client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to callback
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
client.subscribe("s/t")
while True:
    client.publish("s/q",str(input()))
time.sleep(10)
client.publish("s/q", "ON")
time.sleep(120) # wait
client.loop_stop() #stop the loop
