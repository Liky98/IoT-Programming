import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
pwm_led = GPIO.PWM(16, 500) #GPIO.PWM(pin_num,frequency(hz)
pwm_green = GPIO.PWM(20, 500)
pwm_green.start(0)
pwm_led.start(0)
try:
    while True:
        for i in range(101): # 출력을 0부터 100까지
            if(i==100):
                i=0
            pwm_led.ChangeDutyCycle(i) # 출력 변경
            pwm_green.ChangeDutyCycle(i) # 출력 변경
            time.sleep(0.02)
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    pwm.stop()
    GPIO.cleanup()
