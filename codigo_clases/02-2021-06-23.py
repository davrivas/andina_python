var = 0
print(var == 0)
var = 1
print(var == 0)

var = 0
print(var != 0)
var = 1
print(var != 0)

a = 3
b = 5
print(a > b)

a = 3
b = 5
c = 2
print(a >= b)
print(a >= c)

a = 3
b = 5
c = 3
print(a <= b)
print(a <= c)

num = int(input("Digite un número: "))
print(num < 100)
print(num >= 100)

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1 > num2:
    nmasGrande = num1
else:
    nmasGrande = num2

print('El número más grande es:', nmasGrande)

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tecer numero: "))

largestNumber = max(num1, num2, num3)

print("The largest number is:", largestNumber)

x = 1
y = 1.0
z = "1"

if x == y:
    print("uno")
    
if y == int(z):
    print("dos")
elif x == y:
    print("tres")
else:
    print("cuatro")

i = 1
while i <= 10:
    print(i)
    i+=1

import sys

largestNumber = -sys.maxsize - 1
number = int(input("Introduzca un número o escriba -1 para detener: "))
while number != -1:
    if number > largestNumber:
        largestNumber = number
    number = int(input("Introduzca un número o escriba -1 para detener: "))

print("El número más grande es:", largestNumber)

for i in range(500):
    print("El moni", end="")

for i in range(10):
    print("El valor de i actualmente es actualmente", i)

for i in range(2, 8):
    print("El valor de i actualmente es actualmente", i)
    
for i in range(2, 8, 3):
    print("El valor de i actualmente es actualmente", i)

pow = 1
for exp in range(16):
    print("2 a la potencia de", exp, "es", pow)
    pow *= 2

for i in range(1, 6):
    if i == 3:
        break

    print("Inside the loop.", i)

print("Outside the loop.")


for i in range(1, 6):
    if i == 3:
        continue
    
    print("Inside the loop.", i)

print("Outside the loop.")


print(22 & 15)
print(22 | 15)
var = 16
varRight = var >> 1
varLeft = var << 2
print(var, varRight, varLeft)

i = 15
j = 22
bit = i & j
print(bit)
bit = i | j
print(bit)

x = 4
y = 1

a = x & y
b = x | y
c = ~ x
d = x ^ 5
e = x >> 2
f = x << 2
print(a, b, c, d, e, f)


