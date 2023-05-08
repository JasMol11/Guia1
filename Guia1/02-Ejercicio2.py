# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
# calcule el índice de masa corporal y lo almacene en una variable, 
# y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal 
# calculado redondeado con dos decimales

print("Bienvenido, aquí podrás cálcular tu índice de masa corporal")
peso=float(input("Ingresa tu peso en Kg: "))
estatura=float(input("Ingresa tu estatura en metros: "))

imc= peso / (estatura**2)

print("Tu índice de masa corporal (IMC) es de: ", round(imc,2))
