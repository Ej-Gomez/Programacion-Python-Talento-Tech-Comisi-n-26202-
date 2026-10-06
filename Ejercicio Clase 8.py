# Lista principal para almacenar los productos
productos = []

while True:
    # Mostrar el menú principal
    print("\n--- Sistema de gestión básica de productos ---")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    
    # Solicitar y limpiar la opción seleccionada
    opcion = input("Selecciona una opción (1-5): ").strip()
    
    # 1. Agregar producto
    if opcion == "1":
        # Bucle while secundario para validar que no se ingrese un texto vacío
        while True:
            nuevo_producto = input("Ingresa el nombre del producto a agregar: ").strip()
            
            if nuevo_producto == "":
                print("⚠️ Error: El nombre del producto no puede estar vacío. Intenta de nuevo.")
            else:
                productos.append(nuevo_producto)
                print(f"✅ El producto '{nuevo_producto}' fue agregado con éxito.")
                break # Rompe el bucle de validación y vuelve al menú principal
                
    # 2. Mostrar productos
    elif opcion == "2":
        if len(productos) == 0:
            print("⚠️ La lista está vacía. No hay productos registrados.")
        else:
            print("\n--- Lista de productos ---")
            # Bucle for para recorrer la lista y mostrar los índices
            for i in range(len(productos)):
                print(f"{i + 1}. {productos[i]}")
                
    # 3. Buscar producto
    elif opcion == "3":
        if len(productos) == 0:
            print("⚠️ No hay productos para buscar. La lista está vacía.")
        else:
            buscar = input("Ingresa el nombre del producto a buscar: ").strip()
            
            if buscar == "":
                print("⚠️ Error: El campo de búsqueda no puede estar vacío.")
            else:
                # Se utiliza un bucle for para buscar de forma más flexible (ignorando mayúsculas/minúsculas)
                encontrado = False
                for producto in productos:
                    if producto.lower() == buscar.lower():
                        encontrado = True
                        break
                
                if encontrado:
                    print(f"🔍 El producto '{buscar}' sí se encuentra en el sistema.")
                else:
                    print(f"❌ El producto '{buscar}' no está registrado.")
            
    # 4. Eliminar producto
    elif opcion == "4":
        if len(productos) == 0:
            print("⚠️ No hay productos para eliminar. La lista está vacía.")
        else:
            eliminar = input("Ingresa el nombre del producto a eliminar: ").strip()
            
            if eliminar == "":
                print("⚠️ Error: El nombre del producto no puede estar vacío.")
            else:
                eliminado = False
                # Bucle for usando índices para poder usar el método pop()
                for i in range(len(productos)):
                    if productos[i].lower() == eliminar.lower():
                        producto_borrado = productos.pop(i)
                        print(f"🗑️ Producto '{producto_borrado}' eliminado del sistema.")
                        eliminado = True
                        break
                
                if not eliminado:
                    print(f"❌ No se encontró ningún producto llamado '{eliminar}'.")
            
    # 5. Salir
    elif opcion == "5":
        print("Saliendo del sistema... ¡Hasta luego!")
        break # Rompe el bucle principal y finaliza el programa
        
    # Manejo de ingresos incorrectos en el menú principal
    else:
        print("⚠️ Opción no válida. Por favor, ingresa un número del 1 al 5.")