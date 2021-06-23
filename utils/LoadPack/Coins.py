from utils.Image import *
from utils.TexturePackUtils import TexturePack
import os
import json

class TexturePack(TexturePack):
	def __init__(self, order):
		self.order = order
		super().__init__(order, "./textures/TexturePacks/DefaultTextures/1.8")
		self.models = []

	def loadTextureFolder(self):
		pass

	@property
	def textures(self):
		pass

