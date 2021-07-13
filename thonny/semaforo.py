from machine import Pin
import utime

# semaforo 1
led_rojo1 = Pin(15, Pin.OUT)
led_amarillo1 = Pin(5, Pin.OUT)
led_azul1 = Pin(4, Pin.OUT)

#semaforo 2
led_rojo2 = Pin(18, Pin.OUT)
led_amarillo2 = Pin(19, Pin.OUT)
led_azul2 = Pin(21, Pin.OUT)

while True:
    led_rojo1.value(1)
    led_amarillo1.value(0)
    led_azul1.value(0)
    led_rojo2.value(0)
    led_amarillo2.value(0)
    led_azul2.value(1)
    print("rojo", "verde")
    utime.sleep(1)
    
    led_rojo1.value(0)
    led_amarillo1.value(1)
    led_azul1.value(0)
    led_rojo2.value(0)
    led_amarillo2.value(1)
    led_azul2.value(0)
    print("amarillo")
    utime.sleep(0.5)
    
    led_rojo1.value(0)
    led_amarillo1.value(0)
    led_azul1.value(1)
    led_rojo2.value(1)
    led_amarillo2.value(0)
    led_azul2.value(0)
    print("verde", "rojo")
    utime.sleep(1)
    
    led_rojo1.value(0)
    led_amarillo1.value(1)
    led_azul1.value(0)
    led_rojo2.value(0)
    led_amarillo2.value(1)
    led_azul2.value(0)
    print("amarillo")
    utime.sleep(0.5)

if __name__ == ("__main__"):
    main()
