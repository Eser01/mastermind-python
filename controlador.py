import pygame
from pygame.locals import *

# QUIT None
# ACTIVEEVENT gain, state
# KEYDOWN unicode, key, mod
# KEYUP key, mod
# MOUSEMOTION pos, rel, buttons
# MOUSEBUTTONUP pos, button
# MOUSEBUTTONDOWN pos, button
# JOYAXISMOTION joy, axis, value
# JOYBALLMOTION joy, ball, rel
# JOYHATMOTION joy, hat, value
# JOYBUTTONUP joy, button
# JOYBUTTONDOWN joy, button
# VIDEORESIZE size, w, h
# VIDEOEXPOSE None
# USEREVENT Code

class Controlador:
	ventana = None
	ventana_ancho = 640
	ventana_alto = 480
	SCREENRECT = Rect(0, 0, ventana_ancho, ventana_alto)
	font = None

	def init(self, ventana_titulo='Mastermind'):
		# Inicializar PyGame
		if pygame.get_sdl_version()[0] == 2:
			pygame.mixer.pre_init(44100, 32, 2, 1024)
		pygame.init()
		if pygame.mixer and not pygame.mixer.get_init():
			print("Warning, no sound")
			pygame.mixer = None

		# Crear ventana
		winstyle = 0  # |FULLSCREEN
		bestdepth = pygame.display.mode_ok(self.SCREENRECT.size, winstyle, 32)
		self.ventana = pygame.display.set_mode(self.SCREENRECT.size, winstyle, bestdepth)

		# Vefinir fuente a utilizar en la ventana
		default_font = pygame.font.get_default_font()
		self.font = pygame.font.Font(default_font, 16)

		# Cambiar titulo de la ventana
		pygame.display.set_caption(ventana_titulo)
	
	def clock(self, fn=None):
		if self.ventana:
			clock = pygame.time.Clock()
			flag = True
			while flag:
				if fn:
					fn()
					pygame.display.update()
				for event in pygame.event.get():
					print(event)
					if event.type == pygame.QUIT:
						flag = False
						break
					elif event.type == pygame.KEYUP:
						if event.key == 27:
							flag = False
							break
						else:
							pass
				clock.tick(40)
			return True
		return None

	def quit(self):
		pygame.time.wait(100)
		pygame.quit()
