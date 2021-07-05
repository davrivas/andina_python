import math
print(dir(math))

try:
    raise Exception
except BaseException:
    print("a")
except Exception:
    print("b")
except:
    print("c")

for line in open('text.txt', 'rt'):
    print(line)

# try:
#     raise Exception
# except:
#     print("c")
# except BaseException:
#     print("a")
# except Exception:
#     print("b")

assert var != 0

print(len("\\\\"))
# print(len("\\\"))

print(chr(ord('p') + 2))

print(float("1.3"))

class Class:
    def __init__(self, val=0):
        pass

object = Class(1)
object = Class(None)
object = Class()
object = Class(1, 2)

class A:
    def __init__(self, v=2):
        self.v = v
    
    def set(self, v=1):
        self.v += v
        return self.v

a = A()
b = a
b.set()
print(a.v)

class A:
    A = 1
    def __init__(self, v=2):
        self.a = 0

print(hasattr(A, 'a'))

class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(issubclass(A, C))

class A:
    def __init__(self, v):
        self.__a = v + 1

a = A(0)
print(a.__a)

class A:
    def __init__(self):
        pass

a = A(1)
print(hasattr(a, 'A'))

class A:
    def a(self):
        print('a')

class B:
    def a(self):
        print('b')

class C(B, A):
    def c(self):
        self.a()

o = C()
o.c()

try:
    raise Exception(1, 2, 3)
except Exception as e:
    print(type(e.args))
    print(len(e.args))

def I(n):
    s = '+'
    for i in range(n):
        s += s
        yield s

for x in I(2):
    print(x, end="")

class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v

for x in I():
    print(x, end='')

def o(p):
    def q():
        return '*' * p
    return q

r = o(1)
s = o(2)
print(r() + s())

s = open('text.txt', 'r')
q = s.read(1)
print(q)

for x in open('text.txt', 'rt'):
    print(x)

from io import * 

archivo = open('text.txt')
print(archivo.read)

str1 = 'string'
str2 = str1[:]
print(str1, str2)

def f(par2, par1):
    return par2 + par1

# print(f(par2=1, 2))

z = 2
y = 1
x = y < z or z > y and y > z or z < y
print(x)

str = 'abcdef'
def fun(s):
    del s[2]
    return s

print(fun(str))

x, y, z = 3, 2, 1
z, y, x = x, y, z
print(x, y, z)

a = True
b = False
a = a or b
b = a and b
a = a or b
print(a, b)

def fun(x):
    return 1 if x % 2 != 0 else 2

print(fun(fun(1)))

print(len((1, )))

d = { 1:0, 2:1, 3:2, 0:1 }
x = 0

for y in range(len(d)):
    x = d[x]

print(x)

y = input()
x = input()
print(x + y)

print("a", "b", "c", sep="'")

v = 1 + 1 // 2 + 1 / 2 + 2
print(v)

t = (1, )
t = t[0] + t[0]
print(t)

x = 16
while x > 0:
    print('*', end='')
    x //= 2

d = { 'uno':1, 'tres':3, 'dos':2 }

for k in sorted(d.values()):
    print(k, end=' ')

print(len([i for i in range(0, -2)]))

def fun(a, b, c=0):
    print(a, b, c)

fun(b = 0, b = 0)
fun(a = 1, b = 0, c= 0)
fun(1, c = 2)
fun(0)

lt = [1, 2, 3, 4]
lt = list(map(lambda x: 2*x, 1))
print(lt)

i = 4

while i > 0:
    i -= 2
    print("*")
    if i == 2:
        break
else:
    print("*")

t = (1, 2, 3, 4)
t = t[-2:-1]
t = t[-1]
print(t)

d = {}
d['2'] = [1, 2]
d['1'] = [3, 4]

for x in d.keys():
    print(d[x][1], end="")

def fun(d, k, v):
    d[k] = v

dc = {}
print(fun(dc, '1', 'v'))

ls = [[c for c in range(r)] for r in range(3)]
for x in ls:
    if len(x) < 2:
        print()

print(__name__)

try:
    print(1/0)
except Exception:
    print('Apso alfo malo')
finally:
    print('END')

try:
    raise Exception
except BaseException:
    print("a", end="")
else:
    print("b", end="")
finally:
    print("c")

class A:
    def __init__(self, name):
        self.name = name

a = A("name")
print(a)

class X:
    pass

class Y(X):
    pass

class Z(Y):
    pass

x = X()
z = Z()
print(isinstance(x, Z), isinstance(z, X))

# x = "\"
print(len(x))

x = """
"""
print(len(x))

class Class:
    def __init__(self):
        pass

objeto = Class(1)
objeto = Class(None)
objeto = Class(1, 2)
objeto = Class()

class A:
    A = 1
    def __init__(self, v=2):
        self.v = v + A.A
        A.A += 1
    
    def set(self, v):
        self.v += v
        A.A += 1
        return

a = A()
a.set(2)
print(a.v)

class A:
    A = 1
    def __init__(self):
        self.a = 0

print(hasattr(A, 'A'))

class A:
    pass

class B:
    pass

class C(A, B):
    pass

print(issubclass(C, A) and issubclass(C, B))

class A:
    def __init__(self, v):
        self._a = v + 1

a = A(0)
print(a._a)

class A:
    def __init__(self):
        pass
    
    def f(self):
        return 1
    
    def g():
        return self.f()

a = A()
print(a.g())

class A:
    def a(self):
        print('a')
    
class B:
    def a(self):
        print('b')


class C(A, B):
    def c(self):
        self.a()

o = C()
o.c()

def I(n):
    s = ''
    for i in range(n):
        s += '*'
        yield s

for x in I(3):
    print(x, end="")

def a(x):
    def b():
        return x + x
    return b

x = a('x')
y = a('')
print(x() + y())

s = open('text.txt', 'r')
q = s.readlines()
print(type(q))

s = open('text.txt', 'r')
print(type(s.writable()))
print(type(s.write("hola")))
print(type(s.writelines()))