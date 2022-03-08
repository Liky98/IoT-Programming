""" RP에서 온도를 받고, ON/OFF 판별 후, 다시 서버로 전달하는 코드 """
""" PC(Windows) 에서 작동하는 코드입니다. """

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time

normal_temp = 26.0
MQTT_Broker = "test.mosquitto.org"
Topic_RP2PC = "/dht/CCL"
Topic_PC2RP = "/cmd/CCL"

def on_connect (client, userdata , flags, rc ):
    print("Connect with result code" + str (rc))
    client.subscribe(Topic_RP2PC)

def on_message ( client, userdata , msg ) :
    x = str(msg.payload.decode('utf-8'))
    print(msg.topic + " " + x)
    y = eval(x)
    if (y['Serial']=='LeeKiHoon'):
        if y["temperature"] > normal_temp:
            publish.single(Topic_PC2RP, "LeeKiHoon_On", hostname = MQTT_Broker)
        elif y["temperature"] <= normal_temp:
            publish.single(Topic_PC2RP, "LeeKiHoon_Off", hostname = MQTT_Broker)

def on_publish(client, userdata, mid):
    print("message publish..")

def on_disconnect(client, userdata, rc):
    print("Disconnected")
try:
    client = mqtt.Client ()
    client.on_connect = on_connect
    client.connect(MQTT_Broker, 1883, 60)
    client.on_message = on_message
    client.on_publish = on_publish
    client.on_disconnect = on_disconnect
    client.loop_forever()
except :
    time.sleep(1)