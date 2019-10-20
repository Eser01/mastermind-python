import pygame
from . import Vista
import otros.config

from otros.colores import blanco

from elementos.Contenedor import Contenedor
from elementos.Boton import Boton
from elementos.Imagen import Imagen

class MenuPrincipal(Vista):
	contenedor = None
	elementos = []

	def __init__(self):
		self.contenedor = Contenedor(620, 310)
		self.contenedor.posicion(5, 80)
		self.contenedor.alinear('centro')

		logo = Imagen(150, 140, 'imagenes/logo.png')
		logo.ajustarImagen()
		self.contenedor.append(logo)
		self.elementos.append(logo)

		btn1 = self.crear_boton_estandar('Juego PvC')
		btn1.onMouseDown(self.boton_modojugador1)

		btn2 = self.crear_boton_estandar('Juego PvP')
		btn2.onMouseDown(self.boton_modojugador2)

		btn3 = self.crear_boton_estandar(u'Configuración')
		btn3.onMouseDown(self.boton_configuracion)

		btn4 = self.crear_boton_estandar('Salir')
		btn4.onMouseDown(self.boton_salir)

	def crear_boton_estandar(self, texto):
		btn = Boton(150, 32, texto)
		self.elementos.append(btn)
		self.contenedor.append(btn)
		return btn

	def boton_modojugador1(self, event):
		print('Click: Modo Jugador 1')

	def boton_modojugador2(self, event):
		print('Click: Modo Jugador 2')

	def boton_configuracion(self, event):
		print('Click: Configuracion')

	def boton_salir(self, event):
		print('Click: Salir')

	def dibujar(self, controlador):
		controlador.ventana.fill(blanco)
		self.contenedor.dibujar(controlador)

	def MouseMotion(self, event):
		for elemento in self.elementos:
			if elemento.colision(event.pos):
				elemento.MouseIn(event)
			else:
				elemento.MouseOut(event)
		return True

	def MouseButtonUp(self, event):
		for elemento in self.elementos:
			if elemento.colision(event.pos):
				elemento.MouseUp(event)
				return True
		return None

	def MouseButtonDown(self, event):
		for elemento in self.elementos:
			if elemento.colision(event.pos):
				elemento.MouseDown(event)
				return True
		return None

