#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Smart Easy Manager (SEM)
Sistema de Gestión de Inventario y Cotizaciones
Para Negocio de Sonidista

Autor: Sistema SEM
Versión: 1.0
Fecha: 2025
"""

import sys
import os
from colorama import Fore, Style, init

# Agregar el directorio actual al path para importar módulos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importar módulos del sistema
from dao.functions import inicializar_sistema
from main.menu import ejecutar_menu

# Inicializar colorama para colores en Windows
init(autoreset=True)

def mostrar_bienvenida():
    """Muestra el mensaje de bienvenida al sistema"""
    print(f"{Fore.CYAN}" + "="*70)
    print(f"    🎵 SMART EASY MANAGER (SEM) 🎵")
    print(f"    Sistema de Gestión para Negocio de Sonidista")
    print(f"    Versión 1.0 - 2025")
    print("="*70 + f"{Style.RESET_ALL}")
    print(f"{Fore.WHITE}")
    print("  Funcionalidades del sistema:")
    print(f"  {Fore.GREEN}• Gestión de inventario de equipos de sonido")
    print(f"  {Fore.GREEN}• Cotizaciones automáticas con precios dinámicos")
    print(f"  {Fore.GREEN}• Control de stock con alertas")
    print(f"  {Fore.GREEN}• Registro de clientes y descuentos")
    print(f"  {Fore.GREEN}• Historial de ventas y cotizaciones")
    print(f"  {Fore.GREEN}• Cálculo automático de horas extras y transporte")
    print(f"{Style.RESET_ALL}")
    print("="*70)
    
def main():
    """Función principal del programa"""
    try:
        # Mostrar bienvenida
        mostrar_bienvenida()
        
        # Inicializar el sistema (cargar datos de archivos binarios)
        print(f"\n{Fore.YELLOW}Inicializando sistema...{Style.RESET_ALL}")
        inicializar_sistema()
        
        # Ejecutar el menú principal
        print(f"{Fore.GREEN}¡Sistema listo para usar!{Style.RESET_ALL}")
        ejecutar_menu()
        
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}Programa interrumpido por el usuario.{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Gracias por usar Smart Easy Manager (SEM){Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}Error crítico en el sistema: {e}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Contacte al administrador del sistema.{Style.RESET_ALL}")
    finally:
        print(f"\n{Fore.CYAN}Sistema finalizado.{Style.RESET_ALL}")

if __name__ == "__main__":
    # Verificar que se esté ejecutando Python 3
    if sys.version_info[0] < 3:
        print("Este programa requiere Python 3 o superior.")
        sys.exit(1)
    
    # Ejecutar programa principal
    main()