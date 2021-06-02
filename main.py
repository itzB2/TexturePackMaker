import pygame
from utils.ui.cursor import Cursor
from utils.ui.Dropdown import Dropdown
import numpy as np

pygame.init()
Window = pygame.display.set_mode((500,500), pygame.SRCALPHA)
pygame.display.set_caption("Minecraft Texture Pack Maker")
clock = pygame.time.Clock()

Bruh = False

def action(self, val, ind):
	print(self.default, val, ind)
def actionB(self):
	print(self.text)

cursor = Cursor(r"./textures/cursors/Normal.png", r"./textures/cursors/MouseClick/", Window)
dropdown = Dropdown((100,100), 1, ["A","B"], "A")

pygame.key.set_repeat(1,100)

pygame.mouse.set_visible(False)
while not Bruh:
	clock.tick(60)
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			Bruh = True

	Window.fill((0,0,0,255))
	dropdown.update(events, Window)
	cursor.update(events)
	pygame.display.flip()