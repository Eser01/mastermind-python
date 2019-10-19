#!/usr/bin/python
# -*- coding: utf8 -*-

from controlador import Controlador
from otros.boton import Boton
from otros.colores import blanco

controlador = Controlador()

def mostrar_boton():
	controlador.ventana.fill(blanco)
	Boton(controlador, 10, 10, 150, 32, 'Juego PvC')
	Boton(controlador, 10, 52, 150, 32, 'Juego PvP')
	Boton(controlador, 10, 94, 150, 32, u'Configuración')
	Boton(controlador, 10, 136, 150, 32, 'Salir')

controlador.init()
clock = controlador.clock(mostrar_boton)
controlador.quit()