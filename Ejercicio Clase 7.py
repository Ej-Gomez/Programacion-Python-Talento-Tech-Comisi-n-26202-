clientes = []

while True:
    nombre = input("Ingrese el nombre del cliente (o escriba 'fin' para terminar): ").strip()
    
    if nombre.lower() == 'fin':
        break
        
    if not nombre:
        print("Advertencia: El nombre no puede estar vacío. Intente nuevamente.")
    else:
        clientes.append(nombre)

clientes.sort()

print("\nLista de clientes ordenados alfabéticamente:")
for cliente in clientes:
    print(f"- {cliente}")