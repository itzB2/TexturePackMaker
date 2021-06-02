from utils.Mask import *
from utils.widgetUtils import *
from utils.funcs import *

class Label(Widget):
	def __init__(self, pos, size, text):
		self.pos = pos
		self.size = size
		self.text = text
		self.visible = True
		self.object = Text(self.text,'./textures/16x.ttf', self.size*8, [pos[0]+8, pos[1]+8])

	def update(self, surface):
		if self.visible:
			self.object.render(surface)
