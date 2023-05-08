#Escribir un programa que muestre el eco de todo lo que el usuario introduzca
#hasta que el usuario escriba “salir” que terminará

print("If you want to finish, type 'exit'")
word = input("Type something: ")

while word != "exit":
    print(word)
    word = input("Write something: ")
