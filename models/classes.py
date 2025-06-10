class Equipamiento:
    def __init__(self, nombre, precio_venta, precio_servicio, cantidad):
        self.__nombre = nombre
        self.__precio_venta = precio_venta
        self.__precio_servicio = precio_servicio
        self.__cantidad = cantidad

    def __str__(self):
        return f"""
        Nombre: {self.__nombre}
        Precio de venta: ${self.__precio_venta}
        Precio de servicio: ${self.__precio_servicio}
        Cantidad disponible: {self.__cantidad}
        """

    def get_data(self):
        return self.__nombre, self.__precio_venta, self.__precio_servicio, self.__cantidad