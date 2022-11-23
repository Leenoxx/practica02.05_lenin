
alumnado = {"11111111A": {"Nombre": "Pepe", "Apellido": "Sanchez", "Tlf": "607823486",
                          "Correo": "pepe@gmail.com", "Nota": "Aprobado"},
            "12345678B": {"Nombre": "Luis", "Apellido": "Pepe", "Tlf": "245687543",
                          "Correo": "luis@gmail.com", "Nota": "Suspendido"}}

for i in alumnado.values():
        if i["Nota"] == "Aprobado":
            print(i["Nombre"])
