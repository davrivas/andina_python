from machine import Pin
import utime
import _thread

push = Pin(15, Pin.IN, Pin.PULL_DOWN)
rojo = Pin(22, Pin.OUT)
azul = Pin(23, Pin.OUT)

def nucleo_dos():
    while True:
        azul.value(1)
        utime.sleep(0.05)
        azul.value(0)
        utime.sleep(0.05)

_thread.start_new_thread(nucleo_dos, ())

while True:
    estado = push.value()
    print(estado)
    utime.sleep(0.05)
    rojo.value(1 if estado == 0 else 0)

if __name__ == "__main__":
    main()

