import sys
import os
import pwinput
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import dao.functions as funciones
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

ruta = os.path.join(os.path.dirname(__file__), "usuarios.txt") #Variable global para el archivo de usuarios

def cargar_usuarios():
    usuarios = {}
    if os.path.exists(ruta):
        with open(ruta , "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) == 2:
                    usuario, clave = datos
                    usuarios[usuario] = clave
    return usuarios

def iniciar_sesion():
    usuarios = cargar_usuarios() 
    for i in range(3):
        print(f"**Intento #{i+1}**")
        print("INICIO DE SESIÓN")
        usuario = input("Usuario: ")
        intento = pwinput.pwinput(prompt="Contraseña: ", mask="*")
        if usuario in usuarios and usuarios[usuario] == intento:
            print("Acceso permitido\n")
            return
        else:
            print("Usuario o contraseña incorrectos\n")
    print("Número de intentos excedido. Acceso denegado")
    print("Saliendo del programa...")
    exit()

def añadir_usuario():
    usuario = input("Ingrese el nombre de usuario: ")
    clave = pwinput.pwinput(prompt="Ingrese la contraseña: ", mask="*")
    clave_confirmación = pwinput.pwinput(prompt="Confirme la contraseña: ", mask="*")
    if clave == clave_confirmación:
        if os.path.exists(ruta):
            with open(ruta , "a") as archivo:
                archivo.write(f"{usuario},{clave}\n")
        print("Usuario añadido.")
    else:
        print("Las claves no coinciden. Usuario no añadido.")

def administrar_usuarios():
    print(f"\n{Fore.LIGHTMAGENTA_EX}{'='*50}")
    print(f"      ADMINISTRACIÓN DE USUARIOS - SEM")
    print(f"{'='*50}{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Seleccione una opción:{Style.RESET_ALL}")
    print(f"{Fore.GREEN}1.{Style.RESET_ALL} Añadir usuario")
    print(f"{Fore.LIGHTRED_EX}2.{Style.RESET_ALL} Volver al menú principal")
    
    try:
        opcion = int(input(f"\n{Fore.YELLOW}Ingrese su elección: {Style.RESET_ALL}"))
        if opcion == 1:
            añadir_usuario()
        elif opcion == 2:
            print(f"{Fore.CYAN}Regresando al menú principal...{Style.RESET_ALL}")
        else:
            raise ValueError
    except ValueError:
        print(f"{Fore.RED}Error. Ingrese un número válido (1 o 2).{Style.RESET_ALL}")

def mostrar_menu_principal():
    """Muestra el menú principal del sistema"""
    print(f"\n{Fore.CYAN}" + "="*60)
    print(f"    SMART EASY MANAGER (SEM) - Sistema de Inventario")
    print(f"    Negocio de Sonidista - Gestión de Equipos")
    print("="*60 + f"{Style.RESET_ALL}")
    print(f"{Fore.WHITE}1. {Fore.GREEN}Registrar Inventario de productos")
    print(f"{Fore.WHITE}2. {Fore.RED}Eliminar producto")
    print(f"{Fore.WHITE}3. {Fore.BLUE}Impresión del inventario")
    print(f"{Fore.WHITE}4. {Fore.YELLOW}Cotizar servicio")
    print(f"{Fore.WHITE}5. {Fore.MAGENTA}Registrar clientes")
    print(f"{Fore.WHITE}6. {Fore.CYAN}Registrar venta")
    print(f"{Fore.WHITE}7. {Fore.LIGHTBLUE_EX}Historial de cotizaciones")
    print(f"{Fore.WHITE}8. {Fore.LIGHTGREEN_EX}Historial de ventas")
    print(f"{Fore.WHITE}9. {Fore.LIGHTRED_EX}Administrar usuarios")
    print(f"{Fore.WHITE}10. {Fore.LIGHTMAGENTA_EX}Salir{Style.RESET_ALL}")
    print("="*60)

def obtener_opcion():
    """Obtiene la opción seleccionada por el usuario"""
    try:
        opcion = int(input(f"{Fore.CYAN}Seleccione una opción (1-10): {Style.RESET_ALL}"))
        return opcion
    except ValueError:
        print(f"{Fore.RED}Error: Ingrese un número válido.{Style.RESET_ALL}")
        return None

def registrar_inventario():
    """Registra un nuevo producto o actualiza existente"""
    print(f"\n{Fore.GREEN}=== REGISTRAR INVENTARIO ==={Style.RESET_ALL}")
    
    try:
        print("\n¿Qué desea hacer?")
        print("1. Agregar nuevo producto")
        print("2. Actualizar stock de producto existente")
        
        sub_opcion = int(input("Seleccione (1-2): "))
        
        if sub_opcion == 1:
            # Agregar nuevo producto
            nombre = input("Nombre del producto: ").strip()
            if not nombre:
                print(f"{Fore.RED}El nombre no puede estar vacío.{Style.RESET_ALL}")
                return

            precio_venta = float(input("Precio unitario de venta: $"))
            precio_servicio = float(input("Precio unitario de servicio: $"))
            cantidad = int(input("Cantidad disponible: "))
            
            print("\nCategorías disponibles:")
            print("1. parlante")
            print("2. pantalla")
            print("3. luz")
            
            cat_opcion = int(input("Seleccione categoría (1-3): "))
            categorias = {1: "parlante", 2: "pantalla", 3: "luz"}
            categoria = categorias.get(cat_opcion, "parlante")
            
            descripcion = input("Descripción (opcional): ").strip()
            
            producto = funciones.agregar_producto(nombre, precio_venta, precio_servicio, cantidad, categoria, descripcion)
            print(f"{Fore.GREEN}✓ Producto agregado exitosamente: {producto}{Style.RESET_ALL}")
            
        elif sub_opcion == 2:
            # Actualizar stock existente
            funciones.imprimir_inventario()
            id_producto = int(input("\nID del producto a actualizar: "))
            producto = funciones.buscar_producto_por_id(id_producto)
            
            if producto:
                print(f"Producto actual: {producto}")
                nueva_cantidad = int(input("Nueva cantidad: "))
                
                if funciones.actualizar_stock_producto(id_producto, nueva_cantidad):
                    print(f"{Fore.GREEN}✓ Stock actualizado exitosamente.{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Error al actualizar el stock.{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Producto no encontrado.{Style.RESET_ALL}")
    
    except ValueError:
        print(f"{Fore.RED}Error: Ingrese valores numéricos válidos.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

def eliminar_producto_menu():
    """Elimina un producto del inventario"""
    print(f"\n{Fore.RED}=== ELIMINAR PRODUCTO ==={Style.RESET_ALL}")
    
    funciones.imprimir_inventario()
    
    try:
        id_producto = int(input("\nID del producto a eliminar: "))
        producto = funciones.buscar_producto_por_id(id_producto)
        
        if producto:
            print(f"Producto a eliminar: {producto}")
            confirmacion = input("¿Está seguro? (s/n): ").lower().strip()
            
            if confirmacion == 's':
                if funciones.eliminar_producto(id_producto):
                    print(f"{Fore.GREEN}✓ Producto eliminado exitosamente.{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Error al eliminar el producto.{Style.RESET_ALL}")
            else:
                print("Operación cancelada.")
        else:
            print(f"{Fore.RED}Producto no encontrado.{Style.RESET_ALL}")
            
    except ValueError:
        print(f"{Fore.RED}Error: Ingrese un ID válido.{Style.RESET_ALL}")

def cotizar_servicio():
    """Crea una cotización para un cliente"""
    print(f"\n{Fore.YELLOW}=== COTIZAR SERVICIO ==={Style.RESET_ALL}")
    
    try:
        # Seleccionar o crear cliente
        cliente = seleccionar_cliente()
        if not cliente:
            return
        
        # Agregar productos a la cotización
        items_data = []
        print("\nAgregar productos a la cotización:")
        
        while True:
            funciones.imprimir_inventario()
            
            try:
                id_producto = int(input("\nID del producto (0 para terminar): "))
                if id_producto == 0:
                    break
                
                producto = funciones.buscar_producto_por_id(id_producto)
                if not producto:
                    print(f"{Fore.RED}Producto no encontrado.{Style.RESET_ALL}")
                    continue
                
                cantidad = int(input(f"Cantidad de {producto.nombre}: "))
                if cantidad <= 0:
                    print(f"{Fore.RED}La cantidad debe ser mayor a 0.{Style.RESET_ALL}")
                    continue
                
                items_data.append({'id_producto': id_producto, 'cantidad': cantidad})
                print(f"{Fore.GREEN}✓ Agregado: {producto.nombre} x{cantidad}{Style.RESET_ALL}")
                
            except ValueError:
                print(f"{Fore.RED}Error: Ingrese números válidos.{Style.RESET_ALL}")
        
        if not items_data:
            print(f"{Fore.RED}No se agregaron productos a la cotización.{Style.RESET_ALL}")
            return
        
        # Datos adicionales
        costo_transporte = float(input("\nCosto de transporte: $") or "0")
        horas_extras = int(input("Horas extras: ") or "0")
        precio_hora_extra = float(input("Precio por hora extra: $") or "50")
        
        # Crear cotización
        cotizacion = funciones.crear_cotizacion(cliente, items_data, costo_transporte, horas_extras, precio_hora_extra)
        
        if cotizacion:
            funciones.imprimir_cotizacion(cotizacion)
            print(f"{Fore.GREEN}✓ Cotización creada exitosamente.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Error al crear la cotización.{Style.RESET_ALL}")
            
    except ValueError:
        print(f"{Fore.RED}Error: Ingrese valores numéricos válidos.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

def registrar_cliente_menu():
    """Registra un nuevo cliente"""
    print(f"\n{Fore.MAGENTA}=== REGISTRAR CLIENTE ==={Style.RESET_ALL}")
    
    try:
        nombre = input("Nombre del cliente: ").strip()
        if not nombre:
            print(f"{Fore.RED}El nombre no puede estar vacío.{Style.RESET_ALL}")
            return None
        
        # Verificar si ya existe
        cliente_existente = funciones.buscar_cliente_por_nombre(nombre)
        if cliente_existente:
            print(f"{Fore.YELLOW}El cliente ya existe: {cliente_existente}{Style.RESET_ALL}")
            return cliente_existente  # retornar el existente
        
        direccion = input("Dirección: ").strip()
        telefono = input("Teléfono: ").strip()
        descuento = float(input("Descuento predefinido (0-100%): ") or "0")
        
        if descuento < 0 or descuento > 100:
            print(f"{Fore.RED}El descuento debe estar entre 0 y 100%.{Style.RESET_ALL}")
            return None
        
        cliente = funciones.agregar_cliente(nombre, direccion, telefono, descuento)
        print(f"{Fore.GREEN}✓ Cliente registrado exitosamente: {cliente}{Style.RESET_ALL}")
        return cliente  # retornar el nuevo cliente también
        
    except ValueError:
        print(f"{Fore.RED}Error: Ingrese un valor numérico válido para el descuento.{Style.RESET_ALL}")
        return None
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
        return None

def registrar_venta_menu():
    """Registra una nueva venta"""
    print(f"\n{Fore.CYAN}=== REGISTRAR VENTA ==={Style.RESET_ALL}")
    
    try:
        # Seleccionar o crear cliente
        cliente = seleccionar_cliente()
        if not cliente:
            return
        
        # Agregar productos a la venta
        items_data = []
        print("\nAgregar productos a la venta:")
        
        while True:
            funciones.imprimir_inventario()
            
            try:
                id_producto = int(input("\nID del producto (0 para terminar): "))
                if id_producto == 0:
                    break
                
                producto = funciones.buscar_producto_por_id(id_producto)
                if not producto:
                    print(f"{Fore.RED}Producto no encontrado.{Style.RESET_ALL}")
                    continue
                
                if producto.cantidad_disponible == 0:
                    print(f"{Fore.RED}Producto sin stock disponible.{Style.RESET_ALL}")
                    continue
                
                cantidad = int(input(f"Cantidad de {producto.nombre} (disponible: {producto.cantidad_disponible}): "))
                
                if cantidad <= 0:
                    print(f"{Fore.RED}La cantidad debe ser mayor a 0.{Style.RESET_ALL}")
                    continue
                
                if cantidad > producto.cantidad_disponible:
                    print(f"{Fore.RED}Stock insuficiente. Disponible: {producto.cantidad_disponible}{Style.RESET_ALL}")
                    continue
                
                items_data.append({'id_producto': id_producto, 'cantidad': cantidad})
                print(f"{Fore.GREEN}✓ Agregado: {producto.nombre} x{cantidad}{Style.RESET_ALL}")
                
            except ValueError:
                print(f"{Fore.RED}Error: Ingrese números válidos.{Style.RESET_ALL}")
        
        if not items_data:
            print(f"{Fore.RED}No se agregaron productos a la venta.{Style.RESET_ALL}")
            return
        
        # Crear venta
        venta, mensaje = funciones.crear_venta(cliente, items_data)
        
        if venta:
            funciones.imprimir_venta(venta)
            print(f"{Fore.GREEN}✓ {mensaje}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Error: {mensaje}{Style.RESET_ALL}")
            
    except ValueError:
        print(f"{Fore.RED}Error: Ingrese valores numéricos válidos.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

def seleccionar_cliente():
    print("\n¿Qué desea hacer?")
    print("1. Seleccionar cliente existente")
    print("2. Crear nuevo cliente")
    
    try:
        opcion = int(input("Seleccione (1-2): "))

        if opcion == 1:
            if not funciones.clientes:
                print("No hay clientes registrados. Creando nuevo cliente...")
                return crear_cliente_rapido()

            funciones.listar_clientes()

            id_cliente = int(input("\nID del cliente: "))
            cliente = funciones.buscar_cliente_por_id(id_cliente)

            if not cliente:
                print(f"{Fore.RED}Cliente no encontrado.{Style.RESET_ALL}")
                return None

            return cliente

        elif opcion == 2:
            return registrar_cliente_menu()

        else:
            print(f"{Fore.RED}Opción inválida.{Style.RESET_ALL}")
            return None

    except ValueError:
        print(f"{Fore.RED}Error: Ingrese un número válido.{Style.RESET_ALL}")
        return None

def crear_cliente_rapido():
    """Crea un cliente de forma rápida"""
    try:
        nombre = input("Nombre del cliente: ").strip()
        if not nombre:
            print(f"{Fore.RED}El nombre no puede estar vacío.{Style.RESET_ALL}")
            return None
        
        direccion = input("Dirección: ").strip()
        telefono = input("Teléfono: ").strip()
        descuento = float(input("Descuento (0-100%, presione Enter para 0): ") or "0")
        
        if descuento < 0 or descuento > 100:
            descuento = 0
        
        cliente = funciones.agregar_cliente(nombre, direccion, telefono, descuento)
        print(f"{Fore.GREEN}✓ Cliente creado: {cliente}{Style.RESET_ALL}")
        return cliente
        
    except ValueError:
        print(f"{Fore.RED}Error en el descuento, se asignará 0%.{Style.RESET_ALL}")
        cliente = funciones.agregar_cliente(nombre, direccion, telefono, 0)
        return cliente

def mostrar_historial_cotizaciones():
    """Muestra el historial de cotizaciones"""
    print(f"\n{Fore.LIGHTBLUE_EX}=== HISTORIAL DE COTIZACIONES ==={Style.RESET_ALL}")
    
    funciones.listar_cotizaciones()
    
    if funciones.cotizaciones:
        try:
            id_cotizacion = int(input("\nID de cotización para ver detalles (0 para cancelar): "))
            if id_cotizacion != 0:
                cotizacion = funciones.buscar_cotizacion_por_id(id_cotizacion)
                if cotizacion:
                    funciones.imprimir_cotizacion(cotizacion)
                else:
                    print(f"{Fore.RED}Cotización no encontrada.{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}ID inválido.{Style.RESET_ALL}")

def mostrar_historial_ventas():
    """Muestra el historial de ventas"""
    print(f"\n{Fore.LIGHTGREEN_EX}=== HISTORIAL DE VENTAS ==={Style.RESET_ALL}")
    
    funciones.listar_ventas()
    
    if funciones.ventas:
        try:
            id_venta = int(input("\nID de venta para ver detalles (0 para cancelar): "))
            if id_venta != 0:
                venta = funciones.buscar_venta_por_id(id_venta)
                if venta:
                    funciones.imprimir_venta(venta)
                else:
                    print(f"{Fore.RED}Venta no encontrada.{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}ID inválido.{Style.RESET_ALL}")

def ejecutar_menu():
    """Ejecuta el menú principal"""
    iniciar_sesion() #No es necesario comprobar si retorna True o False porque la función saca del programa al usuario automáticamente tras tres intentos fallidos
    while True:
        mostrar_menu_principal()
        opcion = obtener_opcion()
        
        if opcion is None:
            continue
        
        if opcion == 1:
            registrar_inventario()
        elif opcion == 2:
            eliminar_producto_menu()
        elif opcion == 3:
            print(f"\n{Fore.BLUE}=== INVENTARIO ACTUAL ==={Style.RESET_ALL}")
            funciones.imprimir_inventario()
        elif opcion == 4:
            cotizar_servicio()
        elif opcion == 5:
            registrar_cliente_menu()
        elif opcion == 6:
            registrar_venta_menu()
        elif opcion == 7:
            mostrar_historial_cotizaciones()
        elif opcion == 8:
            mostrar_historial_ventas()
        elif opcion == 9:
            administrar_usuarios()
        elif opcion == 10:
            print(f"\n{Fore.GREEN}Gracias por usar Smart Easy Manager (SEM)")
            print(f"¡Hasta luego!{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Opción inválida. Seleccione una opción del 1 al 9.{Style.RESET_ALL}")
        
        # Pausa para que el usuario pueda leer los mensajes
        input(f"\n{Fore.CYAN}Presione Enter para continuar...{Style.RESET_ALL}")