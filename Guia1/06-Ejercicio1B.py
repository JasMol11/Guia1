#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero 
#e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido
i=0

user=input("Introduzca su nombre de usuario: ")
n=int(input("Introduzca un numero entero: "))

while i < n:
    print(user)
    i += 1
