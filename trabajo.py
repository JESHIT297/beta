import random

# ================== CONFIGURACIONES ==================
INGRESO_MIN = 1_000_000  # constante
INGRESO_MAX = 8_000_000  # constante
CANTIDAD_CLIENTES = 5    # constante

# ================== FUNCIONES ==================
def solicitar_datos_cliente():
    """Solicita los datos de un cliente y retorna un diccionario con la información y cálculos."""
    nombre = input("Nombre completo: ")
    id_num = input("Número de identificación: ")
    edad = int(input("Edad: "))
    gasto_mensual = float(input("Gasto mensual: "))
    telefono = input("Teléfono móvil: ")
    direccion = input("Dirección: ")
    estado = True  # Estado predeterminado

    ingreso_mensual = random.randint(INGRESO_MIN, INGRESO_MAX)
    balance = ingreso_mensual - gasto_mensual

    cliente = {
        "Nombre": nombre,
        "ID": id_num,
        "Edad": edad,
        "Gasto": gasto_mensual,
        "Teléfono": telefono,
        "Dirección": direccion,
        "Estado": estado,
        "Ingreso": ingreso_mensual,
        "Balance": balance
    }
    return cliente

def mostrar_reporte_cliente(cliente, idx):
    """Muestra de forma formateada el reporte de un cliente."""
    print(f"\n==================== CLIENTE {idx} ====================")
    print(f"Nombre: {cliente['Nombre']}")
    print(f"ID: {cliente['ID']}")
    print(f"Edad: {cliente['Edad']}")
    print(f"Teléfono: {cliente['Teléfono']}")
    print(f"Dirección: {cliente['Dirección']}")
    print(f"Estado activo: {cliente['Estado']}")
    print(f"Ingreso mensual: ${cliente['Ingreso']:,.2f}")
    print(f"Gasto mensual: ${cliente['Gasto']:,.2f}")
    print(f"Balance estimado: ${cliente['Balance']:,.2f}")
    print(f"=====================================================")

# ================== MAIN ==================
def main():
    clientes = []
    print("\n=== Registro de 5 Clientes para FinanSmart ===")
    for i in range(CANTIDAD_CLIENTES):
        print(f"\n--- Ingreso de datos para el cliente {i+1} ---")
        cliente = solicitar_datos_cliente()
        clientes.append(cliente)

    print("\n=== Reporte Final de Clientes ===")
    for idx, cliente in enumerate(clientes, 1):
        mostrar_reporte_cliente(cliente, idx)

# ================== EJECUCIÓN ==================
if __name__ == "__main__":
    main()
