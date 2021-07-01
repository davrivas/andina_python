from math import *

# for name in dir(math):
#     print(name, end = "\t")


x = 1.4
y = 2.6
ad = 90
print(pi)
print(sin(pi/2))
print(cos(ad))
print(tan(ad))
print(floor(x), floor(y))
print(ceil(x), ceil(y))
print(hypot(x, y))
print(sqrt(144))


from random import *

for i in range(5):
    print(random())

seed(0)

for i in range(5):
    print(random())

print(randrange(4), end = " ")
print(randrange(5, 10), end = " ")
print(randrange(0, 10, 4), end = " ")


from platform import *

print(machine())
print(system())
print(platform())
print(processor())
print(version())
print(python_implementation())
print(python_version_tuple())


palabra = 'por'
print(len(palabra))

vacio = ''
print(len(vacio))

yo_soy = 'I\'m'
print(len(yo_soy))


multiLinea = '''Linea # 1
Linea #2'''
print(len(multiLinea))


ch1 ='@'
ch2 = ' '
ch3 = '['
print(ord(ch1))
print(ord(ch2))
print(ord(ch3))


print(chr(64))
print(chr(945))


alpha = "abcdefg"
print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[::2])
print(alpha[::3])
print(alpha[1::2])


alfabeto = "abcdefghijklmnopqrstuvwxyz"
print("f" in alfabeto)
print("F" in alfabeto)
print("1" in alfabeto)
print("ghi" in alfabeto)
print("Xyz" in alfabeto)


alfabeto = "bcdefghijklmnopqrstuvwxy"
print(alfabeto)
alfabeto = "a" + alfabeto
print(alfabeto)
alfabeto += "z"
print(alfabeto)

print(min("aAbByYzZ"))
t = [0, 1, 2]
print(min(t))

print(max("aAbByYzZ"))
t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + max(t) + ']')
t = [0,1,2]
print(max(t))


print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))


print(list("abcabc"))

print("abcabc".count("b"))
print("abcabc".count("d"))

print("aBcD".capitalize())


print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(8) + ']')
print('[' + 'Beta'.center(12) + ']')
print('[' + 'gamma'.center(20, '*') + ']')


t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("ta"))
print(t.endswith("eta"))


print("omega".startswith("meg"))
print("omega".startswith("om"))


t = "alfabeto"
print(t.find("eto"))
print(t.find("z"))
print(t.find("fa"))


print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

print('Mooo'.isalpha())
print('Mu40'.isalpha())

print('2018'.isdigit())
print('Año2019'.isdigit())


print("Moooo".islower())
print('moooo'.islower())
print('__________')

print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())
print('__________')

print("Moooo".isupper())
print("moooo".isupper())
print("MOOOO".isupper())


print("SiGmA=60".lower())


print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))


print("David      Rivas      2112".split())


print("Yo sé que no sé nada".swapcase())
print()
print("Yo sé que no sé nada".title())
print()
print("Yo sé que no sé nada".upper())


secondGreek = [ "omega", "alpha", "pi", "gama" ]
print(secondGreek)
secondGreek.sort()
print(secondGreek)