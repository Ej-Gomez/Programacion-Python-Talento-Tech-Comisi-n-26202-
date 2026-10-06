mes_actual = 1
total_ingresos = 0.0

print("--- Registro de Ingresos Mensuales ---")

# Bucle while para registrar los 6 meses
while mes_actual <= 6:
    try:
        # Solicitamos el ingreso de cada mes
        ingreso = float(input(f"Ingrese el ingreso del mes {mes_actual}: $"))
        
        # Validamos que sea un número positivo
        if ingreso < 0:
            print("Error: El valor no es válido. Los ingresos no pueden ser negativos. Volvé a ingresar el dato.")
        else:
            # Si es válido, sumamos al acumulado y avanzamos al siguiente mes
            total_ingresos += ingreso
            mes_actual += 1
            
    except ValueError:
        print("Error: Por favor, ingresá un valor numérico válido.")

# Cálculo del promedio mensual
promedio_mensual = total_ingresos / 6

# Mostrar resultados finales
print("\n--- Resumen Financiero ---")
print(f"Total acumulado durante los 6 meses: ${total_ingresos:.2f}")
print(f"Promedio mensual: ${promedio_mensual:.2f}")