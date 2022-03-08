import RPi.GPIO as GPIO
import time


control = 0


# 스위치 눌렸을 때 콜백함수
def switchPressed(channel):
    global control
    print('비상상황 해제')
    control = 0


# 부저음 함수
def buzz():  # 부저를 울리는 함수
    global control
    maxTime = time.time()+ 10
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
    while True:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(16, GPIO.OUT)  # BCM 16번 출력으로 설정 #Red
        GPIO.setup(20, GPIO.OUT)  # BCM 20번 출력으로 설정 #Green
        GPIO.setup(21, GPIO.OUT)  # BCM 21번 출력으로 설정 #Blue
        GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # BUTTON 입력 스위치 안눌렸을 때 on, 눌렸을 때 off
        GPIO.setup(24, GPIO.IN)  # PIR Control
        GPIO.add_event_detect(12, GPIO.RISING, callback=switchPressed)

        GPIO.output(16, True)  # 16번 ON
        GPIO.output(20, True)  # 20번 ON
        GPIO.output(21, True)  # 21번 ON
        time.sleep(8)
        if GPIO.input(24) == True:  # 움직임이 감지되면 True를 반환
            print("SENSOR ON!!")
            control = 1

            GPIO.output(20, False)  # 20번 OFF
            GPIO.output(21, False)  # 21번 OFF

        while control == 1:
            GPIO.setup(25, GPIO.IN)  # 부저음
            GPIO.setup(25, GPIO.OUT)
            buzz()
            time.sleep(0.5)
            if control == 0:
                break

        control = 0
        GPIO.output(16, False)
        time.sleep(0.1)
        GPIO.cleanup()  # 모든 작업 내용 초기
        time.sleep(0.1)

except KeyboardInterrupt:  # Ctrl + C 입력시 동작
    GPIO.cleanup()  # 모든 작업 내용 초기화
finally:  # try구문이 끝나면 반드시 실행
    GPIO.cleanup()  # 모든 작업 내용 초기
    


