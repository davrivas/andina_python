from machine import Pin, PWM
import utime

servo = PWM(Pin(27), freq = 50)

def main():
    while True:
        angulo = float(input('Ingrese un ángulo: '))
        
        if angulo >= 0 and angulo <= 180:
            ciclo = (61.728*angulo**2 - 1E-10*angulo + 1E6)
            ciclo /= 1E6
            ciclo = int(ciclo*1023/20)
            servo.duty(ciclo
                       )
        else:
            print("Digite un ángulo entre 0 y 180")

if __name__ == "__main__":
    main()