import pygame
from PIL import Image
from utils.Mask import Mask, Sprite
import time, asyncio

class Material:
	def __init__(self, color, Texture="Blank", transparent=False):
		self.t = Texture
		self.c = color
		self.transparency = transparent

	@property
	def isImage(self):
		return True if self.t != "Blank" else False

	@property
	def texture(self):
		return self.t

	@property
	def color(self):
		return self.c

	@property
	def transp(self):
		return self.transparency

	def __repr__(self):
		return f"\"Texture\" : {self.t}\n\"Color\" : {self.c}\n\"Transparency\" : {self.transp}"

class SpriteShapeAsset:
	def __init__(self, topLeft, top, topRight, bottomLeft, bottom, bottomRight, left, center, right, offsets):
		self._top = (pygame.image.load(topLeft), pygame.image.load(top), pygame.image.load(topRight))
		self._center = (pygame.image.load(left), pygame.image.load(center), pygame.image.load(right))
		self._bottom = (pygame.image.load(bottomLeft), pygame.image.load(bottom), pygame.image.load(bottomRight))
		self.offsets = offsets

	@property
	def top(self):
		return self._top
	
	@property
	def center(self):
		return self._center

	@property
	def bottom(self):
		return self._bottom

class Circle:
	def __init__(self, radius, pos, mat):
		self.r = radius
		self.p = pos
		self.m = mat
		self.type = "Circle"
		self.Ws = self.WhiteSurface
		self.maskedImage = Mask(self.Ws).maskImage(self.m.texture).surface

	@property
	def WhiteSurface(self):
		if self.m.isImage:
			surf = pygame.Surface(self.m.texture.size)
		else:
			surf = pygame.Surface((self.r+100, self.r+100))

		pygame.draw.circle(surf, (255,255,255), self.p, self.r)
		return surf

	def render(self, surface):
		if self.m.isImage:
			surface.blit(self.maskedSurface, pygame.Rect(pos[0], pos[1],self.r, self.r))
		else:
			pygame.draw.circle(surface, self.m.color, self.p, self.r)

	def refresh(self):
		self.Ws = self.WhiteSurface
		self.maskedImage = Mask(self.Ws).maskImage(self.m.texture).surface

class Square:
	def __init__(self, sideLength, pos, mat):
		self.s = sideLength
		self.p = pos
		self.m = mat
		self.type = "Square"
		self.Rect = pygame.Rect(self.p, (self.s, self.s))
		self.Ws = self.WhiteSurface
		self.surfaceTexture = Sprite(PilImage = self.m.texture).surface		

	@property
	def WhiteSurface(self):
		if self.m.isImage:
			surf = pygame.Surface(self.m.texture.size)
		else:
			surf = pygame.Surface((self.s+100, self.s+100))

		pygame.draw.rect(surf, (255,255,255), self.Rect)
		return surf

	def render(self, surface):
		if self.m.isImage:
			surface.blit(self.surfaceTexture, self.Rect)
		else:
			pygame.draw.rect(surface, self.m.color, self.Rect)

	def refresh(self):
		self.Rect = pygame.Rect(self.p, (self.s, self.s))
		self.Ws = self.WhiteSurface
		self.surfaceTexture = Sprite(PilImage = self.m.texture).surface	

class Rect:
	def __init__(self, a, b, pos, mat):
		self.a = a
		self.b = b
		self.p = pos
		self.m = mat
		m = mat
		self.type = "Rect"
		self.debug = False
		self.transp = self.m.transp
		if not self.transp and self.m.isImage:
			self.surfaceTexture = Sprite(PilImage = self.m.texture).surface
		elif self.m.isImage and self.transp:
			self.surfaceTexture = pygame.image.load(m.texture)
			self.surfaceRect = self.surfaceTexture.get_rect()
			self.surfaceRect.topright = self.p
		self.Rect = pygame.Rect(self.p, (self.a, self.b))
		self.Ws = self.WhiteSurface

	def scaleTranspTexture(self, scale):
		self.surfaceTexture = pygame.transform.scale(self.surfaceTexture, scale)
		self.surfaceRect = pygame.Rect(self.p, scale)

	def setRect(self, rect):
		self.Rect = rect

	@property
	def WhiteSurface(self):
		if self.m.isImage and not self.transp:
			surf = pygame.Surface(self.m.texture.size)
		else:
			surf = pygame.Surface((self.a+100, self.b+100))
		pygame.draw.rect(surf, (255,255,255), self.Rect)
		return surf

	def render(self, surface):
		
		if self.m.isImage and self.debug == False and not self.transp:
			surface.blit(self.surfaceTexture, self.Rect)

		elif self.m.isImage and self.debug == False and self.transp:
			surface.blit(self.surfaceTexture, self.surfaceRect)
		else:
			if self.debug == True:
				pygame.draw.rect(surface, (255,255,255), self.Rect)
			else:
				pygame.draw.rect(surface, self.m.color, self.Rect)

	def refresh(self):
		m = self.m
		self.transp = m.transp
		self.Rect = pygame.Rect(self.p, (self.a, self.b))
		if not self.transp:
			self.surfaceTexture = Sprite(PilImage = self.m.texture).surface
		else:
			self.surfaceTexture = pygame.image.load(m.texture)
			self.surfaceRect.topright = self.p
		self.Ws = self.WhiteSurface

class Text:
	def __init__(self, text, fontPath, size, pos):
		self.text = text
		self.p = fontPath
		self.size = size
		self.pos = pos
		self.type = "Text"
		font = pygame.font.Font(self.p, self.size)
		text = font.render(self.text, True, (255,255,255))
		textRect  = pygame.Rect(self.pos, (text.get_rect().width, text.get_rect().height))
		self.textObj = text
		self.textRect = textRect
		self.debug = False

	def render(self, surface):
		if not self.debug:
			surface.blit(self.textObj, self.textRect)
		else:
			pygame.draw.rect(surface, (255,255,255), self.textRect)

	def refresh(self):
		self.font = pygame.font.Font(self.p, self.size)
		self.textObj = self.font.render(self.text, True, (255,255,255))
		self.textRect  = pygame.Rect(self.pos, (self.textObj.get_rect().width, self.textObj.get_rect().height))

class SpriteShape:
	def __init__(self, length, height, Asset, objheight, objLength, pos):
		self.length = length
		self.height = height
		self.objheight = objheight
		self.objLength = objLength
		self.Asset = Asset
		self.pos = pos
		self.type = "SpriteShape"
		self.update = False

		self.objectsAlongX = self.length // self.objLength if self.length != self.objLength else 3
		self.objectsAlongXremains = self.length % self.objLength
		self.objectsAlongY = self.height // self.objheight if self.height != self.objheight else 3
		self.objectsAlongYremains = self.height % self.objheight

		self.renderX = 0
		self.renderY = 0

		self.DEBUG = False

		self.cache = pygame.Surface((length, height))

		self.objects = []
		self.refresh()

	def refresh(self):
		self.cache = pygame.Surface((self.objLength, self.objheight))

		self.objectsAlongX = ((self.objLength // self.length)-1)+3 if self.objLength // self.length != 1 else 3
		self.objectsAlongXremains = self.objLength % self.length
		self.objectsAlongY = ((self.objheight // self.height)-1)+3 if self.objheight // self.height != 1 else 3
		self.objectsAlongYremains = self.objheight % self.height

		self.update = True

		self.objects = []
		for y in range(self.objectsAlongY):
			tempX = []
			for x in range(self.objectsAlongX):
				if y == 0:
					if x == 0:
						tempX.append(self.Asset.top[0])
					elif x == self.objectsAlongX-1:
						tempX.append(self.Asset.top[2])
					else:
						tempX.append(self.Asset.top[1])
				elif y == self.objectsAlongY-1:
					if x == 0:
						tempX.append(self.Asset.bottom[0])
					elif x == self.objectsAlongX-1:
						tempX.append(self.Asset.bottom[2])
					else:
						tempX.append(self.Asset.bottom[1])
				else:
					if x == 0:
						tempX.append(self.Asset.center[0])
					elif x == self.objectsAlongX-1:
						tempX.append(self.Asset.center[2])
					else:
						tempX.append(self.Asset.center[1])									

			self.objects.append(tempX)

	def render(self, surface):
		self.renderX = 0
		self.renderY = 0
		for y, indY in zip(self.objects, range(len(self.objects))):
			lenY = len(self.objects)

			for x, indX in zip(y, range(len(y))):
				lenX = len(y)
				if indY == 0:
					if indX == 0:
						aX = self.Asset.offsets["TL"][0]
						aY = self.Asset.offsets["TL"][1]

						self.cache.blit(x, (self.renderX, self.renderY))

						self.renderX += aX
						

					elif indX+1 == self.objectsAlongX:
						aX = self.Asset.offsets["TR"][0]
						aY = self.Asset.offsets["TR"][1]

						self.cache.blit(x, (self.renderX, self.renderY))
						self.renderY += aY
					else:
						aX = self.Asset.offsets["T"][0]
						aY = self.Asset.offsets["T"][1]

						self.cache.blit(x, (self.renderX, self.renderY))

						self.renderX += aX
						
				elif indY != self.objectsAlongY-1:
					if indX == 0:
						self.renderX = 0
						aX = self.Asset.offsets["L"][0]
						aY = self.Asset.offsets["L"][1]

						self.cache.blit(x, (self.renderX, self.renderY))

						self.renderX += aX

					elif indX+1 == self.objectsAlongX:
						aX = self.Asset.offsets["R"][0]
						aY = self.Asset.offsets["R"][1]

						self.cache.blit(x, (self.renderX, self.renderY))

						self.renderX += aX
						self.renderY += aY

					else:

						aX = self.Asset.offsets["C"][0]
						aY = self.Asset.offsets["C"][1]

						self.cache.blit(x, (self.renderX, self.renderY))
						self.renderX += aX
				else:
					if indX == 0:
						self.renderX = 0
						aX = self.Asset.offsets["BL"][0]
						aY = self.Asset.offsets["BL"][1]
						self.cache.blit(x, (self.renderX, self.renderY))
						self.renderX += aX
					elif indX+1 == self.objectsAlongX:
						aX = self.Asset.offsets["BR"][0]
						aY = self.Asset.offsets["BR"][1]

						self.cache.blit(x, (self.renderX, self.renderY))
						self.renderX += aX
						self.renderY += aY

					else:
						aX = self.Asset.offsets["B"][0]
						aY = self.Asset.offsets["B"][1]

						self.cache.blit(x, (self.renderX, self.renderY))
						self.renderX += aX

		surface.blit(self.cache, self.pos)

		self.update = False

class Widget:
	def __init__(self):
		pass
	def render(self, surface):
		for obj in self.objects:
			obj.render(surface)


