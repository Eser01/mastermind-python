class Elemento:
	rect = None
	elem_hijos = []
	elem_padre = None

	is_mouse_in = False
	is_mouse_out = False
	is_mouse_up = False
	is_mouse_down = False

	on_click = None

	def colision(self, mouse_position):
		return self.rect.collidepoint(mouse_position)

	def posicion(self, left, top):
		self.rect.top = top
		self.rect.left = left

	def MouseIn(self, event):
		self.is_mouse_in = True
		self.is_mouse_out = False

	def MouseOut(self, event):
		self.is_mouse_in = False
		self.is_mouse_out = True

	def MouseUp(self, event):
		self.is_mouse_up = True
		self.is_mouse_down = False
		if self.on_click and self.is_mouse_in:
			return self.on_click(event)

	def MouseDown(self, event):
		self.is_mouse_up = False
		self.is_mouse_down = True

	def onClick(self, func):
		self.on_click = func
