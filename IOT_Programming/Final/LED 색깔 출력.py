import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT) # BCM 16번 출력으로 설정 Red
GPIO.setup(20,GPIO.OUT) # BCM 20번 출력으로 설정 Green
GPIO.setup(21,GPIO.OUT) # BCM 21번 출력으로 설정 Blue
GPIO.setup(13,GPIO.OUT) # 2번 LED Red
GPIO.setup(19,GPIO.OUT) # 2번 LED Green
GPIO.setup(26,GPIO.OUT) # 2번 LED Blue
try:
	while True:
		GPIO.output(16,True) # 16번 ON
		time.sleep(0.5)
		GPIO.output(16,False) # 16번 OFF
		time.sleep(0.5)
		GPIO.output(20,True) # 20번 ON
		time.sleep(0.5)
		GPIO.output(20,False) # 20번 OFF
		time.sleep(0.5)
		GPIO.output(21,True) # 21번 ON
		time.sleep(0.5)
		GPIO.output(21,False)
		time.sleep(0.5)

		GPIO.output(13,True)
		time.sleep(0.5)
		GPIO.output(13,False)
		time.sleep(0.5)
		GPIO.output(19, True)
		time.sleep(0.5)
		GPIO.output(19, False)
		time.sleep(0.5)
		GPIO.output(26, True)
		time.sleep(0.5)
		GPIO.output(26, False)
		time.sleep(0.5)

except KeyboardInterrupt:
	GPIO.cleanup()
finally: # try구문이 끝나면 반드시 실행
	GPIO.cleanup()
