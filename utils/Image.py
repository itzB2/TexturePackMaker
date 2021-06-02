from PIL import Image
import numpy as np

class PixelID():
	def __init__(self, data, x, y):
		self.data = data
		self.x = x
		self.y = y

	def __repr__(self):
		return f"Value: {self.data}, X Coord: {self.x}, Y Coord: {self.y}"

class BlockTexture():
	def __init__(self, width, height, pilImage = None):
		self.width = width
		self.height = height
		self.pilImage = pilImage if pilImage else Image.new(mode="RGBA", size=(width,height), color=(0,0,0,0))
		self.Pixels = self.pilImage.load()

		self.matrix = np.array(self.pilImage.getdata())

	def __iter__(self):
		self.n = 0
		return self

	def __next__(self):
		if self.n <= len(self.matrix)-1:
			result = PixelID(self.matrix[self.n], self.n%self.width, self.n//self.width)
			self.n += 1
			return result
		else:
			raise StopIteration

	def setPixel(self, coord, color):
		self.Pixels[coord[0], coord[1]] = color
		self.matrix = np.array(self.pilImage.getdata())

	def getPixel(self, coord):
		return self.pilImage.getpixel(coord)

	def setPixels(self, coords, colors):
		for coord, color in zip(coords, colors):
			self.Pixels[coord[0], coord[1]] = color
		self.matrix = np.array(self.pilImage.getdata())

	def getPixels(self, coords):
		pixels = []
		for coord in coords:
			pixels.append(self.pilImage.getpixel(coord))
		return pixels

	def fill(self, color):
		return BlockTexture(self.width, self.height, Image.new(mode="RGBA", size=(self.width,self.height), color=color))

	def save(self, path):
		self.pilImage.save(path)

