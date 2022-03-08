from RPLCD.i2c import CharLCD

try:
    lcd = CharLCD('PCF8574', 0x27)
    lcd.write_string('IOT Jonna')
    lcd.crlf()
    lcd.write_string('hard :(')
except KeyboardInterrupt:
    lcd.clear() # LCD 화면 깨끗하게