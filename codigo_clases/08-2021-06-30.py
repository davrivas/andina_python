class ClaseSimple:
    pass

miPrimerObjeto = ClaseSimple()


class Pila:
    def __init__(self) -> None:
        self.__lista_pila = []
    
    def push(self, val) -> None:
        self.__lista_pila.append(val)
    
    def pop(self):
        val = self.__lista_pila[-1]
        del self.__lista_pila[-1]
        return val

class SumarPila(Pila):
    def __init__(self) -> None:
        Pila.__init__(self)
        self.__sum = 0

objetoPila = Pila()

objetoPila.push(8)
objetoPila.push(4)
objetoPila.push(10)

print(objetoPila.pop())
print(objetoPila.pop())
print(objetoPila.pop())


class ClaseEjemplo:
    contador = 0
    
    def __init__(self, val = 1):
        self.__primera = val
        ClaseEjemplo.contador += 1

objetoEjemplo1 = ClaseEjemplo()
objetoEjemplo2 = ClaseEjemplo(2)
objetoEjemplo3 = ClaseEjemplo(4)

print(objetoEjemplo1.__dict__, objetoEjemplo1.contador)
print(objetoEjemplo2.__dict__, objetoEjemplo2.contador)
print(objetoEjemplo3.__dict__, objetoEjemplo3.contador)


class ClaseEjemplo:
    a = 1
    def __init__(self) -> None:
        self.b = 2

objetoEjemplo = ClaseEjemplo()

print(hasattr(objetoEjemplo, 'b'))
print(hasattr(objetoEjemplo, 'a'))
print(hasattr(ClaseEjemplo, 'b'))
print(hasattr(ClaseEjemplo, 'a'))