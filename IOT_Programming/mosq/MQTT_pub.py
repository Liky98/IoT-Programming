import paho.mqtt.client as mqtt

IP = "192.9.45.252"
Topic = "/PC2RP"

Message = "MQTT action"

mqtt = mqtt.Client() #Mqtt Client 오브젝트 생성
mqtt.connect(IP, 1883) #MQTT 서버에 연결
mqtt.publish(Topic, Message) #토픽과 메세지 발행
#mqtt.publish(Topic, "mosquitto mqtt Message")
mqtt.loop(2) #timeout 2sec.