# futuro = monto * (1 + interes * tiempo)  # F = P*(1+i*n)
# Escribir un programa que pregunte al usuario una cantidad a invertir,
# el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión
# cada año que dura la inversión

print("Bienvenido, aquí podrás calcular el valor Futuro de tu Inversión")

n = 1
monto = float(input("Ingresa el capital a Invertir: $"))
interes = float(input("Ingresa la tasa de interes anual en decimales: "))
tiempo = float(input("Ingresa el tiempo en años de tu inversión: "))


while n <= tiempo:
    futuro = monto * (1 + interes * n)
    print("En el año", n, "su capital será de: $", round(futuro, 2))
    n += 1
