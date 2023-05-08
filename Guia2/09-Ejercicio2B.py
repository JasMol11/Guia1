# Escribir un programa que pida al usuario un número entero positivo
# y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

x = 1
numUser = int(input("Insert an integer: "))

if numUser % 2 != 0:
    print("The number", numUser, "is an odd number")
else:
    print("The number", numUser, "isn't an odd number")

while x <= numUser:
    print(x)
    x += 2
