# Escribir un programa que pregunte al usuario su nombre,
# edad, dirección y teléfono y lo guarde en un diccionario.
# Después debe mostrar por pantalla el mensaje “<nombre>
# tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>”.

datos = {}

datos["nombre"] = input("Escribe tu nombre: ")
datos["edad"] = int(input("Escribe tu edad: "))
datos["direccion"] = input("Escribe tu dirección: ")
datos["tlf"] = int(input("Introduce tu teléfono: "))

print(datos["nombre"], "tiene", datos["edad"], "años, "
      "vive en", datos["direccion"], "y su número de tlf es",
      datos["tlf"])
