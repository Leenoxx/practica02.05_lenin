# Escribir un programa que cree un diccionario de traducción
# español-inglés. El usuario introducirá las palabras en español
# e inglés separadas por dos puntos, y cada par <palabra>:<traducción>
# separados por comas, hasta que el usuario introduzca la palabra “terminar”.
# El programa debe crear un diccionario con las palabras y sus traducciones.
# Después pedirá una frase en español y utilizará el diccionario para
# traducirla palabra a palabra. Si una palabra no está en el
# diccionario debe dejarla sin traducir.

diccionario = {}
texto = input("Escribe una traducción de esta manera "
              "<palabra>:<traducción>:\n")

while texto != "terminar":
    diccionario[texto.split(":")[0]] = texto.split(":")[1]
    texto = input("Escribe una traducción de esta manera "
                  "<palabra>:<traducción>:\n")

traduccion = input("Escribe un texto a traducir: ")

for palabra in traduccion.split():
    if palabra in diccionario.keys():
        print(diccionario[palabra], end=" ")
    else:
        print(palabra, end=" ")
