""" 라이브러리 import """
import tkinter as tk
import RPi.GPIO as GPIO
from RPLCD.i2c import CharLCD
import time

""" SETTING """
control = 0

LED_RED_Control = 0
LED_GREEN_Control = 0
LED_BLUE_Control = 0

GPIO.setmode(GPIO.BCM)

""" ------------함수 정의---------- """

""" 01) Buzzer, Button """



""" LED Sensor """
def LED_RED_ON() :
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16, True)

def LED_RED_OFF() :
    GPIO.output(16, False)

def LED_GREEN_ON() :
    GPIO.setup(20, GPIO.OUT)
    GPIO.output(20, True)

def LED_GREEN_OFF() :
    GPIO.output(20, False)

def LED_BLUE_ON() :
    GPIO.setup(21, GPIO.OUT)
    GPIO.output(21, True)

def LED_BLUE_OFF():
    GPIO.output(21, False)


def Buzzer():  # 부저를 울리는 함수
    global control
    GPIO.setup(25, GPIO.IN)  # 부저음
    GPIO.setup(25, GPIO.OUT)
    time.sleep(0.3)

    if control==0 : #켜져있으면 끄기
        GPIO.output(25,False)
        time.sleep(0.5)
        GPIO.cleanup(25)
    else :
        GPIO.output(25, True)


# 스위치 눌렸을 때 콜백함수
def Button_Click(channel):
    global control
    print('버튼 눌림')
    if control == 0 :
        control = 1
    else :
        control=0
    time.sleep(0.3)
    Buzzer()
    time.sleep(0.2)

def Reset() :
    GPIO.cleanup()
    time.sleep(0.3)
    GPIO.setmode(GPIO.BCM)
    time.sleep(0.3)
    GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    time.sleep(0.3)
    GPIO.add_event_detect(12, GPIO.RISING, callback=Button_Click)



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
        pwm_red.ChangeDutyCycle(i)  # 출력 변경
        pwm_green.ChangeDutyCycle(i)
        pwm_blue.ChangeDutyCycle(i)
        time.sleep(0.02)

def Blink() :
    if GPIO.input(16):
        for i in range(10) :
            GPIO.output(16, False)
            time.sleep(0.1)
            GPIO.output(16, True)
            time.sleep(0.1)
    if GPIO.input(20):
        for i in range(10) :
            GPIO.output(20, False)
            time.sleep(0.1)
            GPIO.output(20, True)
            time.sleep(0.1)
    if GPIO.input(21):
        for i in range(10) :
            GPIO.output(21, False)
            time.sleep(0.1)
            GPIO.output(21, True)
            time.sleep(0.1)



def PIR() :
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(24, GPIO.IN)

    if GPIO.input(24) :
        if GPIO.input(20):
            GPIO.output(20, False)
        if GPIO.input(21):
            GPIO.output(21, False)

        if GPIO.input(16) :
            print("PIR_Detect_Twice!!")
            Blink()
        else :
            print("PIR_Detect!!")
            LED_RED_ON()




class BuzzerMusic(object):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.buzzer_pin = 25  # set to GPIO pin 25
        GPIO.setup(self.buzzer_pin, GPIO.IN)
        GPIO.setup(self.buzzer_pin, GPIO.OUT)


    def buzz(self, pitch, duration):
        if (pitch == 0):
            time.sleep(duration)
            return
        period = 1.0 / pitch  #
        delay = period / 2
        cycles = int(duration * pitch)

        for i in range(cycles):
            GPIO.output(self.buzzer_pin, True)
            time.sleep(delay)
            GPIO.output(self.buzzer_pin, False)
            time.sleep(delay)

    def play(self, tune):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.buzzer_pin, GPIO.OUT)
        x = 0

        if (tune == 3):
            pitches = [392, 294, 0, 392, 294, 0, 392, 0, 392, 392, 392, 0, 1047, 262]
            duration = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.8, 0.4]
            for p in pitches:
                self.buzz(p, duration[x])  # feed the pitch and duration to the func$
                time.sleep(duration[x] * 0.5)
                x += 1

        GPIO.setup(self.buzzer_pin, GPIO.IN)

def music() :
    buzzer_music = BuzzerMusic()
    buzzer_music.play(int(3))



""" GUI 버튼 컨트롤 함수 """
def FUNC_LED_RED_Control() :
    global  LED_RED_Control
    if LED_RED_Control == 0 :
        LED_RED_ON()
        LED_RED_Control = 1
    else :
        LED_RED_OFF()
        LED_RED_Control = 0

def FUNC_LED_GREEN_Control() :
    global  LED_GREEN_Control
    if LED_GREEN_Control == 0 :
        LED_GREEN_ON()
        LED_GREEN_Control = 1
    else :
        LED_GREEN_OFF()
        LED_GREEN_Control = 0


def FUNC_LED_BLUE_Control():
    global LED_BLUE_Control
    if LED_BLUE_Control == 0:
        LED_BLUE_ON()
        LED_BLUE_Control = 1
    else:
        LED_BLUE_OFF()
        LED_BLUE_Control = 0

def Custom01() :
    global LED_GREEN_Control, LED_BLUE_Control, LED_RED_Control
    Reset()
    time.sleep(0.3)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(20, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)
    LED_RED_Control = 1
    LED_BLUE_Control = 1
    LED_GREEN_Control = 1
    pwm_red = GPIO.PWM(16, 500)  # (pin_num, frequency(hz))
    pwm_green = GPIO.PWM(20, 500)
    pwm_blue = GPIO.PWM(21, 500)

    GPIO.output(16, True)
    pwm_red.start(0)
    for i in range(100):  # 출력을 0부터 100까지
        pwm_red.ChangeDutyCycle(i)  # 출력 변경
        time.sleep(0.02)
    GPIO.output(16, True)


    GPIO.output(20, True)
    pwm_green.start(0)
    for i in range(100):  # 출력을 0부터 100까지
        pwm_green.ChangeDutyCycle(i)  # 출력 변경
        time.sleep(0.02)
    GPIO.output(20, True)


    GPIO.output(21, True)
    pwm_blue.start(0)
    for i in range(100):  # 출력을 0부터 100까지
        pwm_blue.ChangeDutyCycle(i)  # 출력 변경
        time.sleep(0.02)
    GPIO.output(21, True)

def Custom02() :
    lcd = CharLCD('PCF8574', 0x27)
    str = input('입력하세요.')
    temp = 0
    if len(str) > 16 :
        str01 = str[:16]
        str02 = str[16:]
        temp = 1

    if temp == 0 :
        lcd.write_string(str)
    else :
        lcd.write_string(str01)
        lcd.crlf()
        lcd.write_string(str02)

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(12, GPIO.RISING, callback=Button_Click)

""" TK 설정 """
main = tk.Tk()
main.title('Raspberry Pi UI')

button01 = tk.Button(main, text ='LED_RED', command=FUNC_LED_RED_Control)
button01.pack()
button02 = tk.Button(main, text ='LED_GREEN', command=FUNC_LED_GREEN_Control)
button02.pack()
button03 = tk.Button(main, text ='LED_BLUE', command=FUNC_LED_BLUE_Control)
button03.pack()
button04 = tk.Button(main, text ='LED_PWM_Modulation', command=LED_PWM_ON)
button04.pack()
button05 = tk.Button(main, text ='Blink', command=Blink)
button05.pack()
button06 = tk.Button(main, text ='Sound_On(Music)', command=music)
button06.pack()
button07 = tk.Button(main, text ='PIR_Check', command=PIR)
button07.pack()
button08 = tk.Button(main, text ='All Off', command=Reset)
button08.pack()
button09 = tk.Button(main, text ='Custom01', command=Custom01)
button09.pack()
button10 = tk.Button(main, text ='Custom02', command=Custom02)
button10.pack()

main.mainloop()
