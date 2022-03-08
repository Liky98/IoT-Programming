import RPi.GPIO as GPIO
from RPLCD.i2c import CharLCD
import time

""" SETTING """
control = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

""" LED Sensor """
def LED_RED_ON() :
    GPIO.output(16, True)

def LED_RED_OFF() :
    GPIO.output(16, False)

def LED_GREEN_ON() :
    GPIO.output(20, True)

def LED_GREEN_OFF() :
    GPIO.output(20, False)

def LED_BLUE_ON() :
    GPIO.output(21, True)

def LED_BLUE_OFF():
    GPIO.output(21, False)

def LED_PWM_ON() : #색별로 가능하게
    pwm_red = GPIO.PWM(16, 500)  # (pin_num, frequency(hz))
    pwm_green = GPIO.PWM(20, 500)
    pwm_blue = GPIO.PWM(21, 500)
    if GPIO.input(16):
        pwm_red.start(0)
    if GPIO.input(20):
        pwm_green.start(0)
    if GPIO.input(21) :
        pwm_blue.start(0)

    for i in range(101):  # 출력을 0부터 100까지
        if (i == 100):
            i = 0
        pwm_red.ChangeDutyCycle(i)  # 출력 변경
        pwm_green.ChangeDutyCycle(i)
        pwm_blue.ChangeDutyCycle(i)
        time.sleep(0.02)


#def BLINK() :


# 스위치 눌렸을 때 콜백함수
def switchPressed(channel):
    global control
    print('비상상황 해제')
    control = 0


# 부저음 함수
def buzz():  # 부저를 울리는 함수
    global control
    maxTime = time.time() + 10
    pitch = 1000  # 주파수
    duration = 0.1  # 울리는 시간
    period = 1.0 / pitch  # 소리의 진동을 만들어 내기 위한 간격
    delay = period / 2  # 간격의 절반을 delay로 설정
    cycles = int(duration * pitch)
    for i in range(cycles):
        GPIO.output(25, True)
        time.sleep(delay)
        GPIO.output(25, False)
        time.sleep(delay)
        if control == 0 or time.time() > maxTime:
            break


try:
    while True :


except KeyboardInterrupt:  # Ctrl + C 입력시 동작
    GPIO.cleanup()  # 모든 작업 내용 초기화
finally:  # try구문이 끝나면 반드시 실행
    GPIO.cleanup()  # 모든 작업 내용 초기



