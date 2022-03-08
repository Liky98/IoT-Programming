from RPLCD.i2c import CharLCD
import time
import datetime # 파이썬 날짜 내장 모듈
lcd = CharLCD('PCF8574', 0x27) 
try:
    while True:
        now = datetime.datetime.now() # 현재 시간
        nowDate = now.strftime('%Y-%m-%d') # 현재 날짜 Parsing 
        nowTime = now.strftime('%H:%M:%S') # 현재 시각 Parsing
        print(now, nowDate, nowTime)
        time.sleep(1)
        lcd.clear()
        lcd.cursor_pos = (0,3) # 글자 표시할 위치 지정
        lcd.write_string(nowDate)
        lcd.crlf()
        lcd.cursor_pos = (1,4)
        lcd.write_string(nowTime)
except KeyboardInterrupt:
    lcd.clear() # LCD 화면 깨끗하게