from machine import Pin
import utime

def rotate(leds):
    for led in leds:
        led.value(1)
        utime.sleep_ms(100)
        led.value(0)
        utime.sleep_ms(100)

led_nums = [15, 4, 16, 17, 5, 21, 3, 23]
leds = list(map(lambda x: Pin(x, Pin.OUT), led_nums))

while True:
    rotate(leds)
    rotate(leds[::-1])

if __name__ == "__main__":
    main()