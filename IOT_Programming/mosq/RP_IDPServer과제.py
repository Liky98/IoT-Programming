""" RP에서 센서를 이용하여 온도와 습도를 파악후, 그 데이터 값을 서버로 보냅니다. """
""" 서버에서 On/OFF값을 받으면 LCD창에 Temp High, Temp Nomarl 을 출력합니다. """
""" 라즈베리파이에서 작동하는 코드입니다. """

import paho.mqtt.client as mqtt
import time
import Adafruit_DHT as dht
import json
import RPi.GPIO as GPIO
from RPLCD.i2c import CharLCD

GPIO.setwarnings(False)

lcd = CharLCD('PCF8574',0x27)
dht_type =22
dht_pin = 23
bcm_pin = 23
intrusion_control = 0

MQTT_HOST = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 60

Topic_RP2PC = "dht/CCL"
Topic_PC2RP = "cmd/CCL"

def on_publish(client, userdata, mid):
    time.sleep(0.1)

def on_connect ( client, userdata , flags, rc ):
    print("Connect with result code" + str (rc))
    client.subscribe(Topic_PC2RP)

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload.decode('utf-8')))
    if msg.payload.decode('utf-8') == "LeeKiHoon_On":
        lcd.clear()
        lcd.write_string("Temp High")

    elif msg.payload.decode('utf-8') == "LeeKiHoon_Off":
        lcd.clear()
        lcd.write_string("Temp Normal")

client = mqtt.Client()
client.on_publish = on_publish
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
client.loop_start()

try:
    while True:
        humidity, temperature = dht.read_retry(dht_type, dht_pin)
        if humidity is not None and temperature is not None:
            data = {'temperature':round(temperature, 1), 'Serial':'LeeKiHoon'}
            client.publish(Topic_RP2PC, str(data))
        else:
            time.sleep(0.1)
except keyboardInterrupt:
    time.sleep(0.1)
