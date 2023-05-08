# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
#y muestre por pantalla el capital obtenido en la inversión.

print("Bienvenido, aquí podrás calcular el valor Futuro de tu Inversión")

monto=float(input("Ingresa el capital a Invertir: $"))
interes=float(input("Ingresa la tasa de interes anual en decimales: "))
tiempo=float(input("Ingresa el tiempo en años de tu inversión: "))

futuro = monto * (1 + interes * tiempo) #F = P*(1+i*n)

print("Al invertir $",monto, "a una tasa de" , interes*100, "% de interes anual, durante", tiempo, "años", "obtendrá un capital de $", futuro)
