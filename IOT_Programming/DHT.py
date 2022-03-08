from RPLCD.i2c import CharLCD
import Adafruit_DHT
import time
dht_type = 22 # DHT 타입
bcm_pin = 23 # 핀 번호
lcd = CharLCD('PCF8574',0x27)

try:
    while True:
        time.sleep(3)
        lcd.clear()
        humidity, temperature = Adafruit_DHT.read_retry(dht_type, bcm_pin)
        humid = str(round(humidity,1)) # 소수점 1째자리에서 올림하고 문자화
        temp = str(round(temperature,1)) # 소수점 1째자리에서 올림하고 문자화
        print(temp,humid)
        lcd.write_string('TEMP ')
        lcd.write_string(temp)
        lcd.write_string('C ')
        lcd.crlf()
        lcd.write_string('HUMID ')
        lcd.write_string(humid)
        lcd.write_string('% ')
except KeyboardInterrupt: # 프로그램 종료 시 LCD 화면의 문자를 지움
    lcd.clear()


