def feliz_anio_nuevo(deseos = True):
    print("Tres...")
    print("Dos...")
    print("Uno...")

    if not deseos:
        return

    print("¡Feliz año nuevo!")

feliz_anio_nuevo()
feliz_anio_nuevo(False)


def saludo():
    print("Bienvenido al curso")
    return "hola"

x = saludo()
print("El retorno de la función es:", x)


valor = None
if valor == None:
    print("Lo siento, no tienes ningún valor")
print(valor)


def strangeFuncion(n):
    if n % 2 == 0:
        return "es par"

print(3)
print(4)


def sum_of_list(lst: list):
    return sum(lst)

print(sum_of_list([5, 4, 3]))
print(sum_of_list(5))
print(sum_of_list("mi lista"))


def strange_list_function(n):
    strange_list = []

    for i in range(0, n):
        strange_list.insert(0, i)

    return strange_list

print(strange_list_function(5))


def scope_test():
    x = 123

scope_test()
print(x)


def mi_funcion():
    print("¿Conozco la variable?", var)

var = 1
mi_funcion()
print(var)


def mi_funcion():
    var = 2
    print("¿Conozco la variable?", var)

var = 1
mi_funcion()
print(var)


def mi_funcion():
    global var
    var = 2
    print("¿Conozco la variable?", var)

var = 1
mi_funcion()
print(var)


def mi_funcion(n):
    print("Yo obtuve", n)
    n += 1
    print("Yo ahora tengo", n)

var = 1
mi_funcion(var)
print(var)


def is_int(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False

print(is_int(5))
print(is_int(5.0))
print(is_int("5"))


def create_list(n):
    my_list = []
    
    for i in range(n):
        my_list.append(i)
    
    return my_list

print(create_list(5))


def multiply(a, b):
    return a * b

print(multiply(3, 4))

def multiply(a, b):
    return

print(multiply(3, 4))


def deseos():
    return "¡Feliz cumpleaños!"

d = deseos()
print(d)


def message():
    alt = 1
    print("Hola, mundo!")

print(alt)


def imc(peso, altura):
    return peso / altura ** 2

print(imc(52.5, 1.65))


def es_un_triangulo(a, b, c):
    return not (a + b <= c or b + c <= a or c + a <= b)

print(es_un_triangulo(1, 1, 1))
print(es_un_triangulo(1, 1, 3))


def es_un_triangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b

a = float(input("Ingresa la longitud del primer lado: "))
b = float(input("Ingresa la longitud del segundo lado: "))
c = float(input("Ingresa la longitud del tercer lado: "))

puedeSer = "Felicidades, puede ser un triángulo"
noPuedeSer = "Lo siento, no puede ser un triángulo"
print(puedeSer if es_un_triangulo(a, b, c) else noPuedeSer)


def enter_number(i: int):
    return int(input(f"Digite numero {i + 1}: "))

def multiplicar(lst: list):
    res = 1
    
    for i in lst:
        res *= i
        
    return res

print("Bienvenido a la multiplicación")
lst = []

for i in range(5):
    lst.append(enter_number(i))

print(lst)
print("La multiplicación es:", multiplicar(lst))


tuple1 = (1, 2, 4, 8)
tuple2 = 1., .5, .25, .125


miTupla = (1, 10, 100, 1000)
print(miTupla[0])
print(miTupla[-1])
print(miTupla[1:])
print(miTupla[:-2])

for elem in miTupla:
    print(elem)


miTupla = (1, 10, 100)

t1 = miTupla + (1000, 10000)
t2 = miTupla * 3

print(len(t2))
print(t1)
print(t2)


miTupla = (1, 10, 100, 1000)
miTupla.append(10000)
del miTupla[0]
miTupla[1] = -10


dict = {
    "cat": "chat",
    "dog": "chien",
    "horse": "cheval"
    }
phoneNumbers = {
    "boss": 654321987,
    "Suzy": 6546546
    }

emptyDictionay = {}
print(dict, phoneNumbers, emptyDictionay)
print(dict["cat"])
print(phoneNumbers["boss"])
print(len(emptyDictionay))

diccionario = {
    "clave4": 234,
    "clave2": True,
    "clave3": "Valor 1",
    "clave1": [1, 2, 3, 4]
    }

print(diccionario)
print(type(diccionario))
print(len(diccionario))
print(diccionario["clave1"])
print(diccionario.keys())
print(diccionario.values())
print(sorted(diccionario.keys()))
print(diccionario.items())
diccionario[4] = "Color"
print(diccionario)
diccionario["clave4"] = "9999999"
print(diccionario)
del diccionario["clave1"]
print(diccionario)
diccionario.popitem()
print(diccionario)
diccionarioCopia = diccionario.copy()
print(diccionario, id(diccionario), diccionarioCopia, id(diccionarioCopia))

diccionario.clear()
print(diccionario)


cesta = {}
salir = "0"

while salir == "0":
    producto = input("Digite el nombre del producto: ")
    precio = float(input("Digite el precio: "))
    cesta[producto] = precio
    salir = input("Presione 0 para seguir comprando, de lo contrario, otro número: ")

print()
print("Lista de compra")

for producto in cesta.keys():
    print(producto, cesta[producto])