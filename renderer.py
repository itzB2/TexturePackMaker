import pygame
from utils.ui.cursor import Cursor
from utils.ui.Listview import ListView
import numpy as np

class Renderer:
	def __init__(self):
		pass

	def init(self):
		pygame.init()
		# Window = pygame.display.set_mode((1520,768), pygame.SRCALPHA)
		self.Window = pygame.display.set_mode((600,600), pygame.SRCALPHA)
		pygame.display.set_caption("Minecraft Texture Pack Maker")
		self.clock = pygame.time.Clock()

		self.Bruh = False
		self.cursor = Cursor(r"./textures/cursors/Normal.png", r"./textures/cursors/MouseClick/", self.Window)
		pygame.key.set_repeat(1,100)
		pygame.mouse.set_visible(False)

	def render(self):
		while not self.Bruh:
			self.clock.tick(60)
			events = pygame.event.get()
			for event in events:
				if event.type == pygame.QUIT:
					self.Bruh = True

			self.Window.fill((0,0,0,255))
			self.cursor.update(events)
			pygame.display.flip()