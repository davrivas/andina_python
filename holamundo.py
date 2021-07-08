from machine import Pin
import utime

led_onboard = Pin(2, Pin.OUT)
time = .5

while True:
    led_onboard.value(1)
    print("on")
    utime.sleep(time)
    
    led_onboard.value(0)
    print("off")
    utime.sleep(time)

if __name__ == "__main__":
    main()