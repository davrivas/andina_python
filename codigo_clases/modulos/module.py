# print("me gusta se un modulo")

# print(__name__)

# numero = 0

# if __name__ == "__main__":
#     print("me gusta ser un modulo")
# else:
#     print("me encanta ser un modulo")


numero = 8

def sumar(a, b):
    print("esto es una suma")
    return a + b

def producto(a, b):
    print("esto es una multiplicación")
    return a * b

if __name__ == "__main__":
    print("me gusta ser un modulo")
    print(sumar(5, 5))
    print(producto(5, 5))
else:
    print("me encanta ser un modulo")