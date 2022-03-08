import paho.mqtt.client as mqtt

IP = "192.9.45.252"
Topic = "/RP-RP-PC"

Port = 1883
Keepalive_interval = 60


# 서버로부터 CONNTACK 응답을 받을 때 호출되는 콜백
def on_connect(client, userdata, flags, rc):
    global Topic
    #print("Connected with result code " + str(rc))
    client.subscribe(Topic)  # TOPIC구독 ”IoT-P"


# 서버로부터 publish message를 받을 때 호출되는 콜백
def on_message(client, userdata, msg):
    #print(msg.topic + " " + str(msg.payload))  # 토픽과 메세지를 출력한다.
    print(str(msg.payload))

client = mqtt.Client()  # client 오브젝트 생성
client.on_connect = on_connect  # 콜백설정
client.on_message = on_message  # 콜백설정
client.connect(IP, 1883, 60)  # 라즈베리파이3 MQTT 브로커에 연결 #IP,Port,Keepalive_interval
client.loop_forever()

