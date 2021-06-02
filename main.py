import pygame
from utils.ui.cursor import Cursor
from utils.ui.PixelEditor import *
import numpy as np

pygame.init()
Window = pygame.display.set_mode((500,500), pygame.SRCALPHA)
pygame.display.set_caption("Minecraft Texture Pack Maker")
clock = pygame.time.Clock()

Bruh = False

cursor = Cursor(r"./textures/cursors/Normal.png", r"./textures/cursors/MouseClick/", Window)

s = 32

editorWindow = PixelEditor(Window, (100,100), size = (s,s))
editorWindow.refresh()

pygame.key.set_repeat(2,100)

pygame.mouse.set_visible(False)
while not Bruh:
	clock.tick(60)
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			Bruh = True

	Window.fill((0,0,0,255))
	editorWindow.update(events)
	cursor.update(events)
	pygame.display.flip()