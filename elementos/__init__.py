class Elemento:
	rect = None
	elem_hijos = []
	elem_padre = None

	is_mouse_in = False
	is_mouse_out = False
	is_mouse_up = False
	is_mouse_down = False

	on_mouse_in = None
	on_mouse_out = None
	on_mouse_up = None
	on_mouse_down = None

	def colision(self, mouse_position):
		return self.rect.collidepoint(mouse_position)

	def posicion(self, left, top):
		self.rect.top = top
		self.rect.left = left

	def MouseIn(self, event):
		is_mouse_in = True
		is_mouse_out = False
		if self.on_mouse_in:
			self.on_mouse_in(event)

	def onMouseIn(self, func):
		self.on_mouse_in = func

	def MouseOut(self, event):
		is_mouse_in = False
		is_mouse_out = True
		if self.on_mouse_out:
			self.on_mouse_out(event)

	def onMouseOut(self, func):
		self.on_mouse_out = func

	def MouseUp(self, event):
		is_mouse_up = True
		is_mouse_down = False
		if self.on_mouse_up:
			self.on_mouse_up(event)

	def onMouseUp(self, func):
		self.on_mouse_up = func

	def MouseDown(self, event):
		is_mouse_up = False
		is_mouse_down = True
		if self.on_mouse_down:
			self.on_mouse_down(event)

	def onMouseDown(self, func):
		self.on_mouse_down = func
