# Escribir un programa que pida al usuario un número entero
# y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
# *
# **
# ***
# ****
# *****
# ******

x = int(1)
num = int(input("Insert an Integer: "))

while x <= num:
    print("*" * x)
    x += 1
