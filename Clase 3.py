nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
correo = input("Ingrese su correo electrónico: ")

if nombre.strip() != "" and apellido.strip() != "" and correo.strip() != "" and edad > 18:
    print(apellido)
    print(edad)
    print(correo)
else:
    print("ERROR!")#
