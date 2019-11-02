# Clases y modulos externos
import pygame

# Clases y modulos internos
from vistas import Vista
from singleton import Singleton
from signals import signals

# Configuraciones y Constantes del programa
from otros import config
from otros.colores import blanco

# Elementos para la interfaz
from elementos.Contenedor import Contenedor
from elementos.Boton import Boton
from elementos.Imagen import Imagen


# Definicion de la Vista "Menu Principal"
class MenuPrincipal(Vista, metaclass=Singleton):
	fondo = None
	contenedor = None

	# Se ejecuta cuando se presiona una tecla mientras la ventana del juego esta activa
	def evento_keyup(self, evento):
		if evento.data.key == 27:
			print('Tecla: ESC')
			signals.cerrarPrograma()

	# Esta funcion se ejecuta cuando se hace click en el boton "Juego PvC"
	def boton_modojugador1(self, event):
		print('Click: Modo Jugador 1')

	# Esta funcion se ejecuta cuando se hace click en el boton "Juego PvP"
	def boton_modojugador2(self, event):
		print('Click: Modo Jugador 2')

	# Esta funcion se ejecuta cuando se hace click en el boton "Configuración"
	def boton_configuracion(self, event):
		print('Click: Configuracion')

	# Esta funcion se ejecuta cuando se hace click en el boton "Salir"
	def boton_salir(self, event):
		print('Click: Salir')
		signals.cerrarPrograma()

	# Metodo para crear rapidamente un boton (ver "__init__")
	def crear_boton_estandar(self, texto, click=None):
		btn = Boton(150, 32, texto)
		if click:
			btn.onClick(click)
		self.nuevoElemento(btn)
		self.contenedor.append(btn)
		return btn

	# Inicializacion de la Vista
	def __init__(self, ventana_ancho, ventana_alto):
		self.fondo = pygame.image.load('imagenes/fondo1.jpg')
		self.fondo_rect = self.fondo.get_rect()
		if self.fondo_rect.width >= ventana_ancho and self.fondo_rect.height >= ventana_alto:
			pos_y = (self.fondo_rect.height - ventana_alto)/2
			pos_x = (self.fondo_rect.width - ventana_ancho)/2
			chop_rect = pygame.Rect(pos_x, pos_y, ventana_ancho, ventana_alto)
			self.fondo = self.fondo.subsurface(chop_rect)
			self.fondo_rect = self.fondo.get_rect()

		# Crear el elemento contenedor de los sub-elementos
		ventana_ancho -= config.SEPARACION*2
		ventana_alto -= config.SEPARACION*2

		self.contenedor = Contenedor(ventana_ancho, ventana_alto)
		self.contenedor.posicion(config.SEPARACION, 80)
		self.contenedor.alinear('centro')

		# Crear la imagen de logo y colocarla en la ventana
		logo = Imagen(150, 140, 'imagenes/logo.png')
		logo.ajustarImagen()
		self.contenedor.append(logo)
		self.nuevoElemento(logo)

		# Crear botones y asignar acciones cuando se les haga click
		self.crear_boton_estandar('Juego PvC', click=self.boton_modojugador1)
		self.crear_boton_estandar('Juego PvP', click=self.boton_modojugador2)
		self.crear_boton_estandar(u'Configuración', click=self.boton_configuracion)
		self.crear_boton_estandar('Salir', click=self.boton_salir)

		# Registrar otro tipo de eventos
		self.registrarEvento('keyup', self.evento_keyup)
