from machine import Pin
import utime
led_nums = [15, 4, 16, 17, 5, 21, 3, 23]
leds_list = list(map(lambda x: Pin(x, Pin.OUT), led_nums))

def leds(led_states: list):
    for i in range(len(leds_list)):
        leds_list[i].value(led_states[i])

while True:
    leds([0,0,0,0,0,0,0,0])
    utime.sleep(0.1)
    leds([0,0,0,0,0,0,0,1])
    utime.sleep(0.1)
    leds([0,0,0,0,0,0,1,1])
    utime.sleep(0.1)
    leds([0,0,0,0,0,1,1,1])
    utime.sleep(0.1)
    leds([0,0,0,0,1,1,1,1])
    utime.sleep(0.1)
    leds([0,0,0,1,1,1,1,1])
    utime.sleep(0.1)
    leds([0,0,1,1,1,1,1,1])
    utime.sleep(0.1)
    leds([0,1,1,1,1,1,1,1])
    utime.sleep(0.1)
    leds([1,1,1,1,1,1,1,1])
    utime.sleep(0.1)

if __name__ == "__main__":
    main()