#!/usr/bin/python
# -*- coding: utf8 -*-

from controlador import Controlador
from vistas.MenuPrincipal import MenuPrincipal
from otros import config

vista_inicial = MenuPrincipal(config.VENTANA_ANCHO, config.VENTANA_ALTO)

controlador = Controlador()
controlador.init()
clock = controlador.clock(vista_inicial)
controlador.quit()