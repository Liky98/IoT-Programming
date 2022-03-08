import paho.mqtt.client as mqtt
import time
import Adafruit_DHT as dht
import json
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
dht_type =22
dht_pin = 23
# Define Variables
MQTT_HOST = " 192.9.44.252" #자신의 pc ip
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 60
MQTT_TOPIC = "dht/CCL"
# Define on_publish event function

def on_publish(client, userdata, mid):
    print ("Message Published...")

def on_connect ( client, userdata , flags, rc ):
    print("Connect with result code" + str (rc))
    client.subscribe("dht/CCL")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload.decode('utf-8')))
    if msg.payload.decode('utf-8') == "on":
        GPIO.output(16, True)
    elif msg.payload.decode('utf-8') == "off":
        GPIO.output(16, False)

# Initiate MQTT Client
client = mqtt.Client()
# Register publish callback function
client.on_publish = on_publish
client.on_connect = on_connect
client.on_message = on_message

# Connect with MQTT Broker
client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
client.loop_start()
try:
    while True:
        humidity, temperature = dht.read_retry(dht_type, dht_pin)
        if humidity is not None and temperature is not None:
            data = {'temperature':round(temperature, 1), 'humidity' : round(humidity, 1)}
            client.publish(MQTT_TOPIC, str(data))
            print('Published. Sleeping ...')
        else:
            print('Failed to get reading. Skipping ...')
except keyboardInterrupt:
    GPIO.cleanup()
