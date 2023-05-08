# Escribir un programa que pida al usuario dos números
# y muestre por pantalla su división.
# Si el divisor es cero el programa debe mostrar un error.

numberOne = float(input("Insert the first number: "))
numberTwo = float(input("Insert the second number: "))

if numberTwo == 0:
    print("ERROR, the divisor can't be 0")
else:
    resultDiv = numberOne / numberTwo
    print("The division is:", resultDiv)
