import RPi.GPIO as GPIO
from RPLCD.i2c import CharLCD
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT) # BCM 16번 출력으로 설정
GPIO.setup(20,GPIO.OUT) # BCM 20번 출력으로 설정
GPIO.setup(21,GPIO.OUT) # BCM 21번 출력으로 설정
GPIO.setup(25, GPIO.IN)
GPIO.setup(25, GPIO.OUT)
lcd = CharLCD('PCF8574', 0x27)
GPIO.cleanup()
lcd.clear()
