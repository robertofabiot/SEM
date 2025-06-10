class EquipamientoDao:
    def __init__(self, inventario):
        self.inventario = inventario

    def agregar_item(self, item):
        self.inventario.append(item)
        print("Item agregado correctamente.")

    def mostrar_items(self):
        for item in self.inventario:
            print(item)