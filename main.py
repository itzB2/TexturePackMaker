import pygame
from utils.ui.cursor import Cursor
from utils.ui.Listview import ListView, CustomView, CustomViewLoader
import numpy as np

pygame.init()
Window = pygame.display.set_mode((500,500), pygame.SRCALPHA)
pygame.display.set_caption("Minecraft Texture Pack Maker")
clock = pygame.time.Clock()

Bruh = False

cursor = Cursor(r"./textures/cursors/Normal.png", r"./textures/cursors/MouseClick/", Window)

def action(self, val, ind):
	print(self.pos, val, ind)

class BlockSelector(CustomView):
	pass

class BlockSelectorLoader(CustomViewLoader):
	pass

customView = BlockSelector()
customViewLoader = BlockSelectorLoader(customView, "Gold Ingot, minecraft:gold_ingot, 266, 0;")
listView = ListView(customViewLoader, (0,0), action)

pygame.key.set_repeat(1,100)

pygame.mouse.set_visible(False)
while not Bruh:
	clock.tick(60)
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			Bruh = True

	Window.fill((0,0,0,255))
	cursor.update(events)
	pygame.display.flip()