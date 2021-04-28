import pygame
from widgets.Button import Button
from widgets.Label import Label
from widgets.EditText import EditText
from cursor import Cursor

pygame.init()
Window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Minecraft Texture Pack Maker")
clock = pygame.time.Clock()

Bruh = False

cursor = Cursor(r"./textures/cursors/Normal.png", r"./textures/cursors/MouseClick/", Window)

editText = EditText((100, 100), 2, "Bruh")

pygame.mouse.set_visible(False)
while not Bruh:
	clock.tick(60)
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			Bruh = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				print(pygame.mouse.get_pos())

	Window.fill((0,0,0))
	editText.update(Window)
	cursor.update(events)
	pygame.display.flip()