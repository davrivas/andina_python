from machine import Pin
import utime

rojo = Pin(22, Pin.OUT)
azul = Pin(23, Pin.OUT)

while True:
    num = input('Digite 1 para rojo o 2 para azul')
    
    if num == "1":
        rojo.value(1)
        utime.sleep(1)
    elif num == "2":
        azul.value(1)
        utime.sleep(1)    
    
    rojo.value(0)
    azul.value(0)