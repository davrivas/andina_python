from machine import Pin, PWM, ADC
from time import sleep

led = PWM(Pin(4), freq = 5000)
potenciometro = ADC(Pin(36))

while True:
    duty_cycle = potenciometro.read_u16()
    led.duty(duty_cycle)
    print(duty_cycle)
    sleep(0.005)