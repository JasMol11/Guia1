#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades 
#y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 
#6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 
#8 dígitos enteros y 2 decimales.

nombreProducto=input("Ingrese el nombre del producto: ")

precioProducto=float(input("Ingrese el precio del producto: $"))

cantUnidades=int(input("Ingrese el número de unidades: "))

costoTotal= precioProducto * cantUnidades

print ("Producto: ",nombreProducto,"Precio unitario: $",precioProducto,"stock: ",cantUnidades,"Unidades", "Costo Total: $",costoTotal )
