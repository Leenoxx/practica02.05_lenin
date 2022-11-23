# Escribir un programa que permita gestionar la base de datos de alumnado de un classroom.
# Los alumnos y alumnas se guardarán en una lista que almacena un diccionario para cada
# alumno/a en el que la clave de cada alumno/a será su NIF, y el valor será otro
# diccionario con los datos del alumno/a (nombre, apellidos, teléfono, correo, aprobado),
# donde aprobado tendrá el valor True si ha aprobado el módulo.
# El programa debe preguntar al usuario por una opción del siguiente
# menú: (1) Añadir alumno/a, (2) Eliminar alumno/a, (3) Mostrar alumno/a,
# (4) Listar t0d0 el alumnado, (5) Listar alumnado aprobado, (6) Terminar.
#  En función de la opción elegida el programa tendrá que hacer lo siguiente:
# Preguntar los datos del alumno/a, crear un diccionario con los datos y añadirlo a la base de datos.
# Preguntar por el NIF del alumno/a y eliminar sus datos de la base de datos.
# Preguntar por el NIF del alumno/a y mostrar sus datos.
# Mostrar lista de t0d0 el alumnado de la base de datos con su NIF y nombre.
# Mostrar la lista del alumnado aprobado de la base de datos con su NIF y nombre.
# Terminar el programa.

alumnado = {"11111111A": {"Nombre": "Pepe", "Apellido": "Sanchez", "Tlf": "607823486",
                          "Correo": "pepe@gmail.com", "Nota": "Aprobado"}}
alumno_nuevo = {}
identificacion = {}
lista_menu = [1, 2, 3, 4, 5, 6]

menu = int(input("Introduce un número:\n"
                 "(1) Añadir alumno/a\n"
                 "(2) Eliminar alumno/a\n"
                 "(3) Mostrar alumno/a\n"
                 "(4) Listar t0d0 el alumnado\n"
                 "(5) Listar alumnado aprobado\n"
                 "(6) Terminar\n->"))

while menu in lista_menu:

    if menu == 1:
        nif = input("Escribe el nuevo NIF del alumno: ")
        name = input("Escribe el nombre: ")
        apellido = input("Escribe el apellido: ")
        tlf = input("Introduce el número: ")
        correo = input("Escribe el correo: ")
        nota = input("¿Aprobado o Suspendido?: ")
        alumno_nuevo["Nombre"] = name
        alumno_nuevo["Apellido"] = apellido
        alumno_nuevo["Tlf"] = tlf
        alumno_nuevo["Correo"] = correo
        alumno_nuevo["Nota"] = nota
        identificacion[nif] = alumno_nuevo
        alumnado.update(identificacion)

    elif menu == 2:
        nif = input("Introduce el NIF del alumno a eliminar: ")
        if nif in alumnado:
            del alumnado[nif]
        else:
            print("Alumno no encontrado!!")

    elif menu == 3:
        nif = input("Introduce el NIF del alumno a mostrar: ")
        if nif in alumnado:
            print(alumnado[nif])
        else:
            print("Alumno no encontrado!!")

    elif menu == 4:
        for i in alumnado.values():
            print(i["Nombre"], i["Apellido"])

    elif menu == 5:
        for i in alumnado.values():
            if i["Nota"] == "Aprobado":
                print(i["Nombre"], i["Apellido"])

    elif menu == 6:
        break

    print("------------------------------")
    menu = int(input("Introduce un número:\n"
                     "(1) Añadir alumno/a\n"
                     "(2) Eliminar alumno/a\n"
                     "(3) Mostrar alumno/a\n"
                     "(4) Listar t0d0 el alumnado\n"
                     "(5) Listar alumnado aprobado\n"
                     "(6) Terminar\n->"))

print("FIN DEL PROGRAMA :D")
