from utils.Image import *
import os
import json

class TexturePack:
	def __init__(self, path):
		self.texturePath = os.path.join(path, "/assets/minecraft/textures")
		self.optifinePath = os.path.join(path, "/assets/minecraft/optifine")
		self.textPath = os.path.join(path, "/assets/minecraft/texts")
		self.modelPath = os.path.join(path, "/assets/minecraft/models")
		self.languagePath = os.path.join(path, "/assets/minecraft/lang")
		self.blockStatesPath = os.path.join(path, "/assets/minecraft/blockstates")
		self.fontPath = os.path.join(path, "/assets/minecraft/font")

		self.details = json.load(f.open(r"./dataValues/JSONs/1.8.9.json"))

	def loadTextureFolder(self):
		availableOptions = os.listdir(self.texturePath)
		for option in availableOptions

