from utils.funcs import *
from Scene.SceneManager import SceneManager

class Scene():
	def __init__(self, name):
		self.objects = []
		self.window = None
		self.name = name
		self.SceneManager = 

	def addObject(self, obj, order):
		index = clamp(order, 0, len(self.objects))
		self.objects.insert(index, obj)

	def render(self, window):
		self.window = None
		for obj in self.objects:
			obj.render(window)

	@property
	def TopOrder(self):
		return len(self.objects)

	def __del__(self):
		if self.window == None:
			pass
		else:
			self.window.fill((0,0,0))
