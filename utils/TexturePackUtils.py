from utils.Image import BlockTexture, ModelTexture, EntityTexture

class TexturePack:
	def __init__(self, order, defaultTexturePackPath):
		self.order = order
		self.path = defaultTexturePackPath
		self.models = []
		self.blockStates = {}
		self.animated = {}

	def loadFolder(self):
		pass
