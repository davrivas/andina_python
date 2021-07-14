from machine import Pin, PWM
from time import sleep

led = PWM(Pin(4), freq = 5000)

def main():
    while True:
        for duty_cycle in range(0, 65360):
            led.duty(duty_cycle)
            sleep(0.05)

if __name__ == "__main__":
    main()