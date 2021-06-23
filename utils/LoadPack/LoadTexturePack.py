from utils.Image import *
import os

from utils.LoadPack.BountifulUpdate import TexturePack as COINS

class LoadTexturePack:
	def __init__(self, order, version):
		if version == 1.8:
			self.textures = COINS(order)

		self.files = {}
		self.load()

	def load(self):
		self.files = self.textures.loadTextureFolder()


