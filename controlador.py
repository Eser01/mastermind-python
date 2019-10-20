import pygame
from pygame.locals import *
from otros import config

class Controlador:
	ventana = None
	SCREENRECT = Rect(0, 0, config.VENTANA_ANCHO, config.VENTANA_ALTO)
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
	
	def clock(self, vista_inicial):
		if self.ventana:
			# Dibujar por primera vez
			vista_inicial.dibujar(self)
			pygame.display.update()

			clock = pygame.time.Clock()
			flag = True
			redibujar = None
			while flag:
				# Verificar todos los eventos que esten almacenados
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						flag = False
						break

					elif event.type == pygame.KEYUP:
						if event.key == 27:
							flag = False
							break
						else:
							pass

					elif event.type == pygame.MOUSEMOTION:
						redibujar = vista_inicial.MouseMotion(event)

					elif event.type == pygame.MOUSEBUTTONUP:
						redibujar = vista_inicial.MouseButtonUp(event)

					elif event.type == pygame.MOUSEBUTTONDOWN:
						redibujar = vista_inicial.MouseButtonDown(event)

				# Redibujar vista en caso de que se haya cambiado algun elemento / o cerrar terminar el programa en caso de una señar "False"
				if redibujar:
					vista_inicial.dibujar(self)
					pygame.display.update()
					redibujar = None
				elif redibujar == False:
					flag = False
					vista_inicial.dibujar(self)
					pygame.display.update()
					redibujar = None

				# Pausar por 40ms para no congelar el PC
				clock.tick(40)

			# La ventana se cierra correctamente
			return True

		# No existe ventana para abrir
		return None

	def quit(self):
		pygame.time.wait(100)
		pygame.quit()

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