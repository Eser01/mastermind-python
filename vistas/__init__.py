class Vista:
	contenedor = None
	elementos = []

	def dibujar(self, controlador):
		controlador.ventana.blit(self.fondo, self.fondo_rect)
		self.contenedor.dibujar(controlador)

	def MouseMotion(self, event):
		for elemento in self.elementos:
			if elemento.colision(event.pos):
				elemento.MouseIn(event)
			else:
				elemento.MouseOut(event)
		return True

	def MouseButtonUp(self, event):
		for elemento in self.elementos:
			if elemento.colision(event.pos):
				return elemento.MouseUp(event)
		return None

	def MouseButtonDown(self, event):
		for elemento in self.elementos:
			if elemento.colision(event.pos):
				elemento.MouseDown(event)
				return True
		return None