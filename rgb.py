from machine import Pin
import utime
led_nums = [15, 4, 16]
leds_list = list(map(lambda x: Pin(x, Pin.OUT), led_nums))

def leds(led_states: list):
    print(led_states)
    for i in range(len(leds_list)):
        leds_list[i].value(led_states[i])

while True:
    leds([1,1,1])
    utime.sleep(2)
    leds([1,1,0])
    utime.sleep(2)
    leds([1,0,1])
    utime.sleep(2)
    leds([1,0,0])
    utime.sleep(2)
    leds([0,1,1])
    utime.sleep(2)
    leds([0,1,0])
    utime.sleep(2)
    leds([0,0,1])
    utime.sleep(2)
    leds([0,0,0])
    utime.sleep(2)

if __name__ == "__main__":
    main()
