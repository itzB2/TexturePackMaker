import pygame
from utils.ui.cursor import Cursor
from utils.ui.Listview import ListView
import numpy as np

pygame.init()
# Window = pygame.display.set_mode((1520,768), pygame.SRCALPHA)
Window = pygame.display.set_mode((600,600), pygame.SRCALPHA)
pygame.display.set_caption("Minecraft Texture Pack Maker")
clock = pygame.time.Clock()

Bruh = False

def ya_yeet(self, val, ind):
	print(val, ind)

cursor = Cursor(r"./textures/cursors/Normal.png", r"./textures/cursors/MouseClick/", Window)

listView = ListView((0, 0), (200,150), 1, ["Chiseled Deepslate", "Cracked Deepslate Bricks", "Deepslate Bricks", "Cracked Deepslate Tiles", "Deepslate Tiles", "Polished Deepslate", "Cobbled Deepslate"], ya_yeet)

pygame.key.set_repeat(1,100)

pygame.mouse.set_visible(False)
while not Bruh:
	clock.tick(60)
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			Bruh = True

	Window.fill((0,0,0,255))
	listView.update(events, Window)
	cursor.update(events)
	pygame.display.flip()