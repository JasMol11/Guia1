# Escribir un programa que pida al usuario un número entero
# y muestre por pantalla si es par o impar.

numUser = int(input("Insert an integer: "))

if numUser % 2 == 0:
    print("The number", numUser, "is an even number")
else:
    print("The number", numUser, "is an odd number")
