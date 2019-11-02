from eventos import Evento

class Vista:
	contenedor = None
	elementos = []

	_keyup_funcs = []
	_keydown_funcs = []
	_windowactivation_funcs = []

	def dibujar(self, controlador):
		controlador.ventana.blit(self.fondo, self.fondo_rect)
		self.contenedor.dibujar(controlador)

	def nuevoElemento(self, elemento):
		self.elementos.append(elemento)

	def registrarEvento(self, evento_tipo, evento_func):
		if evento_tipo == 'keyup':
			self._keyup_funcs.append(evento_func)
		elif evento_tipo == 'keydown':
			self._keydown_funcs.append(evento_func)
		elif evento_tipo == 'windowactivation':
			self._windowactivation_funcs.append(evento_func)

	def _MouseMotion(self, event):
		# MOUSEMOTION pos, rel, buttons
		ev = Evento(event, 'mousemotion', event)
		for elemento in self.elementos:
			if elemento.colision(event.pos):
				ev.tipo = 'mousein'
				elemento.MouseIn(ev)
			else:
				ev.tipo = 'mouseout'
				elemento.MouseOut(event)
		return True

	def _MouseButtonUp(self, event):
		# MOUSEBUTTONUP pos, button
		ev = Evento(event, 'mouseup', event)
		for elemento in self.elementos:
			if elemento.colision(event.pos):
				elemento.MouseUp(ev)
				return ev.redibujar
		return False

	def _MouseButtonDown(self, event):
		# MOUSEBUTTONDOWN pos, button
		ev = Evento(event, 'mousedown', event)
		for elemento in self.elementos:
			if elemento.colision(event.pos):
				elemento.MouseDown(ev)
				return ev.redibujar
		return False

	def _KeyUp(self, event):
		# KEYUP key, mod
		if len(self._keyup_funcs) > 0:
			ev = Evento(event, 'keyup', event)
			redibujar = True
			for func in self._keyup_funcs:
				func(ev)
				if ev.redibujar == False:
					redibujar = False
			return redibujar
		return None

	def _KeyDown(self, event):
		# KEYDOWN unicode, key, mod
		if len(self._keydown_funcs) > 0:
			ev = Evento(event, 'keydown', event)
			redibujar = True
			for func in self._keydown_funcs:
				func(ev)
				if ev.redibujar == False:
					redibujar = False
			return redibujar
		return None

	def _WindowActivation(self, event):
		# ACTIVEEVENT gain, state
		if len(self._windowactivation_funcs) > 0:
			ev = Evento(event, 'windowactivation', event)
			redibujar = True
			for func in self._windowactivation_funcs:
				func(ev)
				if ev.redibujar == False:
					redibujar = False
			return redibujar
		return None

# QUIT None
# JOYAXISMOTION joy, axis, value
# JOYBALLMOTION joy, ball, rel
# JOYHATMOTION joy, hat, value
# JOYBUTTONUP joy, button
# JOYBUTTONDOWN joy, button
# VIDEORESIZE size, w, h
# VIDEOEXPOSE None
# USEREVENT Code