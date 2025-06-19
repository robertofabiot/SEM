import pickle
import os
from models.classes import Producto, Cliente, Cotizacion, Venta, ItemCotizacion, ItemVenta
from colorama import Fore, Style, init

# Inicializar colorama para colores en Windows
init(autoreset=True)

# Rutas de archivos de datos
DATOS_DIR = "datos"
PRODUCTOS_FILE = os.path.join(DATOS_DIR, "productos.bin")
CLIENTES_FILE = os.path.join(DATOS_DIR, "clientes.bin")
COTIZACIONES_FILE = os.path.join(DATOS_DIR, "cotizaciones.bin")
VENTAS_FILE = os.path.join(DATOS_DIR, "ventas.bin")

# Variables globales para almacenar datos en memoria durante la ejecución
productos = []
clientes = []
cotizaciones = []
ventas = []

def crear_directorio_datos():
    """Crea el directorio de datos si no existe"""
    if not os.path.exists(DATOS_DIR):
        os.makedirs(DATOS_DIR)

def guardar_datos(datos, archivo):
    """Guarda datos en un archivo binario"""
    crear_directorio_datos()
    try:
        with open(archivo, 'wb') as f:
            pickle.dump(datos, f)
        return True
    except Exception as e:
        print(f"Error al guardar datos: {e}")
        return False

def cargar_datos(archivo):
    """Carga datos desde un archivo binario"""
    try:
        if os.path.exists(archivo):
            with open(archivo, 'rb') as f:
                return pickle.load(f)
        return []
    except Exception as e:
        print(f"Error al cargar datos: {e}")
        return []

def inicializar_sistema():
    global productos, clientes, cotizaciones, ventas
    productos = cargar_datos(PRODUCTOS_FILE)
    clientes = cargar_datos(CLIENTES_FILE)
    cotizaciones = cargar_datos(COTIZACIONES_FILE)
    ventas = cargar_datos(VENTAS_FILE)
    
    print(f"Productos cargados: {len(productos) if productos else 0}")
    print(f"Clientes cargados: {len(clientes) if clientes else 0}")
    print(f"Cotizaciones cargadas: {len(cotizaciones) if cotizaciones else 0}")
    print(f"Ventas cargadas: {len(ventas) if ventas else 0}")
    
    if not productos:
        crear_productos_ejemplo()
    
    print("Sistema inicializado correctamente.")

def crear_productos_ejemplo():
    """Crea productos de ejemplo si no existen"""
    global productos
    productos_ejemplo = [
        Producto(1, "Parlante JBL EON615", 450.0, 10, "parlante", "Parlante activo 15 pulgadas"),
        Producto(2, "Pantalla LED 55\"", 800.0, 5, "pantalla", "Pantalla LED 55 pulgadas 4K"),
        Producto(3, "Luz Par LED RGB", 120.0, 20, "luz", "Luz Par LED con control RGB"),
        Producto(4, "Micrófono Shure SM58", 99.0, 8, "parlante", "Micrófono dinámico profesional"),
        Producto(5, "Pantalla Proyector 100\"", 200.0, 3, "pantalla", "Pantalla para proyector 100 pulgadas"),
        Producto(6, "Luz Estrobo LED", 85.0, 15, "luz", "Luz estroboscópica LED alta potencia")
    ]
    productos.extend(productos_ejemplo)
    guardar_productos()

def guardar_productos():
    """Guarda la lista de productos"""
    return guardar_datos(productos, PRODUCTOS_FILE)

def guardar_clientes():
    """Guarda la lista de clientes"""
    return guardar_datos(clientes, CLIENTES_FILE)

def guardar_cotizaciones():
    """Guarda la lista de cotizaciones"""
    return guardar_datos(cotizaciones, COTIZACIONES_FILE)

def guardar_ventas():
    """Guarda la lista de ventas"""
    return guardar_datos(ventas, VENTAS_FILE)

# FUNCIONES PARA PRODUCTOS
def obtener_siguiente_id_producto():
    """Obtiene el siguiente ID disponible para productos"""
    if not productos:
        return 1
    return max(p.id_producto for p in productos) + 1

def agregar_producto(nombre, precio_unitario, cantidad_disponible, categoria, descripcion=""):
    """Agrega un nuevo producto al inventario"""
    global productos
    id_producto = obtener_siguiente_id_producto()
    producto = Producto(id_producto, nombre, precio_unitario, cantidad_disponible, categoria, descripcion)
    productos.append(producto)
    guardar_productos()
    return producto

def buscar_producto_por_id(id_producto):
    """Busca un producto por su ID"""
    for producto in productos:
        if producto.id_producto == id_producto:
            return producto
    return None

def buscar_producto_por_nombre(nombre):
    """Busca un producto por su nombre"""
    for producto in productos:
        if producto.nombre.lower() == nombre.lower():
            return producto
    return None

def eliminar_producto(id_producto):
    """Elimina un producto del inventario"""
    global productos
    producto = buscar_producto_por_id(id_producto)
    if producto:
        productos.remove(producto)
        guardar_productos()
        return True
    return False

def actualizar_stock_producto(id_producto, nueva_cantidad):
    """Actualiza el stock de un producto"""
    producto = buscar_producto_por_id(id_producto)
    if producto:
        producto.cantidad_disponible = nueva_cantidad
        guardar_productos()
        return True
    return False

def reducir_stock_producto(id_producto, cantidad):
    """Reduce el stock de un producto"""
    producto = buscar_producto_por_id(id_producto)
    if producto and producto.cantidad_disponible >= cantidad:
        producto.cantidad_disponible -= cantidad
        guardar_productos()
        return True
    return False

def obtener_productos_stock_bajo():
    """Obtiene lista de productos con stock bajo"""
    return [p for p in productos if p.tiene_stock_bajo()]

def obtener_productos_sin_stock():
    """Obtiene lista de productos sin stock"""
    return [p for p in productos if p.cantidad_disponible == 0]

def imprimir_inventario():
    """Imprime el inventario completo con colores"""
    if not productos:
        print("No hay productos en el inventario.")
        return
    
    print("\n" + "="*80)
    print(f"{'ID':<5} {'NOMBRE':<25} {'PRECIO':<10} {'STOCK':<8} {'CATEGORÍA':<12} {'ESTADO':<10}")
    print("="*80)
    
    for producto in productos:
        if producto.cantidad_disponible == 0:
            color = Fore.RED
            estado = "SIN STOCK"
        elif producto.tiene_stock_bajo():
            color = Fore.YELLOW
            estado = "STOCK BAJO"
        else:
            color = Fore.GREEN
            estado = "DISPONIBLE"
        
        print(f"{color}{producto.id_producto:<5} {producto.nombre:<25} ${producto.precio_unitario:<9.2f} {producto.cantidad_disponible:<8} {producto.categoria:<12} {estado:<10}{Style.RESET_ALL}")
    
    print("="*80)
    
    # Mostrar resumen
    stock_bajo = obtener_productos_stock_bajo()
    sin_stock = obtener_productos_sin_stock()
    
    if stock_bajo:
        print(f"\n{Fore.YELLOW}⚠️  ALERTA: {len(stock_bajo)} productos con stock bajo{Style.RESET_ALL}")
    
    if sin_stock:
        print(f"{Fore.RED}❌ ATENCIÓN: {len(sin_stock)} productos sin stock{Style.RESET_ALL}")

# FUNCIONES PARA CLIENTES
def obtener_siguiente_id_cliente():
    """Obtiene el siguiente ID disponible para clientes"""
    if not clientes:
        return 1
    return max(c.id_cliente for c in clientes) + 1

def agregar_cliente(nombre, direccion, telefono, descuento=0.0):
    """Agrega un nuevo cliente"""
    global clientes
    id_cliente = obtener_siguiente_id_cliente()
    cliente = Cliente(id_cliente, nombre, direccion, telefono, descuento)
    clientes.append(cliente)
    guardar_clientes()
    return cliente

def buscar_cliente_por_id(id_cliente):
    """Busca un cliente por su ID"""
    for cliente in clientes:
        if cliente.id_cliente == id_cliente:
            return cliente
    return None

def buscar_cliente_por_nombre(nombre):
    """Busca un cliente por su nombre"""
    for cliente in clientes:
        if cliente.nombre.lower() == nombre.lower():
            return cliente
    return None

def listar_clientes():
    """Lista todos los clientes"""
    if not clientes:
        print("No hay clientes registrados.")
        return
    
    print("\n" + "="*70)
    print(f"{'ID':<5} {'NOMBRE':<20} {'TELÉFONO':<15} {'DESCUENTO':<10}")
    print("="*70)
    
    for cliente in clientes:
        print(f"{cliente.id_cliente:<5} {cliente.nombre:<20} {cliente.telefono:<15} {cliente.descuento:<10.1f}%")
    
    print("="*70)

# FUNCIONES PARA COTIZACIONES
def obtener_siguiente_id_cotizacion():
    """Obtiene el siguiente ID disponible para cotizaciones"""
    if not cotizaciones:
        return 1
    return max(c.id_cotizacion for c in cotizaciones) + 1

def crear_cotizacion(cliente, items_data, costo_transporte=0.0, horas_extras=0, precio_hora_extra=50.0):
    """Crea una nueva cotización"""
    global cotizaciones
    
    # Crear items de cotización
    items = []
    for item_data in items_data:
        producto = buscar_producto_por_id(item_data['id_producto'])
        if producto:
            item = ItemCotizacion(producto, item_data['cantidad'])
            items.append(item)
    
    if not items:
        return None
    
    id_cotizacion = obtener_siguiente_id_cotizacion()
    cotizacion = Cotizacion(id_cotizacion, cliente, items, costo_transporte, horas_extras, precio_hora_extra)
    cotizaciones.append(cotizacion)
    guardar_cotizaciones()
    return cotizacion

def imprimir_cotizacion(cotizacion):
    """Imprime una cotización formateada"""
    print("\n" + "="*80)
    print(f"COTIZACIÓN #{cotizacion.id_cotizacion:04d}")
    print(f"Fecha: {cotizacion.fecha.strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80)
    
    # Información del cliente
    print(f"Cliente: {cotizacion.cliente.nombre}")
    print(f"Teléfono: {cotizacion.cliente.telefono}")
    print(f"Dirección: {cotizacion.cliente.direccion}")
    print("-"*80)
    
    # Detalles de productos
    print(f"{'PRODUCTO':<30} {'CANT.':<6} {'P.UNIT':<10} {'TOTAL':<12} {'OBSERV.':<10}")
    print("-"*80)
    
    for item in cotizacion.items:
        observacion = ""
        if item.cantidad_excedente > 0:
            observacion = f"+20% ({item.cantidad_excedente})"
        
        print(f"{item.producto.nombre:<30} {item.cantidad_solicitada:<6} ${item.producto.precio_unitario:<9.2f} ${item.precio_total:<11.2f} {observacion:<10}")
    
    print("-"*80)
    
    # Totales
    print(f"{'Subtotal:':<50} ${cotizacion.subtotal:>10.2f}")
    if cotizacion.descuento_cliente > 0:
        print(f"{'Descuento cliente (' + str(cotizacion.cliente.descuento) + '%):':<50} $-{cotizacion.descuento_cliente:>9.2f}")
    if cotizacion.costo_transporte > 0:
        print(f"{'Transporte:':<50} ${cotizacion.costo_transporte:>10.2f}")
    if cotizacion.total_horas_extras > 0:
        print(f"{'Horas extras (' + str(cotizacion.horas_extras) + 'h):':<50} ${cotizacion.total_horas_extras:>10.2f}")
    
    print("="*80)
    print(f"{'TOTAL:':<50} ${cotizacion.total:>10.2f}")
    print("="*80)

# FUNCIONES PARA VENTAS
def obtener_siguiente_id_venta():
    """Obtiene el siguiente ID disponible para ventas"""
    if not ventas:
        return 1
    return max(v.id_venta for v in ventas) + 1

def crear_venta(cliente, items_data):
    """Crea una nueva venta y actualiza el inventario"""
    global ventas
    
    # Verificar disponibilidad antes de crear la venta
    for item_data in items_data:
        producto = buscar_producto_por_id(item_data['id_producto'])
        if not producto or producto.cantidad_disponible < item_data['cantidad']:
            return None, f"Stock insuficiente para {producto.nombre if producto else 'producto no encontrado'}"
    
    # Crear items de venta
    items = []
    for item_data in items_data:
        producto = buscar_producto_por_id(item_data['id_producto'])
        item = ItemVenta(producto, item_data['cantidad'])
        items.append(item)
    
    # Crear la venta
    id_venta = obtener_siguiente_id_venta()
    venta = Venta(id_venta, cliente, items)
    
    # Actualizar inventario
    for item in items:
        reducir_stock_producto(item.producto.id_producto, item.cantidad)
    
    ventas.append(venta)
    guardar_ventas()
    return venta, "Venta registrada exitosamente"

def imprimir_venta(venta):
    """Imprime una venta formateada"""
    print("\n" + "="*80)
    print(f"VENTA #{venta.id_venta:04d}")
    print(f"Fecha: {venta.fecha.strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80)
    
    # Información del cliente
    print(f"Cliente: {venta.cliente.nombre}")
    print(f"Teléfono: {venta.cliente.telefono}")
    print(f"Dirección: {venta.cliente.direccion}")
    print("-"*80)
    
    # Detalles de productos
    print(f"{'PRODUCTO':<35} {'CANT.':<6} {'P.UNIT':<10} {'TOTAL':<12}")
    print("-"*80)
    
    for item in venta.items:
        print(f"{item.producto.nombre:<35} {item.cantidad:<6} ${item.precio_unitario:<9.2f} ${item.precio_total:<11.2f}")
    
    print("="*80)
    print(f"{'TOTAL:':<50} ${venta.total:>10.2f}")
    print("="*80)

# FUNCIONES PARA HISTORIALES
def listar_cotizaciones():
    """Lista todas las cotizaciones"""
    if not cotizaciones:
        print("No hay cotizaciones registradas.")
        return
    
    print("\n" + "="*90)
    print(f"{'ID':<5} {'CLIENTE':<20} {'FECHA':<12} {'TOTAL':<12} {'ITEMS':<8}")
    print("="*90)
    
    for cotizacion in sorted(cotizaciones, key=lambda x: x.fecha, reverse=True):
        fecha_str = cotizacion.fecha.strftime('%Y-%m-%d')
        items_count = len(cotizacion.items)
        print(f"{cotizacion.id_cotizacion:<5} {cotizacion.cliente.nombre:<20} {fecha_str:<12} ${cotizacion.total:<11.2f} {items_count:<8}")
    
    print("="*90)

def listar_ventas():
    """Lista todas las ventas"""
    if not ventas:
        print("No hay ventas registradas.")
        return
    
    print("\n" + "="*80)
    print(f"{'ID':<5} {'CLIENTE':<20} {'FECHA':<12} {'TOTAL':<12} {'ITEMS':<8}")
    print("="*80)
    
    for venta in sorted(ventas, key=lambda x: x.fecha, reverse=True):
        fecha_str = venta.fecha.strftime('%Y-%m-%d')
        items_count = len(venta.items)
        print(f"{venta.id_venta:<5} {venta.cliente.nombre:<20} {fecha_str:<12} ${venta.total:<11.2f} {items_count:<8}")
    
    print("="*80)

def buscar_cotizacion_por_id(id_cotizacion):
    """Busca una cotización por su ID"""
    for cotizacion in cotizaciones:
        if cotizacion.id_cotizacion == id_cotizacion:
            return cotizacion
    return None

def buscar_venta_por_id(id_venta):
    """Busca una venta por su ID"""
    for venta in ventas:
        if venta.id_venta == id_venta:
            return venta
    return None