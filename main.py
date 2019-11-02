#!/usr/bin/python
# -*- coding: utf8 -*-

# Ocultar mensaje de bienvenida de PyGame
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

# SubComponentes del programa
from controlador import Controlador

# Vistas
from vistas.MenuPrincipal import MenuPrincipal

# Crear controlador, Iniciar, cargar la vista del menu principal, y mecanismo de cierre
controlador = Controlador()

controlador.registrarVista('menu-principal', MenuPrincipal)

controlador.init()
controlador.music()
clock = controlador.clock('menu-principal')
controlador.quit()