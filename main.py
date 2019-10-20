#!/usr/bin/python
# -*- coding: utf8 -*-

# Ocultar mensaje de bienvenida de PyGame
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

# SubComponentes del programa
from controlador import Controlador
from vistas.MenuPrincipal import MenuPrincipal
from otros import config

# Vista del Menu Principal
vista_inicial = MenuPrincipal(config.VENTANA_ANCHO, config.VENTANA_ALTO)
vista_inicial2 = MenuPrincipal(config.VENTANA_ANCHO, config.VENTANA_ALTO)
vista_inicial3 = MenuPrincipal(config.VENTANA_ANCHO, config.VENTANA_ALTO)

# Crear controlador, Iniciar, cargar la vista del menu principal, y mecanismo de cierre
controlador = Controlador()
controlador.init()
controlador.music()
clock = controlador.clock(vista_inicial)
controlador.quit()