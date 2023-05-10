lista_numeros = [10, 45, 356, 10, 10, 10,
                 46, 67, 45, 10, 10, 43, 10, 65, 10, 10]

lista_numeros.sort()

for num in lista_numeros:
    if num > 10 and num < 356:
        print("El valor del elemento es: ", num)
