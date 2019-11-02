class Evento:
	tipo = None
	propagar = True
	redibujar = True
	data = None
	_original = None

	def __init__(self, event, tipo, data):
		self._original = event
		self.tipo = tipo
		self.data = data
	
	def noPropagar(self):
		self.propagar = False

	def noRedibujar(self):
		self.redibujar = False