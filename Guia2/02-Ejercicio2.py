# Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario
# coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

passwrd = input("Insert your password: ")
print("Your password have been saved")

passwrdConf = input("Confirm your password: ")


if passwrd.lower() == passwrdConf.lower():
    print("The password is correct :)")
else:
    print("The password is incorrect:(")
