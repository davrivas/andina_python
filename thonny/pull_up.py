# pull up
from machine import Pin
import utime

push = Pin(15, Pin.IN, Pin.PULL_UP)
bombillo = Pin(23, Pin.OUT)

while True:
    estado = push.value()
    bombillo.value(1 if estado == 0 else 0)
    utime.sleep(0.05)

if __name__ == "__main__":
    main()