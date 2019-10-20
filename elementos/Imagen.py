import pygame
from . import Elemento

class Imagen(Elemento):
	imagen = None
	imagen_rect = None
	#color_fondo = colores.azur

	def __init__(self, dim_ancho, dim_alto, imagen):
		self.rect = pygame.Rect(0, 0, dim_ancho, dim_alto)
		self.imagen = pygame.image.load(imagen)
		self.imagen_rect = self.imagen.get_rect()

	def ajustarImagen(self, ajuste_tipo='contener'): # contener, cubrir, calzar
		if ajuste_tipo == 'contener':
			h_proporcion = self.imagen_rect.height / self.rect.height
			w_proporcion = self.imagen_rect.width / self.rect.width
			if (w_proporcion <= 1 and h_proporcion > 1) or (h_proporcion > 1 and w_proporcion > 1 and h_proporcion > w_proporcion):
				inverso = h_proporcion**(-1)
				dimensiones = ( round(self.imagen_rect.width*inverso), round(self.imagen_rect.height*inverso) )
				self.imagen = pygame.transform.scale(self.imagen, dimensiones)
				self.imagen_rect = self.imagen.get_rect()
			elif (h_proporcion <= 1 and w_proporcion > 1) or (h_proporcion > 1 and w_proporcion > 1 and w_proporcion > h_proporcion):
				inverso = w_proporcion**(-1)
				dimensiones = ( self.imagen_rect.width*inverso, self.imagen_rect.height*inverso )
				self.imagen = pygame.transform.scale(self.imagen, dimensiones)
				self.imagen_rect = self.imagen.get_rect()

		elif ajuste_tipo == 'cubrir':
			h_proporcion = self.imagen_rect.height / self.rect.height
			w_proporcion = self.imagen_rect.width / self.rect.width
			if (h_proporcion < 1 and w_proporcion >= 1) or (h_proporcion < 1 and w_proporcion < 1 and h_proporcion < w_proporcion):
				inverso = h_proporcion**(-1)
				dimensiones = ( self.imagen_rect.width*inverso, self.imagen_rect.height*inverso )
				self.imagen = pygame.transform.scale(self.imagen, dimensiones)
				self.imagen_rect = self.imagen.get_rect()
			elif (w_proporcion < 1 and h_proporcion >= 1) or (h_proporcion < 1 and w_proporcion < 1 and w_proporcion < h_proporcion):
				inverso = w_proporcion**(-1)
				dimensiones = ( self.imagen_rect.width*inverso, self.imagen_rect.height*inverso )
				self.imagen = pygame.transform.scale(self.imagen, dimensiones)
				self.imagen_rect = self.imagen.get_rect()

		elif ajuste_tipo == 'calzar':
			if (self.imagen_rect.width != self.rect.width) or (self.imagen_rect.height != self.rect.height):
				dimensiones = (self.rect.width, self.rect.height)
				self.imagen = pygame.transform.scale(self.imagen, dimensiones)
				self.imagen_rect = self.imagen.get_rect()
	
	def dibujar(self, controlador):
		pos_x = self.rect.left + (self.rect.width/2) - (self.imagen_rect.width/2)
		pos_y = self.rect.top + (self.rect.height/2) - (self.imagen_rect.height/2)
		controlador.ventana.blit(self.imagen, (pos_x, pos_y))