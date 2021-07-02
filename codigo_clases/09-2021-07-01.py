# class conClase:
#     varia = 1
#     def __init__(self) -> None:
#         self.var = 2
    
#     def metodo(self):
#         pass
    
#     def __oculto(self):
#         pass

# obj = conClase()
# obj.metodo()


# class rectangulo:
#     def __init__(self, base: int, altura: int) -> None:
#         self.altura = altura
#         self.base = base
    
#     def area(self):
#         area = self.base * self.altura
#         return area
    
#     def perimetro(self):
#         perimetro = (2 * self.base) + (2 * self.altura)
#         return perimetro

# areaRectangulo = rectangulo(8, 9)
# areaDos = areaRectangulo.area()
# print(areaDos)


# class A:
#     pass

# class B(A):
#     pass

# class C(A):
#     pass

# class D(A, B):
#     pass

# d = D()


# class Vehiculo:
#     def  __init__(self, marca: str, color: str) -> None:
#         self.marca = marca
#         self.color = color
    
#     def __str__(self) -> str:
#         return "marca: {}, color: {}".format(self.marca, self.color)

# class CarroAntiguo(Vehiculo):
#     def __init__(self, marca: str, color: str, modelo: int) -> None:
#         Vehiculo.__init__(self, marca, color)
#         self.modelo = modelo
    
#     def __str__(self) -> str:
#         return "marca: {}, color: {}, modelo {}".format(self.marca, self.color, self.modelo)

# class CarroNuevo(Vehiculo):
#     def __init__(self, marca: str, color: str, motor: str) -> None:
#         Vehiculo.__init__(self, marca, color)
#         self.motor = motor
    
#     def __str__(self) -> str:
#         return "marca: {}, color: {}, motor {}".format(self.marca, self.color, self.motor)

# class NuevoGama(CarroNuevo):
#     def __init__(self, marca: str, color: str, motor: str, precio: float) -> None:
#         CarroNuevo.__init__(self, marca, color, motor)
#         self.precio = precio
    
#     def __str__(self) -> str:
#         return "marca: {}, color: {}, motor {}, precio {}".format(self.marca, self.color, self.motor, self.precio)

# f1 = NuevoGama("BMW", "rojo", "v8", 1000)
# print(f1)


class BD:
    estado = False
    
    def __init__(self):
        pass
    
    def conexion(self, host, port, user, password, database):
        if host == "localhost" and port == 3306 and user == "root" and password == "secret" and database == "dev":
            print("Conexion establecida")
            BD.estado = True
        else:
            print("No se pudo establecer la conexion")
            BD.estado = False
        
        return BD.estado
    
    def obtener(self):
        pass
    
    def crear(self):
        pass
    
    def actualizar(self):
        pass
    
    def borrar(self):
        pass

class Usuario:
    def __init__(self):
        self.__nombre = ""
        self.correo = ""
        self.edad = ""
    
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

baseDatos = BD()
baseDatos.conexion("localhost", 3306, "root", "secret", "dev")

if not baseDatos.estado:
    exit("End")

print(baseDatos.estado)