import pygame
import colores

def Boton(controlador, pos_izquierda, pos_arriba, ancho, alto, texto):
	# crear rectangulo del boton
	posicion_rectangulo = (pos_izquierda, pos_arriba)
	dimensiones = (ancho, alto)
	rectangulo = pygame.draw.rect(controlador.ventana, colores.azur, (posicion_rectangulo, dimensiones))
	
	# crear texto del boton
	text = controlador.font.render(texto, True, colores.blanco)
	
	# colocar texto del boton centrado en el rectangulo
	textRect = text.get_rect()
	pos_txt_arriba = pos_arriba + (alto/2) - (textRect.height/2)
	pos_txt_izquierda = pos_izquierda + (ancho/2) - (textRect.width/2)
	posicion_texto = (pos_txt_izquierda, pos_txt_arriba)

	# mostrar texto en la ventana
	controlador.ventana.blit(text, posicion_texto)