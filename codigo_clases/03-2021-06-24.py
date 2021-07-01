numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista:", numbers)
numbers[0] = 111
print("Contenido de la lista:", numbers)

myList = [4, 3, 5.8, False, 'Hola']
print(myList)
print(myList[4])
myList[1] = "curso"
print(myList)
myList[0] = myList[4]
print(myList)
print(myList[0])
del myList[4]
print(myList)

numbers = [10, 5, 7, 2, 1]
print("Index 0:", numbers[0])
print("Length:", len(numbers))
print("Index -1:", numbers[-1])
print("Index -2:", numbers[-2])
print("Index -5:", numbers[-5])

numbers = [1, 2, 3, 4, 5]
print(numbers)
numbers[2] = int(input("Digite el nuevo número central: "))
print(numbers)
del numbers[len(numbers) - 1]
print(numbers)
print("Longitud:", len(numbers))

myList = [4, 3, 4, False, 'Hola']
print(myList)
myList.append(8)
print(myList)
myList.append(9)
print(myList)
myList.extend(range(10, 13))
print(myList)
print(myList.count(8))
myList.insert(9, True)
print(myList)
myList.remove(12)
print(myList)

myList = []

for i in range(7):
    myList.append(i + 1)
    
print(myList)
myList.reverse()
print(myList)
myList.sort()
print(myList)
print("Index 3:", myList.index(3))
myList.pop()
print(myList)
myList.pop(0)
print(myList)


variable1 = 1
variable2 = 2
print(variable1, variable2)
variable1, variable2 = variable2, variable1
print(variable1, variable2)

myList = [10, 1, 8, 3, 5]
print(myList)
myList[0], myList[4] = myList[4], myList[0]
myList[1], myList[3] = myList[3], myList[1]
print(myList)

lista1 = [1,2,3,4]
lista2 = [1,2,3,4]
lista3 = lista1
print(lista1, id(lista1))
print(lista2, id(lista2))
print(lista3, id(lista3))
print(id(lista1) == id(lista3))

myList = [10, 8, 6, 4, 2]
print(myList)
newList = myList[1:3]
print(newList)
newList = myList[:]
print(newList)
newList = myList[:3]
print(newList)
newList = myList[2:]
print(newList)
newList = list(myList)
print(newList)

a = "A"
b = "B"
c = "C"
d = ""
lst = [a, b, c, d]
print(lst)
lst.reverse()
print(lst)

lst = ["D", "F", "A", "Z"]
lst.sort()
print(lst)

def get_number():
    print("Enter a value")
    return int(input())

print("Bienvenidos al curso")
a = get_number()
b = get_number()
c = get_number()

def hola():
    print("hola")

hola(5)


def message(number):
    print(number)

message(3)


def saludo(nombre):
    print("Bienvenido al curso", nombre)

saludo("Python")
saludo("C#")
saludo("Javascript")


def saludo(numero):
    print("Ingrese un numero", numero)

numero = 1234
saludo(1)
print(numero)


def saludo(cosa, otra):
    print("Palabra", cosa, ". Otra palabra", otra)
    
saludo("uno", 1)


def my_function(a, b, c):
    print(a, b, c)

my_function(1, 2, 3)


def sum(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

sum(1, 2, 3)
sum(c = 1, a = 2, b = 3)
sum(3, c = 1, b = 2)
# sum(3, a = 1, b = 2)
sum(4, 3, c = 2)
# sum(4, d = 3, c = 2)


import math

print(dir(math))
print(math.sin(math.pi / 2))


from math import sin, pi
print(sin(pi/2))

def introduction(first_name, last_name = "Smith"):
    print("Hello, my name is", first_name, last_name)
    
introduction("John", "Doe")
introduction("John")