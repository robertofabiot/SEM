# Smart Easy Manager (SEM)

## Sistema de Gestión de Inventario y Cotizaciones para Negocio de Sonidista

### Descripción

Smart Easy Manager (SEM) es un sistema completo para la gestión de un negocio de sonidista que ofrece servicios de instalación de parlantes, pantallas y luces para eventos. El sistema automatiza la gestión del inventario, la elaboración de cotizaciones y la administración de usuarios, reduciendo errores manuales y mejorando la eficiencia operativa.

### Características Principales

- ✅ **Gestión de Inventario**: Control completo de productos con alertas de stock bajo y precios diferenciados para venta y servicio  
- ✅ **Cotizaciones Automáticas**: Cálculo automático de precios de servicio con recargos por excedentes  
- ✅ **Control de Clientes**: Registro de clientes con descuentos personalizados  
- ✅ **Ventas**: Registro de ventas con precios específicos de venta y actualización automática del inventario  
- ✅ **Historial Completo**: Seguimiento de todas las cotizaciones y ventas  
- ✅ **Persistencia de Datos**: Almacenamiento en archivos binarios para conservar información  
- ✅ **Interfaz Colorida**: Uso de colores para mejor experiencia de usuario  
- ✅ **Gestión de Usuarios**: Añadir y eliminar usuarios mediante contraseña verificada  

### Estructura del Proyecto

```
SEM/
├── app.py                  # Archivo principal para ejecutar
├── dao/
│   └── functions.py       # Funciones de acceso a datos
├── models/
│   └── classes.py         # Clases del modelo de datos
├── main/
│   └── menu.py           # Interfaz de menú del usuario
├── datos/                 # Directorio para archivos binarios (se crea automáticamente)
│   ├── productos.bin
│   ├── clientes.bin
│   ├── cotizaciones.bin
│   └── ventas.bin
├── usuarios.txt           # Archivo de usuarios (formato texto)
└── README.md
```

### Requisitos del Sistema

- Python 3.6 o superior  
- Librerías:
  - `colorama` para colores en terminal  
  - `pwinput` para ocultar entrada de contraseñas  

### Instalación

1. Instalar Python 3 (si no está instalado)
2. Instalar las librerías necesarias:
   ```bash
   pip install colorama pwinput
   ```

### Ejecución

Para ejecutar el sistema, abra una terminal en el directorio SEM y ejecute:

```bash
python app.py
```

### Funcionalidades del Sistema

#### 1. Registrar Inventario de Productos
- Agregar nuevos productos al inventario con precios separados para venta y servicio
- Actualizar stock de productos existentes
- Categorías: parlantes, pantallas, luces

#### 2. Eliminar Producto
- Eliminar productos del inventario con confirmación

#### 3. Impresión del Inventario
- Visualización completa del inventario
- Productos con stock bajo aparecen en amarillo
- Productos sin stock aparecen en rojo
- Alertas automáticas de stock bajo

#### 4. Cotizar Servicio
- Selección de cliente existente o creación de nuevo cliente
- Selección de productos con cantidades
- Cálculo automático de precios de servicio:
  - 20% extra por unidades que excedan el stock disponible
  - Descuentos personalizados por cliente
  - Costo de transporte
  - Horas extras con precio configurable

#### 5. Registrar Clientes
- Registro de nuevos clientes
- Información: nombre, dirección, teléfono, descuento predefinido

#### 6. Registrar Venta
- Registro de ventas con precios específicos para venta
- Actualización automática del inventario
- Verificación de stock disponible
- Solo permite vender productos con stock suficiente

#### 7. Historial de Cotizaciones
- Listado de todas las cotizaciones realizadas
- Visualización detallada de cotizaciones específicas

#### 8. Historial de Ventas
- Listado de todas las ventas realizadas
- Visualización detallada de ventas específicas

#### 9. Administración de Usuarios
- Añadir nuevos usuarios ingresando nombre y contraseña
- Eliminar usuarios ingresando su contraseña para verificación
- Solo puede eliminarse un usuario si se proporciona su clave correctamente
- Usuarios almacenados en un archivo de texto (`usuarios.txt`)

### Reglas de Negocio

1. **Stock Mínimo**: Los productos con 5 unidades o menos se consideran de stock bajo  
2. **Recargo por Excedente**: Si se solicita más cantidad de la disponible, se cobra 20% extra por las unidades excedentes  
3. **Descuentos**: Cada cliente puede tener un descuento predefinido (0-100%)  
4. **Horas Extras**: Precio configurable por hora (predeterminado: $50/hora)  
5. **Persistencia**: Todos los datos se guardan automáticamente en archivos binarios  

### Productos de Ejemplo

El sistema incluye productos de ejemplo al ejecutarse por primera vez:
- Parlante JBL EON615 - $450.00  
- Pantalla LED 55" - $800.00  
- Luz Par LED RGB - $120.00  
- Micrófono Shure SM58 - $99.00  
- Pantalla Proyector 100" - $200.00  
- Luz Estrobo LED - $85.00  

### Datos Técnicos

- **Almacenamiento**: Archivos binarios (.bin) usando pickle  
- **Codificación**: UTF-8 para soporte de caracteres especiales  
- **Colores**: Implementado con colorama para compatibilidad con Windows  
- **Fechas**: Formato ISO para mejor compatibilidad  
- **Contraseñas**: Entrada oculta con `pwinput`, archivo de usuarios en texto plano  

### Mantenimiento

- Los archivos de datos se encuentran en la carpeta `datos/`
- Para respaldar información, copie toda la carpeta `datos/` y el archivo `usuarios.txt`
- Para reiniciar el sistema, elimine la carpeta `datos/` y el archivo `usuarios.txt`

### Soporte

Para reportar problemas o sugerencias, contacte al administrador del sistema.

---

**Smart Easy Manager (SEM) v1.0 - 2025**  
*Sistema desarrollado para optimizar la gestión de negocios de sonidistas*