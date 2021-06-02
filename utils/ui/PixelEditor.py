from utils.Image import *
from utils.funcs import stripList
import pygame
import threading

class PixelEditor:
	def __init__(self, parent, pos, fill = "Transparent", Image = None, size = (0,0)):
		if Image != None and size == (0,0):
			self.Image = Image
			self.size = (Image.width, Image.height)
		elif Image == None and size != (0,0):
			self.Image = BlockTexture(size[0], size[1])
			self.size  = size

		self.parent = parent
		self.pos = pos
		self.PixelSize = 8
		self.pixelEditor = pygame.Surface((self.size[0]*self.PixelSize, self.size[1]*self.PixelSize), pygame.SRCALPHA)
		if fill == "Transparent":
			renderX = 0
			renderY = 0
			for i in range(int(self.size[0]/16)):
				renderX = 0
				for j in range(int(self.size[1]/16)):
					color = (186, 186, 186) if (i + j) % 2 != 0 else (125, 125, 125)
					pygame.draw.rect(self.pixelEditor, color, pygame.Rect(renderX, renderY, 16*self.PixelSize, 16*self.PixelSize))
					renderX += 16*self.PixelSize
				renderY += 16*self.PixelSize
		self.drawFlag = True

		self.currentColor = (0, 115, 255)

	def setPixel(self, x, y, color):
		self.Image.setPixel((x, y), color)

	def render(self):
		if self.drawFlag:
			lastY = 0
			self.renderX = 0
			self.renderY = 0
			for pixel in self.Image:
				if lastY+1 == pixel.y:
					self.renderX = 0
					self.renderY += self.PixelSize
				lastY = pixel.y
				self.renderX = int(pixel.x * self.PixelSize)
				self.setAlphaPixel(self.pixelEditor, pixel.data, int(self.PixelSize), (self.renderX, self.renderY))
			self.parent.blit(self.pixelEditor, self.pos)
			self.drawFlag = False
		else:
			self.parent.blit(self.pixelEditor, self.pos)

	def refresh(self):
		self.drawFlag = True

	def setAlphaPixel(self, surface, color, size, pos):
		alpha = pygame.Surface((size,size), pygame.SRCALPHA)
		alpha.fill(color)
		surface.blit(alpha, pos)
		# del aplha

	def clear(self, color):
		self.Image = self.Image.fill(color)
		self.drawFlag = True

	def pixelIndex(self, pos):
		index = [0,0]
		if pos[0] > self.pos[0] and pos[0] < self.pos[0]+self.size[0]*self.PixelSize and pos[1] > self.pos[1] and pos[1] < self.pos[1]+self.size[1]*self.PixelSize:
			x = 0
			while x<self.size[0]:
				startPos = int(x*self.PixelSize)
				endPos = int((x+1)*self.PixelSize)
				if pos[0] <= endPos+self.pos[0] and pos[0] >= startPos+self.pos[0]:
					index[0] = x
					break
				x+=1
			y = 0
			while y<self.size[1]:
				startPos = int(y*self.PixelSize)
				endPos = int((y+1)*self.PixelSize)
				if pos[1] <= endPos+self.pos[1] and pos[1] >= startPos+self.pos[1]:
					index[1] = y
					break
				y+=1
			return index
		return False

	def update(self, events):
		if pygame.mouse.get_pressed()[0]:
			pos = pygame.mouse.get_pos()
			index = self.pixelIndex(pos)
			if index:
				self.setPixel(index[0], index[1], self.currentColor)
				self.refresh()
		self.render()

	def colorPickingWindow(self, pos, surface):
		pass

