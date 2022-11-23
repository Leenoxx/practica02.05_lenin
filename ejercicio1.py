# Escribir un programa que guarde en una variable el diccionario
# {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario
# por una divisa y muestre su símbolo o un mensaje de aviso
# si la divisa no está en el diccionario.

divisa = {"Euro": "€", "Dollar": "$", "Yen": "¥"}

pregunta = input("Introduce una divisa: ")

print(divisa.get(pregunta, "No existe dicha divisa"))
