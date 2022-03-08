import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)
GPIO.setup(25, GPIO.OUT)
def buzz(): # 부저를 울리는 함수
    pitch = 1000 # 주파수
    duration = 0.1 # 울리는 시간
    period = 1.0 / pitch # 소리의 진동을 만들어 내기 위한 간격
    delay = period / 2 # 간격의 절반을 delay로 설정
    cycles = int(duration * pitch)
    for i in range(cycles):
        GPIO.output(25,True)
        time.sleep(delay)
        GPIO.output(25,False)
        time.sleep(delay)
try:
    while True:
        buzz() # 울림!
        time.sleep(0.5) # 0.5초마다 울리게 설정
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()