import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(24,GPIO.IN)
try:
    while True:
        if GPIO.input(24) == True: # 움직임이 감지되면 True를 반환
            print("SENSOR ON!!")
            GPIO.output(16,True) # LED를 켠다
        if GPIO.input(24) == False: # 움직임이 없을 경우 False를 반환
            print("SENSOR OFF!!")
            GPIO.output(16,False) # LED를 끈다
        time.sleep(0.5) # 0.5초 마다 감지
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()
