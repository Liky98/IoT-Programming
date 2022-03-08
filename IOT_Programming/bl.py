import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT) # BCM 16번 출력으로 설정
GPIO.setup(20,GPIO.OUT) # BCM 20번 출력으로 설정
GPIO.setup(21,GPIO.OUT) # BCM 21번 출력으로 설정
try:
    while True:
        GPIO.output(16,True) # 16번 ON
        time.sleep(0.1) # 0.1초간 Delay
        GPIO.output(20,True) # 20번 ON
        time.sleep(0.1)
        GPIO.output(21,True) # 21번 ON
        time.sleep(0.1)
        GPIO.output(16,False) # 21번 OFF
        time.sleep(0.1)
        GPIO.output(20,False) # 21번 OFF
        time.sleep(0.1)
        GPIO.output(21,False) # 21번 OFF
        time.sleep(0.1)
except KeyboardInterrupt: # Ctrl + C 입력시 동작
    GPIO.cleanup() # 모든 작업 내용 초기화
finally: # try구문이 끝나면 반드시 실행
    GPIO.cleanup() # 모든 작업 내용 초기화