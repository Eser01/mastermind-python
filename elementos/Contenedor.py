import pygame
from . import Elemento
from otros import config

class Contenedor(Elemento):
	align = 'izquierda'

	def __init__(self, dim_ancho, dim_alto):
		self.rect = pygame.Rect(0, 0, dim_ancho, dim_alto)

	def append(self, elemento):
		if len(self.elem_hijos) == 0:
			elemento.posicion(self.rect.left, self.rect.top)
			self.elem_hijos.append(elemento)
		else:
			elem_ultimo = self.elem_hijos[-1]

			pos_left = self.rect.left
			pos_top = elem_ultimo.rect.top + elem_ultimo.rect.height + config.SEPARACION

			elemento.posicion(pos_left, pos_top)
			self.elem_hijos.append(elemento)

		if self.align == 'centro':
			abs_pos_x = self.rect.left + (self.rect.width/2)
			off_left = elemento.rect.width/2
			pos_x = abs_pos_x - off_left
			elemento.posicion(pos_x, elemento.rect.top)

	def alinear(self, align):
		self.align = align

	def dibujar(self, controlador):
		for elemento in self.elem_hijos:
			elemento.dibujar(controlador)