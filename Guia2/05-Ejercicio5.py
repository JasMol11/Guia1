# Para tributar un determinado impuesto se debe ser mayor de 16 años
# y tener unos ingresos iguales o superiores a $1000 mensuales.
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales
# y muestre por pantalla si el usuario tiene que tributar o no

ageUser = int(input("Insert your age: "))
monthlyIncome = float(input("Insert your monthly income: $"))

if ageUser >= 16 and monthlyIncome >= 1000:
    print("You can pay taxes")
else:
    print("You can't pay taxes")
    print("To pay taxes you have to be older than 16 years old and your monthly income more than $1,000.00")
