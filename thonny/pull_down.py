# pull down
from machine import Pin
import utime

push = Pin(15, Pin.IN, Pin.PULL_DOWN)
bombillo = Pin(23, Pin.OUT)

while True:
    estado = push.value()
    print(estado)
    utime.sleep(0.05)
    bombillo.value(1 if estado == 0 else 0)    

if __name__ == "__main__":
    main()
