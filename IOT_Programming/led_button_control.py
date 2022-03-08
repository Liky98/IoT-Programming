import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT) 
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP) # BUTTON 입력 스위치 안눌렸을 때 on, 눌렸을 때 off
control=False # LED 제어 전역 변수
try:
    while True: # 무한루프
        button_state = GPIO.input(12)
        if button_state == False: # 버튼이 눌리면 False
            if(control==True): # Toggle
                control=False
            else:
                control=True
            print("button pressed") 
        if control == True: # LED 제어 변수가 True 상태이면 LED를 켠다
            GPIO.output(16,True)
        else: # LED 제어 변수가 False 상태이면 LED를 끈다
            GPIO.output(16,False)
        time.sleep(0.2) # 0.2초마다 버튼이 눌렸는지 감지
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()