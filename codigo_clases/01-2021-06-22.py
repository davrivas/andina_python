print("La Witsi Witsi Araña \n subio a su telaraña\n\nVino la lluvia \n y se la llevo")

print("La Witsi Witsi Araña", "subio a su telaraña", "\n", "Vino la lluvia", "y se la llevo")

print("My name is", "Python.", end=" *** ")
print("Monty Python")

print("My", "name", "is", "Monty", "Python.", sep="+")

print("Programming", "Essentials", "in", sep="***", end="...")
print("Python")

print(2)
print("2")

print(2+2)
print("2"+"2")

print(type(2))
print(type("2"))

print(type(4))
print(type(4.0))

print(11_111_111) # 11'111.111

print(0o123) # oct
print(0xFFFF) # hex
print(0b110011) # bin

print(-3)
print(-2.0)
print(.4)
print(4.)

print(3e8)
print(0.0000000000000000000001)

print("I like \"Monty Python\"")
print('I like "Monty Python"')

print(True)
print(False)

print("I'm", "learning", '"Python"', sep="\n")

print(2+2)
print(2-2)
print(2*2)
print(2/2)
print(2//2)
print(2%2)
print(2**2)

print(-6 // 4)
print(6. // -4)

print(-4 - 4)

print(2 + 3 * 5)
print(9 % 6 % 2) # left ot right

print(2 ** 2 ** 3) # right to left

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

print((2 ** 4), (2 * 4.), (2 * 4))
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
print((2 % -4), (2 % 4), (2 ** 3 ** 2))

var = 1
print(var)

var = 1
account_balance = 1000.0
clientName = 'John Doe'
print(var, account_balance, clientName)
print(var)

import sys

var = sys.version_info
print("Python version:", end=" ")
print(var.major, var.minor, var.micro, sep=".")

var = 1
print(var)
var = var + 1
print(var)

var = 100
var = 200 + 300
print(var)

import math

a = 2
b = 4
c = math.sqrt((a ** 2) + (b ** 2))
print(c)

a = 2
print("Cateto A", a)
b = 4
print("Cateto B", b)
c = ((a ** 2) + (b ** 2)) ** 0.5
print("La hipotenusa es", c)

# ---------

juan = 3
maria = 4
adan = 5
print(juan, maria, adan, sep = ", ")

totalManzanas = juan + maria + adan
print("Numero total de manzanas: ", totalManzanas)

prom = (juan + maria + adan) // 3
print(prom)

# ---------

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles / 0.6214
kilometers_to_miles = kilometers * 0.6214

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

print("Dime cualquier cosa...")
algo = input()
print(f"Me acabas de decir {algo}!")

algo = input("Dime cualquier cosa")
print("Me acabas de decir", algo, "!")

anything = int(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)


cateto_a = float(input("Inserta la longitud del primer cateto: "))
cateto_b = float(input("Inserta la longitud del segundo cateto: "))
hipo = (cateto_a ** 2 + cateto_b ** 2) ** 0.5
print("La longitud de la hipotenusa es: ", hipo)

fnam = input("May I have your first name, please?")
lnam = input("May I have your last name, please?")
print("Thank you.\n\n")
print("Your name is " + fnam + " " + lnam + ".")

print("James" * 3)

number = 23
print("Hola " + str(number))