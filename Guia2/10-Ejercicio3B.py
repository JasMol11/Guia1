# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás
# desde ese número hasta cero separados por comas.

num = int(input("Insert a positive integer: "))

countdown = ""

for i in range(num, -1, -1):
    countdown += str(i) + ", "

print(countdown)
