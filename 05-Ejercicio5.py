#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
#Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete 
#así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
#Cada payaso pesa 112 g y cada muñeca 75 g. 
#Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido 
#y calcule el peso total del paquete que será enviado.

print("Bienvenido, aquí podrás calcular el peso total del paquete")
pesoPayasos=int(112)
pesoMuñecas=int(75)

cantPayasos=int(input("Ingrese la cantidad de payasos vendidos: "))
cantMuñecas=int(input("Ingrese la cantidad de muñecas vendidas: "))

pesoTotal = (cantPayasos * pesoPayasos) + (cantMuñecas * pesoMuñecas)
print(pesoTotal)

print("El peso total del paquete es: ", pesoTotal, "gramos")