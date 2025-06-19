from datetime import datetime

class Producto:
    def __init__(self, id_producto, nombre, precio_unitario, cantidad_disponible, categoria, descripcion=""):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.cantidad_disponible = cantidad_disponible
        self.categoria = categoria  # 'parlante', 'pantalla', 'luz'
        self.descripcion = descripcion
        self.stock_minimo = 5  # Alerta de stock bajo
    
    def __str__(self):
        return f"ID: {self.id_producto}, {self.nombre}, Precio: ${self.precio_unitario:.2f}, Stock: {self.cantidad_disponible}"
    
    def to_dict(self):
        return {
            'id_producto': self.id_producto,
            'nombre': self.nombre,
            'precio_unitario': self.precio_unitario,
            'cantidad_disponible': self.cantidad_disponible,
            'categoria': self.categoria,
            'descripcion': self.descripcion,
            'stock_minimo': self.stock_minimo
        }
    
    @classmethod
    def from_dict(cls, data):
        producto = cls(
            data['id_producto'],
            data['nombre'],
            data['precio_unitario'],
            data['cantidad_disponible'],
            data['categoria'],
            data.get('descripcion', '')
        )
        producto.stock_minimo = data.get('stock_minimo', 5)
        return producto
    
    def tiene_stock_bajo(self):
        return self.cantidad_disponible <= self.stock_minimo
    
    def esta_disponible(self, cantidad_solicitada):
        return self.cantidad_disponible >= cantidad_solicitada

class Cliente:
    def __init__(self, id_cliente, nombre, direccion, telefono, descuento=0.0):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.descuento = descuento  # Descuento en porcentaje (0-100)
    
    def __str__(self):
        return f"ID: {self.id_cliente}, {self.nombre}, Tel: {self.telefono}, Descuento: {self.descuento}%"
    
    def to_dict(self):
        return {
            'id_cliente': self.id_cliente,
            'nombre': self.nombre,
            'direccion': self.direccion,
            'telefono': self.telefono,
            'descuento': self.descuento
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data['id_cliente'],
            data['nombre'],
            data['direccion'],
            data['telefono'],
            data.get('descuento', 0.0)
        )

class ItemCotizacion:
    def __init__(self, producto, cantidad_solicitada):
        self.producto = producto
        self.cantidad_solicitada = cantidad_solicitada
        self.cantidad_disponible = min(cantidad_solicitada, producto.cantidad_disponible)
        self.cantidad_excedente = max(0, cantidad_solicitada - producto.cantidad_disponible)
        self.precio_normal = self.cantidad_disponible * producto.precio_unitario
        self.precio_excedente = self.cantidad_excedente * producto.precio_unitario * 1.2  # 20% extra
        self.precio_total = self.precio_normal + self.precio_excedente
    
    def __str__(self):
        return f"{self.producto.nombre} x{self.cantidad_solicitada} = ${self.precio_total:.2f}"
    
    def to_dict(self):
        return {
            'producto': self.producto.to_dict(),
            'cantidad_solicitada': self.cantidad_solicitada,
            'cantidad_disponible': self.cantidad_disponible,
            'cantidad_excedente': self.cantidad_excedente,
            'precio_normal': self.precio_normal,
            'precio_excedente': self.precio_excedente,
            'precio_total': self.precio_total
        }
    
    @classmethod
    def from_dict(cls, data):
        producto = Producto.from_dict(data['producto'])
        item = cls(producto, data['cantidad_solicitada'])
        item.cantidad_disponible = data['cantidad_disponible']
        item.cantidad_excedente = data['cantidad_excedente']
        item.precio_normal = data['precio_normal']
        item.precio_excedente = data['precio_excedente']
        item.precio_total = data['precio_total']
        return item

class Cotizacion:
    def __init__(self, id_cotizacion, cliente, items, costo_transporte=0.0, horas_extras=0, precio_hora_extra=50.0):
        self.id_cotizacion = id_cotizacion
        self.cliente = cliente
        self.items = items
        self.costo_transporte = costo_transporte
        self.horas_extras = horas_extras
        self.precio_hora_extra = precio_hora_extra
        self.fecha = datetime.now()
        self.subtotal = sum(item.precio_total for item in items)
        self.descuento_cliente = (self.subtotal * cliente.descuento) / 100
        self.total_horas_extras = horas_extras * precio_hora_extra
        self.total = self.subtotal - self.descuento_cliente + self.costo_transporte + self.total_horas_extras
    
    def __str__(self):
        return f"Cotización #{self.id_cotizacion} - {self.cliente.nombre} - Total: ${self.total:.2f} - {self.fecha.strftime('%Y-%m-%d %H:%M')}"
    
    def to_dict(self):
        return {
            'id_cotizacion': self.id_cotizacion,
            'cliente': self.cliente.to_dict(),
            'items': [item.to_dict() for item in self.items],
            'costo_transporte': self.costo_transporte,
            'horas_extras': self.horas_extras,
            'precio_hora_extra': self.precio_hora_extra,
            'fecha': self.fecha.isoformat(),
            'subtotal': self.subtotal,
            'descuento_cliente': self.descuento_cliente,
            'total_horas_extras': self.total_horas_extras,
            'total': self.total
        }
    
    @classmethod
    def from_dict(cls, data):
        cliente = Cliente.from_dict(data['cliente'])
        items = [ItemCotizacion.from_dict(item_data) for item_data in data['items']]
        cotizacion = cls(
            data['id_cotizacion'],
            cliente,
            items,
            data['costo_transporte'],
            data['horas_extras'],
            data['precio_hora_extra']
        )
        cotizacion.fecha = datetime.fromisoformat(data['fecha'])
        cotizacion.subtotal = data['subtotal']
        cotizacion.descuento_cliente = data['descuento_cliente']
        cotizacion.total_horas_extras = data['total_horas_extras']
        cotizacion.total = data['total']
        return cotizacion

class ItemVenta:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = producto.precio_unitario
        self.precio_total = cantidad * producto.precio_unitario
    
    def __str__(self):
        return f"{self.producto.nombre} x{self.cantidad} = ${self.precio_total:.2f}"
    
    def to_dict(self):
        return {
            'producto': self.producto.to_dict(),
            'cantidad': self.cantidad,
            'precio_unitario': self.precio_unitario,
            'precio_total': self.precio_total
        }
    
    @classmethod
    def from_dict(cls, data):
        producto = Producto.from_dict(data['producto'])
        item = cls(producto, data['cantidad'])
        item.precio_unitario = data['precio_unitario']
        item.precio_total = data['precio_total']
        return item

class Venta:
    def __init__(self, id_venta, cliente, items):
        self.id_venta = id_venta
        self.cliente = cliente
        self.items = items
        self.fecha = datetime.now()
        self.total = sum(item.precio_total for item in items)
    
    def __str__(self):
        return f"Venta #{self.id_venta} - {self.cliente.nombre} - Total: ${self.total:.2f} - {self.fecha.strftime('%Y-%m-%d %H:%M')}"
    
    def to_dict(self):
        return {
            'id_venta': self.id_venta,
            'cliente': self.cliente.to_dict(),
            'items': [item.to_dict() for item in self.items],
            'fecha': self.fecha.isoformat(),
            'total': self.total
        }
    
    @classmethod
    def from_dict(cls, data):
        cliente = Cliente.from_dict(data['cliente'])
        items = [ItemVenta.from_dict(item_data) for item_data in data['items']]
        venta = cls(
            data['id_venta'],
            cliente,
            items
        )
        venta.fecha = datetime.fromisoformat(data['fecha'])
        venta.total = data['total']
        return venta