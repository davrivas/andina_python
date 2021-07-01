from math import pi

def perimetro_cuadrado(a: int):
    return a * 4

def perimetro_rectangulo(b, h):
    return (b + h) * 4

def perimetro_circulo(r):
    return 2 * pi * r

def perimetro_triangulo(a: int, b: int, c: int):
    return sum([a, b, c])