from random import randint

# Constantes
INGRESO_MIN = 1_000_000
INGRESO_MAX = 8_000_000
CANTIDAD_CLIENTES = 5

# Lista para guardar los clientes
clientes = []

# Repetir 5 veces para registrar 5 clientes
for i in range(CANTIDAD_CLIENTES):
    print(f"\n=== Ingreso de datos para cliente {i+1} ===")

    nombre = input("Nombre completo: ")
    identificacion = input("Número de identificación: ")
    edad = int(input("Edad: "))
    gasto = float(input("Gasto mensual: "))
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")
    estado = True  # Estado predeterminado

    ingreso = randint(INGRESO_MIN, INGRESO_MAX)
    balance = ingreso - gasto

    # Guardar todos los datos del cliente en un diccionario
    cliente = {
        "Nombre": nombre,
        "ID": identificacion,
        "Edad": edad,
        "Gasto": gasto,
        "Teléfono": telefono,
        "Dirección": direccion,
        "Estado": estado,
        "Ingreso": ingreso,
        "Balance": balance
    }

    # Agregar el cliente a la lista
    clientes.append(cliente)

# Mostrar todos los clientes
print("\n=== REPORTE DE TODOS LOS CLIENTES ===")

for idx, cliente in enumerate(clientes, start=1):
    print(f"\n--- Cliente {idx} ---")
    print(f"Nombre: {cliente['Nombre']}")
    print(f"ID: {cliente['ID']}")
    print(f"Edad: {cliente['Edad']}")
    print(f"Teléfono: {cliente['Teléfono']}")
    print(f"Dirección: {cliente['Dirección']}")
    print(f"Estado: {cliente['Estado']}")
    print(f"Ingreso: ${cliente['Ingreso']:,.0f}")
    print(f"Gasto: ${cliente['Gasto']:,.0f}")
    print(f"Balance: ${cliente['Balance']:,.0f}")