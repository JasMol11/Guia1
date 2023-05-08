# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
# El grupo A está formado por las mujeres con un nombre anterior a la M
# y los hombres con un nombre posterior a la N
# y el grupo B por el resto.
# Escribir un programa que pregunte al usuario su nombre y sexo,
# y muestre por pantalla el grupo que le corresponde.

sex = input("Insert your sex, F or M: ")
name = input("Insert your name: ")

if (sex == "F" and name.lower() < "m") or (sex == "M" and name.lower() > "n"):
    group = "A"
else:
    group = "B"

print("Your are in the group", group)
