import pygame
from . import VistaSingleton
from otros import config

from otros.colores import blanco

from elementos.Contenedor import Contenedor
from elementos.Boton import Boton
from elementos.Imagen import Imagen

class MenuPrincipal(VistaSingleton):
	fondo = None

	def __init__(self, ventana_ancho, ventana_alto):
		self.fondo = pygame.image.load('imagenes/fondo1.jpg')
		self.fondo_rect = self.fondo.get_rect()
		if self.fondo_rect.width >= ventana_ancho and self.fondo_rect.height >= ventana_alto:
			pos_y = (self.fondo_rect.height - ventana_alto)/2
			pos_x = (self.fondo_rect.width - ventana_ancho)/2
			chop_rect = pygame.Rect(pos_x, pos_y, ventana_ancho, ventana_alto)
			self.fondo = self.fondo.subsurface(chop_rect)
			self.fondo_rect = self.fondo.get_rect()

		ventana_ancho -= config.SEPARACION*2
		ventana_alto -= config.SEPARACION*2

		self.contenedor = Contenedor(ventana_ancho, ventana_alto)
		self.contenedor.posicion(config.SEPARACION, 80)
		self.contenedor.alinear('centro')

		logo = Imagen(150, 140, 'imagenes/logo.png')
		logo.ajustarImagen()
		self.contenedor.append(logo)
		self.elementos.append(logo)

		btn1 = self.crear_boton_estandar('Juego PvC')
		btn1.onClick(self.boton_modojugador1)

		btn2 = self.crear_boton_estandar('Juego PvP')
		btn2.onClick(self.boton_modojugador2)

		btn3 = self.crear_boton_estandar(u'Configuración')
		btn3.onClick(self.boton_configuracion)

		btn4 = self.crear_boton_estandar('Salir')
		btn4.onClick(self.boton_salir)

	def crear_boton_estandar(self, texto):
		btn = Boton(150, 32, texto)
		self.elementos.append(btn)
		self.contenedor.append(btn)
		return btn

	def boton_modojugador1(self, event):
		print('Click: Modo Jugador 1')
		return True

	def boton_modojugador2(self, event):
		print('Click: Modo Jugador 2')
		return True

	def boton_configuracion(self, event):
		print('Click: Configuracion')
		return True

	def boton_salir(self, event):
		print('Click: Salir')
		return False

