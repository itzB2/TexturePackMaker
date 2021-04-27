from pygame import Surface
import pygame
from PIL import Image
import numpy as np

pygame.init()

class Sprite():
	def __init__(self, surface=None, PilImage=None):
		self.s = surface
		self.P = PilImage

	@property
	def surface(self):
		if self.s != None:
			return self.s
		elif self.P != None:
			return pygame.image.fromstring(self.P.tobytes(), self.P.size, self.P.mode).convert()
		else:
			raise Exception("No Inputs u Moron")

	@property
	def PilImage(self):
		if self.s != None:
			imgdata = pygame.surfarray.array3d(self.s)
			return Image.fromarray(imgdata)
		elif self.P != None:
			return self.p
		else:
			raise Exception("No Inputs u Moron")

class Mask():
	def __init__(self, shape):
		self.s = shape

	def maskSurface(self, surface):
		s = Sprite(surface = surface)
		if str(type(self.s)) == "<class \'PIL.JpegImagePlugin.JpegImageFile\'>":
			m = Sprite(PilImage = self.s)
		elif str(type(self.s)) == "<class \'pygame.Surface\'>":
			m = Sprite(surface = self.s)

		image = np.array(s.PilImage)
		MaskImage = np.array(m.PilImage).T
		print(len(image), len(MaskImage), len(image[0]), len(MaskImage[0]))
		return Sprite(PilImage = Image.fromarray(np.dstack((image,MaskImage))))

	def maskImage(self, image):
		if str(type(self.s)) == "<class \'PIL.JpegImagePlugin.JpegImageFile\'>":
			m = Sprite(PilImage = self.s)
		elif str(type(self.s)) == "<class \'pygame.Surface\'>":
			m = Sprite(surface = self.s)

		image = np.array(image)
		MaskImage = np.array(m.PilImage).T
		print(len(image), len(MaskImage), len(image[0]), len(MaskImage[0]))
		return Sprite(PilImage = Image.fromarray(np.dstack((image,MaskImage))))

