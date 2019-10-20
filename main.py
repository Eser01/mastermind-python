#!/usr/bin/python
# -*- coding: utf8 -*-

from controlador import Controlador
from vistas.MenuPrincipal import MenuPrincipal

vista_inicial = MenuPrincipal()

controlador = Controlador()
controlador.init()
clock = controlador.clock(vista_inicial)
controlador.quit()