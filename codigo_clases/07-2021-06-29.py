print(6/0)


lista = []
x = lista[0]


num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

if num2 != 0:
    print(num1 / num2)
else:
    print("Esta operacion no puede ser realizada.")


try:
    print("todo va bien")
    x = 1 / 1
    print("sigue bien")
except:
    print("Oh cielos, algo salió mal...")


try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except:
    print("Oh cielos, algo salió mal...")

print("FIN")


try:
    x = int(input("Ingresa un número: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("No se puede dividir entre 0.")
except ValueError:
    print("Se debe ingresar un valor entero.")

print("THE END")


try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ValueError:
    print("Debes ingresar un valor entero.")
except:
    print("Oh cielos, algo salio mal...")

print("FIN.")


try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ValueError:
    print("Debes ingresar un valor entero.")

print("FIN.")


import math

x = float(input("Ingresa un numero:"))
assert x >= 0

x = math.sqrt(x)

print(x)


############################
# Scenario Datos
nombre = input("Ingre el nombre de usuario: ")
print("¡Hola " + nombre + "!")


x = ((3 + 2) / 2 * 5) ** 2
print(x)

try:
    n = int(input("Ingresa el primer número: "))
    m = int(input("Ingresa el segundo número: "))
    c = n // m
    r = n % m
    print("n =", n)
    print("m =", m)
    print("c =", c)
    print("r =", r)
except ZeroDivisionError:
    print("No se puede dividir entre 0")
except ValueError:
    print("Digite un valor entero")
except:
    print("Ocurrió un error :(")


# Listas
asignaturas = [ "Matemáticas", "Física", "Química", "Historia", "Lengua"]
mensaje = "Yo estudio: "

for i in range(len(asignaturas)):
    if (i == len(asignaturas) - 1):
        mensaje += "y " + asignaturas[i]
    else:
        mensaje += asignaturas[i] + ", "

print(mensaje)


# Listas y bucles
from math import asin


asignaturas = [ "Matemáticas", "Física", "Química", "Historia", "Lengua"]
calififaciones = []

for i in range(len(asignaturas)):
    nota = float(input("Ingrese la nota que haya sacado en " + asignaturas[i] + ": "))
    calififaciones.append(nota)

for i in range(len(asignaturas)):
    print("En", asignaturas[i], "has sacado", calififaciones[i])


# Listas
cantidad = int(input("Digite la cantidad de numeros ganadores: "))
numeros = []

for i in range(cantidad):
    print("Digite el numero", i + 1, "de la loteria:", end=" ")
    numero = int(input())
    numeros.append(numero)

numeros.sort()
print()
print("Los números ordenados de la loteria son:")

for numero in numeros:
    print(numero)


# Bucles
contraseña = "python"
intentoContraseña = ''
adivinada = False
intentos = 1

while intentoContraseña != contraseña and intentos <= 3:
    intentoContraseña = input("Digite la contraseña: ")
    if (intentoContraseña == contraseña):
        adivinada = True
    else:
        print("Contraseña inválida")
        intentos += 1

print("\n")
if adivinada:
    print("Se adivinó la contraseña!!! :D")
else:
    print("No se adivinó la contraseña :(")


# Condicionales y metodos de cadenas
contraseña = "contraseña"
intento = input("Digite la contraseña: ")

if  contraseña == intento.lower():
    print("La contraseña coincide")
else:
    print("La contraseña no coincide")


# Condicionales y excepciones
try:
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    print(num1 / num2)
except ZeroDivisionError:
    print("No se puede dividir entre 0")
except ValueError:
    print("Digite un valor entero")
except:
    print("Ocurrió un error :(")


# Bucles
edad = int(input("Digite la edad del cliente: "))

if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 4
else:
    precio = 10

print("El precio de la entrada es $", precio, sep = "")


# Diccionario
persona = {}
persona["nombre"] = input("Digite el nombre: ")
persona["edad"] = int(input("Digite la edad: "))
persona["direccion"] = input("Digite la dirección: ")
persona["telefono"] = input("Digite el teléfono: ")
print(persona["nombre"], "tiene", persona["edad"], "años, vive en", persona["direccion"], 'y su número de teléfono es', persona["telefono"])


# Funciones
def saludo(nombre: str):
    print("Hola " + nombre)

saludo("David")
saludo("Santiago")


def invoice(amount, iva = 16):
    return amount + amount * iva / 100

print(invoice(1000, 10))
print(invoice(1000))


