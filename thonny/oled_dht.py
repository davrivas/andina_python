from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from dht import DHT11
import utime
import os
import sys

def get_number(number: int) -> str:
    return str(number) if number >= 10 else "0{}".format(number)

width = 128
height = 64

i2c = I2C(0, scl = Pin(22), sda = Pin(21))
oled = SSD1306_I2C(width, height, i2c)
sensorDHT = DHT11(Pin(15))

even = True

while True:
    oled.fill(0)
    sensorDHT.measure()
    
    temp = sensorDHT.temperature()
    hum = sensorDHT.humidity()
    now = utime.gmtime()
    date_str = "{}-{}-{}".format(now[0], get_number(now[1]), get_number(now[2]))
    time_str = "{}:{}:{}".format(now[3], get_number(now[4]), get_number(now[5]))
    
    oled.text("* " * 8 if even else " *" * 8, 0, 0)
    oled.text('T = {:02d}C'.format(temp), 0, 10)
    oled.text('H = {:02d}%'.format(hum), 0, 20)
    oled.text(date_str, 0, 30)
    oled.text(time_str, 0, 40)
    oled.text("* " * 8 if not even else " *" * 8, 0, 50)
    oled.show()
    even = not even    
    utime.sleep(1)

if __name__ == "__name__":
    main()