from machine import Pin, PWM
import utime

buzzer = PWM(Pin(4), freq = 450)

while True:
    for i in range(1, 10):
        buzzer.duty(i)
        utime.sleep(1)
        buzzer.duty(0)
        utime.sleep(1)