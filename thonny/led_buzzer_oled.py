from machine import Pin, PWM, I2C
import utime
from ssd1306 import SSD1306_I2C

led = Pin(4, Pin.OUT)
buzzer = PWM(Pin(15), freq = 450)

width = 128
height = 64
i2c = I2C(0, scl = Pin(22), sda = Pin(21))
oled = SSD1306_I2C(width, height, i2c)

def setup(led_val: int, buzzer_val: int, oled_text: str):
    oled.fill(0)
    led.value(led_val)
    buzzer.duty(buzzer_val)
    oled.text(oled_text, 0, 0)
    oled.show()
    utime.sleep(1)
    
def on():
    setup(1, 10, "On")

def off():
    setup(0, 0, "Off")

def main():
    while True:
        on()
        off()

if __name__ == "__main__":
    main()