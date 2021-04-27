import pygame
from PIL import Image
from utils.ImageMask import Mask, Sprite
import time, asyncio

class Material:
	def __init__(self, color, Texture="Blank"):
		self.t = Texture
		self.c = color

	@property
	def isImage(self):
		return True if self.t != "Blank" else False

	@property
	def texture(self):
		return self.t

	@property
	def color(self):
		return self.c

class Circle:
	def __init__(self, radius, pos, mat):
		self.r = radius
		self.p = pos
		self.m = mat
		self.type = "Circle"

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
			maskedSurface = Mask(self.WhiteSurface).maskImage(self.m.texture).surface
			surface.blit(maskedSurface, pygame.Rect(pos[0], pos[1],self.r, self.r))
		else:
			pygame.draw.circle(surface, self.m.color, self.p, self.r)

class Square:
	def __init__(self, sideLength, pos, mat):
		self.s = sideLength
		self.p = pos
		self.m = mat
		self.type = "Square"

	@property
	def WhiteSurface(self):
		if self.m.isImage:
			surf = pygame.Surface(self.m.texture.size)
		else:
			surf = pygame.Surface((self.s+100, self.s+100))

		pygame.draw.rect(surf, (255,255,255), pygame.Rect(self.p, (self.s, self.s)))
		return surf

	def render(self, surface):
		if self.m.isImage:
			surface.blit(Sprite(PilImage = self.m.texture).surface, pygame.Rect(self.p[0], self.p[1],self.s, self.s))
		else:
			pygame.draw.rect(surface, self.m.color, pygame.Rect(self.p[0], self.p[1],self.s, self.s))

class Rect:
	def __init__(self, a, b, pos, mat):
		self.a = a
		self.b = b
		self.p = pos
		self.m = mat
		self.type = "Rect"

	@property
	def WhiteSurface(self):
		if self.m.isImage:
			surf = pygame.Surface(self.m.texture.size)
		else:
			surf = pygame.Surface((self.a+100, self.b+100))
		self.Rect = pygame.Rect(self.p, (self.a, self.b))
		pygame.draw.rect(surf, (255,255,255), self.Rect)
		return surf

	def render(self, surface):
		self.Rect = pygame.Rect(self.p, (self.a, self.b))
		if self.m.isImage:
			surface.blit(Sprite(PilImage = self.m.texture).surface, self.Rect)
		else:
			pygame.draw.rect(surface, self.m.color, self.Rect)

class Text:
	def __init__(self, text, fontPath, size, pos):
		self.text = text
		self.p = fontPath
		self.size = size
		self.pos = pos
		self.type = "Text"
		font = pygame.font.Font(self.p, self.size)
		text = font.render(self.text, True, (255,255,255))
		textRect  = pygame.Rect(self.pos, (text.get_rect()[0], text.get_rect()[1]))
		self.text = text
		self.textRect = textRect

	def render(self, surface):
		surface.blit(self.text, self.textRect)

class Widget:
	def __init__(self):
		pass
	def render(self, surface):
		for obj in self.objects:
			obj.render(surface)

class Animation:
	def __init__(self):
		pass
	def start(self):
		pass

