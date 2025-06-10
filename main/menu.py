import models.classes as c
import dao.functions as f

inventario = f.EquipamientoDao([])

def menu():
    print("""
    === CRUD SONIDISTA ===
    1. Agregar equipamiento
    2. Mostrar inventario
    3. Salir
    """)

def main():
    while True:
        menu()
        opcion = input("Opción: ")
        if opcion == "1":
            nombre = input("Nombre del equipo: ")
            precio_venta = float(input("Precio de venta: "))
            precio_servicio = float(input("Precio de servicio: "))
            cantidad = int(input("Cantidad disponible: "))
            item = c.Equipamiento(nombre, precio_venta, precio_servicio, cantidad)
            inventario.agregar_item(item)
        elif opcion == "2":
            inventario.mostrar_items()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")
