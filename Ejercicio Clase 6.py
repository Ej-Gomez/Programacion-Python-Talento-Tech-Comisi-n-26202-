# Lista de clientes de prueba, incluyendo un nombre vacío y nombres con mayúsculas/minúsculas mixtas
clientes = ["ana", "JUAN", "", "marta"]

for i in range(len(clientes)):
    posicion = i + 1
    nombre = clientes[i]
    
    # Verificamos si el nombre está vacío
    if nombre == "":
        print(f"Cliente {posicion}: [ALERTA] Nombre no válido")
    else:
        # Aplicamos el método .capitalize() sugerido en la Parte 2 (optativa)
        print(f"Cliente {posicion}: {nombre.capitalize()}")