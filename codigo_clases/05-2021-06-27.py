lst = [1,2]

for v in range (2):
    lst.insert(-1, lst[v])
    
print(lst)

nums = [1,2,3]
vals = nums
print(id(nums), id(vals))

def func1(a):
    return None

def func2(a):
    return func1(a) * func1(a)

print(func2(2))

print(1 // 2)

z = 0
y = 10
x = y < z and z > y or y > z and z < y
print(x)

in_ = 0
IN = 0
# in = 0

list = [x * x for x in range(5)]

def fun(lst):
    del lst[lst[2]]
    return lst

print(fun(list))


x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z
print(x, y, z)

a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)

def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2

print(fun(fun(2)))

nums = [1, 2, 3]
vals = nums
del vals[:]
print(nums, vals)

x = 3
y = 2
x = x % y
x = x % y
y = y % x
print(y)

print(1 // 5 + 1 / 5)

tuple = (0, 8)
tuple[1] = tuple[1] + tuple[0]
print(tuple[1])

x = float(input())
y = float(input())
print(y ** (1 / x))

dct = { 'uno': 'dos', 'tres': 'uno', 'dos':'tres' }
v = dct['tres']

for k in range(len(dct)):
    v = dct[v]

print(v)

lst = [i for i in range(-1, -2)]
print(len(lst))

def fun(a, b, c = 0):
    return a + b + c

print(fun(a = 1, b = 0, c = 0))
print(fun(0, 1, 2))
print(fun(a =0, b =0))
print(b = 1)

def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y -1)

print(fun(0, 3))

i = 0
while i  < i + 2:
    i += 1
    print("*")
else:
    print("*")

tup = (1, 2, 4, 8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)

dd = {"3": "2"}
dd.vals()

dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)

for x in dct.keys():
    print(dct[x][1], end = "")

def func(inp = 2, out = 3):
    return inp * out

print(func(out = 2))

lst = [[x for x in range(3)] for y in range(3)]

for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")