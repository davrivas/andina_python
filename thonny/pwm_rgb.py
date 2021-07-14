from machine import Pin, PWM
from random import randrange
from time import sleep

led_r = PWM(Pin(13), freq = 10000)
led_g = PWM(Pin(12), freq = 10000)
led_b = PWM(Pin(14), freq = 10000)
factor = (65530 / 255)

def get_color(color: int) -> int:
    return int(factor * (255 - color))

while True:
    color_r = randrange(255)
    color_g = randrange(255)
    color_b = randrange(255)
    
    led_r.duty(get_color(color_r))    
    led_g.duty(get_color(color_g))    
    led_b.duty(get_color(color_b))
    print(color_r, color_g, color_b)
    sleep(1)
    