# Añade un título con un print() para la pizzería, algo como -> Pizzería PF <-.
# El usuario introducirá el dinero que quiera. Guárdalo en una variable.
# Crea una lista donde ir añadiendo los ingredientes extra. Pista: métodos de adición en listas.
# Habrá mínimo tres tipos de pizzas para elegir (pon las que quieras).
# Cada pizza tendrá un coste diferente.
# El usuario podrá elegir solo una pizza.
# Una vez elegida la pizza, se le informará al usuario del total que lleva por el momento.
# Se le debe solicitar, si quiere o no, añadir ingredientes extra (estos harán subir el precio final).
# Añade al menos 3 ingredientes extra. El usuario podrá elegir ninguno, uno o varios de estos.
# No hay límite de ingredientes extra. Si se pasa del dinero que tiene, se le dirá que no le llega y que
# vuelva a realizar el pedido.
# Las pizzas e ingredientes, tendrán sus precios almacenados en variables o constantes
# (piensa que los precios son los que son y no deben variar en todo el programa).
# Con cada ingrediente extra, se le debe ir sumando el precio al total y mostrárselo al usuario con el
# cambio que le queda.
# Si el usuario no quiere ingredientes extra, puede pagar directamente sin añadir ninguno.
# Finalmente, se le debe presentar el ticket (imprimido en la consola) con el total
# gastado, el cambio y todos los elementos que se han añadido al pedido, pizza, ingredientes extra y precios.

print("Welcome to Jason's Pizza")
print("~~~~~~~~~~~~~~~~~~~~~~~~")

budget = float(input("Insert your budget: $"))
initialMoney = budget
total = 0
order = []

margaritaPizza = 8.99
calzonePizza = 4.99
hawaiianPizza = 9.99

extraCheese = 1.99
extraBacon = 2.55
extraPepperoni = 9.99

print("ASOME! We have some options for you:")
while True:
    print(f"1 - Margarita - ${margaritaPizza}")
    print(f"2 - Calzone - ${calzonePizza}")
    print(f"3 - Hawaiian - ${hawaiianPizza}")
    selectedPizza = int(input("Please, select your pizza with a number: "))

    match selectedPizza:
        case 1:
            print(
                f"You selected Margarita Pizza. \n Total to Pay ${margaritaPizza}")
            budget -= margaritaPizza
            print(f"You have ${round(budget,2)}")
            total += margaritaPizza
            order.append(f"Margarita Pizza- ${margaritaPizza}")
            break
        case 2:
            print(
                f"You selected Calzone Pizza. \n Total to Pay ${calzonePizza}")
            budget -= calzonePizza
            print(f"You have ${round(budget,2)}")
            total += calzonePizza
            order.append(f"Calzone Pizza - ${calzonePizza}")
            break
        case 3:
            print(
                f"You selected Hawaiian Pizza. \n Total to Pay ${hawaiianPizza}")
            budget -= hawaiianPizza
            print(f"You have ${round(budget,2)}")
            total += hawaiianPizza
            order.append(f"Hawaiian Pizza - ${hawaiianPizza}")
            break
        case _:
            print("Incorrect Option, please select 1 to 3")

while True:
    print("Do you want add extra ingredients?")
    print(f"1 - Extra Cheese - ${extraCheese}")
    print(f"2 - Extra Bacon - ${extraBacon}")
    print(f"3 - Extra Pepperoni - ${extraPepperoni}")
    print("4 - I'm ok, thank you. Go to pay")
    extrasSelected = int(input("Please, select your extras with a number: "))

    match extrasSelected:
        case 1:
            print(
                f"You selected Extra Cheese. \n Total to Pay ${extraCheese}")
            budget -= extraCheese
            print(f"You have ${round(budget,2)}")
            total += extraCheese
            order.append(f"Extra Cheese - ${extraCheese}")
        case 2:
            print(
                f"You selected Extra Bacon. \n Total to Pay ${extraBacon}")
            budget -= extraBacon
            print(f"You have ${round(budget,2)}")
            total += extraBacon
            order.append(f"Extra Bacon - ${extraBacon}")
        case 3:
            print(
                f"You selected Extra Pepperoni. \n Total to Pay ${extraPepperoni}")
            budget -= extraPepperoni
            print(f"You have ${round(budget,2)}")
            total += extraPepperoni
            order.append(f"Extra Pepperoni - ${extraPepperoni}")
        case 4:
            print("Ok, that's all")
            break
        case _:
            print("Incorrect Option, please select 1 to 4")

if total <= initialMoney:
    print(" ~~~~~ YOUR ORDER ~~~~~")
    print("      DESCRIPTION")
    for i in order:
        print(f"-{i}.")
    print("------------------------")
    print(f"Your Total is: ${round(total,2)}")
    print("------------------------")
    print(f"Your change is: ${round(budget,2)}")
    print("------------------------")
    print("   Enjoy your meal :) ")
    print("------------------------")
else:
    print("Sorry, insufficient money. Please start over")
