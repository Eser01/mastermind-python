import pygame
from otros import colores
from . import Elemento

class Boton(Elemento):
	texto = None
	color_fondo = colores.azur
	color_texto = colores.blanco

	def __init__(self, dim_ancho, dim_alto, texto):
		self.rect = pygame.Rect(0, 0, dim_ancho, dim_alto)
		self.texto = texto

	def definirColores(self, fondo, texto):
		self.color_fondo = fondo
		self.color_texto = texto
	
	def dibujar(self, controlador):
		# crear rectangulo del boton
		rectangulo = pygame.draw.rect(controlador.ventana, self.color_fondo, self.rect)
		
		# crear texto del boton
		text = controlador.font.render(self.texto, True, self.color_texto)
		
		# colocar texto del boton centrado en el rectangulo
		textRect = text.get_rect()
		pos_txt_arriba = self.rect.top + (self.rect.height/2) - (textRect.height/2)
		pos_txt_izquierda = self.rect.left + (self.rect.width/2) - (textRect.width/2)
		posicion_texto = (pos_txt_izquierda, pos_txt_arriba)

		# mostrar texto en la ventana
		controlador.ventana.blit(text, posicion_texto)

	def MouseIn(self, event):
		super().MouseIn(event)
		self.color_fondo = colores.azur_light

	def MouseOut(self, event):
		super().MouseOut(event)
		self.color_fondo = colores.azur

	def MouseUp(self, event):
		super().MouseUp(event)
		if self.is_mouse_in:
			self.color_fondo = colores.azur_light
		else:
			self.color_fondo = colores.azur

	def MouseDown(self, event):
		super().MouseDown(event)
		self.color_fondo = colores.azur_dark
		