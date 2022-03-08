""" RP에서 센서를 이용하여 온도와 습도를 파악후, 그 데이터 값을 서버로 보냅니다. """
""" 서버에서 On/OFF값을 받으면 LCD창에 Temp High, Temp Nomarl 을 출력합니다. """
""" 라즈베리파이에서 작동하는 코드입니다. """

import paho.mqtt.client as mqtt
import time
import Adafruit_DHT as dht
import json
import RPi.GPIO as GPIO
from RPLCD.i2c import CharLCD
# -*- coding: utf-8 -*
import RPi.GPIO as GPIO
import time
import speech_recognition as sr

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

r = sr.Recognizer()
mic = sr.Microphone()
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)

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


lcd.clear()
lcd.write_string("201735999")
lcd.crlf()
lcd.write_string("LeeKiHoon")

client = mqtt.Client()
client.on_publish = on_publish
client.on_connect = on_connect
client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
client.on_message = on_message
client.loop_start()
time.sleep(2)

try:
    print("A moment of silence, please...")
    with mic as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))

    while True:
        try :
            with mic as source:
                print("Say something!")
                audio = r.listen(source)
            gcSTT = r.recognize_google(audio, language = 'ko')
            print("Google cloud Speech Recognition thinks you said : " + gcSTT)

            if "불 켜" in gcSTT:
                humidity, temperature = dht.read_retry(dht_type, dht_pin)
                if humidity is not None and temperature is not None:
                    data = {'temperature': round(temperature, 1), 'Serial': 'LeeKiHoon'}
                    client.publish(Topic_RP2PC, str(data))
                    time.sleep(1)

                else:
                    time.sleep(0.1)
                GPIO.output(16,True)

            elif "불 꺼" in gcSTT:
                lcd.clear()
                lcd.write_string("201735999")
                lcd.crlf()
                lcd.write_string("LeeKiHoon")

                GPIO.output(16,False)
        except sr.UnknownValueError:
            print("Google Cloud Speech could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Cloud Speech service; {0}".format(e))
        except :
            time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()

