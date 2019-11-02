import pygame
from pygame.locals import *
from otros import config
from singleton import Singleton
from signals import signals

# Este objeto se encarga de controlar todos los eventos
# de la ventana, carga las vistas y les pasa los eventos
# a estas
class Controlador(metaclass=Singleton):
	# Ventana de PyGame
	ventana = None

	# Dimension de la ventana
	SCREENRECT = Rect(0, 0, config.VENTANA_ANCHO, config.VENTANA_ALTO)

	# Objeto Font de PyGame
	font = None

	# Vista que actualmente se esta mostrando en la ventana
	vista_actual = None

	# Estado de la musica: False = En pausa; True = Repoduciendose
	estado_musica = False

	# "Almacen" de las vistas
	vistas = {}

	# Inicializar todas las funcionalidades del juego
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
	
	# Comenzar el reloj que permite lanzar y recibir
	# eventos del juego
	def clock(self, nombre_vista):
		VistaActual = self.vistas[nombre_vista]
		self.vista_actual = VistaActual(config.VENTANA_ANCHO, config.VENTANA_ALTO)
		if self.ventana:
			# Dibujar por primera vez
			self.vista_actual.dibujar(self)
			pygame.display.update()

			clock = pygame.time.Clock()
			flag = True
			redibujar = None
			while flag and self.vista_actual:
				# Verificar señal de termino en el bus de memorie
				if signals.comprobar('cerrar-programa'):
					flag = False
					break

				# Verificar todos los eventos que esten almacenados
				# para pasar algunos (Mouse y Key) a la vista
				# actualmente funcionando
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						flag = False
						break

					elif event.type == pygame.KEYUP:
						redibujar = self.vista_actual._KeyUp(event)

					elif event.type == pygame.KEYDOWN:
						redibujar = self.vista_actual._KeyDown(event)

					elif event.type == pygame.ACTIVEEVENT:
						redibujar = self.vista_actual._WindowActivation(event)

					elif event.type == pygame.MOUSEMOTION:
						redibujar = self.vista_actual._MouseMotion(event)

					elif event.type == pygame.MOUSEBUTTONUP:
						redibujar = self.vista_actual._MouseButtonUp(event)

					elif event.type == pygame.MOUSEBUTTONDOWN:
						redibujar = self.vista_actual._MouseButtonDown(event)

				# Si se ejecuto el evento QUIT o se apreto la tecla ESC
				if flag == False:
					break

				# Redibujar vista en caso de que se haya cambiado algun
				# elemento / o cerrar terminar el programa en caso de
				# una señar "False"
				if redibujar:
					self.vista_actual.dibujar(self)
					pygame.display.update()
					redibujar = None

				# Pausar por 40ms para no congelar el PC
				clock.tick(40)

			# La ventana se cierra correctamente
			if self.estado_musica:
				pygame.mixer.music.pause()
			return True

		# No existe ventana para abrir
		return None

	# Guarda una vista dentro del controlador
	def registrarVista(self, nombre, vista):
		self.vistas[nombre] = vista

	# Empieza a reproducir la musica de fondo
	def music(self):
		# Copyright: https://www.youtube.com/watch?v=w1MYuE1eZVo
		pygame.mixer.music.load('sonidos/gravity_sound.mp3')
		pygame.mixer.music.play(-1)
		self.estado_musica = True

	# Cierra todo el modulo pygame
	def quit(self):
		pygame.time.wait(50)
		pygame.quit()
