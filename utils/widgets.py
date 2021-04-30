import pygame
from PIL import Image
from utils.ImageMask import Mask, Sprite
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

class Widget:
	def __init__(self):
		pass
	def render(self, surface):
		for obj in self.objects:
			obj.render(surface)
