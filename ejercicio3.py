# Escribir un programa que guarde en un diccionario los
# precios de los artículos de la tabla, pregunte al usuario
# por un artículo, un número de unidades y muestre por pantalla
# el precio de esa cantidad de producto. Si el producto
# no está en el diccionario debe mostrar un mensaje informando de ello.

articulos = {"Pan": 1.40, "Huevos": 2.30,
             "Cebolla": 0.85, "Aceite": 4.35}

articulo = input("Escribe el artículo que quieres: ")
cantidad = int(input("Introduce la cantidad: "))

if articulo in articulos.keys():
    print("El precio de", cantidad, "unidades de", articulo,
          "es", cantidad * articulos[articulo], "€")
else:
    print("Dicho producto no está en la lista")
