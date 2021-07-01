from perimetro import *
from areas import *

x = 2
y = 3
z = 5
print(x, y, z)

print("Area cuadrado: ", area_cuadrado(x))
print("Area rectangulo: ", area_rectangulo(x, y))
print("Area circulo: ", area_circulo(x))
print("Area triangulo:", area_triangulo(x, y))
print("---")
print("Perimetro cuadrado: ", perimetro_cuadrado(x))
print("Perimetro rectangulo: ", perimetro_rectangulo(x, y))
print("Perimetro circulo: ", perimetro_circulo(x))
print("Perimetro triangulo: ", perimetro_triangulo(x, y, z))