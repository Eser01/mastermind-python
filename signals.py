from singleton import Singleton

class Signals(metaclass=Singleton):
	_cerrar_programa = False

	def comprobar(self, signal):
		if signal == 'cerrar-programa':
			return self._cerrar_programa
		return None

	def cerrarPrograma(self):
		self._cerrar_programa = True

signals = Signals()