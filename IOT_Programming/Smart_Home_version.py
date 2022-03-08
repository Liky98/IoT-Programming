""" 라이브러리 import """
import RPi.GPIO as GPIO
from RPLCD.i2c import CharLCD
import time
import Adafruit_DHT
import datetime
from picamera import PiCamera

"""전역변수 설정"""
global control
global dht_type
global bcm_pin
global lcd
camera = PiCamera()

""" SETTING """
def setup() :
    global control
    global dht_type
    global bcm_pin
    global lcd
    control = 0
    GPIO.setmode(GPIO.BCM)
    dht_type = 22 # DHT 타입
    bcm_pin = 23 # 핀 번호
    lcd = CharLCD('PCF8574',0x27)

    GPIO.setup(24, GPIO.IN) #감지센서on
    GPIO.setup(20, GPIO.OUT) #첫번째파란색LED
    GPIO.setup(21, GPIO.OUT) #두번째파란색LED


""" 함수 설정 """
def Button_Click(channel):
    global control
    print('버튼 눌림')
    control = 1

def buzzer() :
    GPIO.setup(25, GPIO.IN)
    GPIO.setup(25, GPIO.OUT)
    GPIO.output(25,True)

def Warring_ON() :
    global control
    GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(12, GPIO.RISING, callback=Button_Click)
    camera.resolution = (1024, 768)
    time.sleep(1)
    camera.capture('camera.jpg')
    buzzer()
    while control == 0 :
        GPIO.output(21, True)
        time.sleep(0.1)
        GPIO.output(21, False)
        time.sleep(0.1)
        GPIO.output(20, True)
        time.sleep(0.1)
        GPIO.output(20, False)
        time.sleep(0.1)

def PIR() :
    if GPIO.input(24) :
        print("Sensor ON")
        return True
    else :
        print("Sensor OFF")
        return False
    time.sleep(0.5)


def time_and_temp() :
    now = datetime.datetime.now()  # 현재 시간
    nowDate = now.strftime('%Y-%m-%d')  # 현재 날짜 Parsing
    nowTime = now.strftime('%H:%M:%S')  # 현재 시각 Parsing
    print(now, nowDate, nowTime)

    humidity, temperature = Adafruit_DHT.read_retry(dht_type, bcm_pin)
    humid = str(round(humidity, 1))  # 소수점 1째자리에서 올림하고 문자화
    temp = str(round(temperature, 1))  # 소수점 1째자리에서 올림하고 문자화
    print(temp, humid)
    time.sleep(1)

    lcd.clear()
    lcd.write_string('Time: ')
    lcd.write_string(nowTime)
    lcd.crlf()

    lcd.write_string('TEMP: ')
    lcd.write_string(temp)
    lcd.write_string('C ')

def name_and_number() :
    lcd.clear()
    lcd.write_string('Name:Lee Ki Hoon')
    lcd.crlf()
    lcd.write_string('No:   201735998')


""" Main """
try:
    while True:
        setup() #초기화
        if PIR() : #감지되었을 때
            name_and_number()
            Warring_ON()
            GPIO.cleanup()
            time.sleep(1)
        else : #미감지일 때
            time_and_temp()
            time.sleep(4)
            GPIO.cleanup()
            time.sleep(0.1)
except KeyboardInterrupt: # 프로그램 종료 시 LCD 화면의 문자를 지움
    lcd.clear()
    GPIO.cleanup()