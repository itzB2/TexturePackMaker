import pygame
from utils.ui.cursor import Cursor
from utils.ui.Dropdown import Dropdown
from utils.ui.Checkbox import Checkbox
import numpy as np

pygame.init()
Window = pygame.display.set_mode((500,500), pygame.SRCALPHA)
pygame.display.set_caption("Minecraft Texture Pack Maker")
clock = pygame.time.Clock()

Bruh = False

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