from machine import Pin, ADC
import utime

sensor = ADC(Pin(39))

while True:
    # conversion_factor = 100 / (65535)
    lectura = float(sensor.read_u16())
    print(lectura)
    # valor = lectura * conversion_factor
    # print(valor)
    utime.sleep(0.25)