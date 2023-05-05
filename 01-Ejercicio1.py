# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora 
# Después debe mostrar por pantalla la paga que le corresponde
# CALCULADORA DE SALARIO DEVENGADO

print("Bienvenido, aquí podrás cálcular tu salario devengado")

nombreTrabajor=input("Ingresa tu nombre: ")
horasTrabajadas=int(input("Ingresa el número de horas trabajadas: "))
costoHora=float(input("Ingresa el costo por hora: "))

costoTotal= costoHora * horasTrabajadas

print(nombreTrabajor, "tu pago correspondiente a", horasTrabajadas, "horas de trabajo es de: $", costoTotal)
