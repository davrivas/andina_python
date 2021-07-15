from machine import Pin, PWM
import utime

servo= PWM(Pin(27), freq = 50)
while True:
    angulo = float(input('ingrese un angulo: '))
    if angulo >=0 and angulo <=180:
        ciclo = (61.728*angulo**2 - 10000000000*angulo + 1000000)
        ciclo /= 1000000
        ciclo = int(ciclo*1023/20)
        servo.duty(ciclo)
    else:
        print ('digite un angulo entre 0 y 180 ')
            
    
    
    