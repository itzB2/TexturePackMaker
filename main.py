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

def action(self):
	print(self.text)

cursor = Cursor(r"./textures/cursors/Normal.png", r"./textures/cursors/MouseClick/", Window)
	
editText = EditText((100, 100), 1, "Bruh")

pygame.key.set_repeat(1,100)

pygame.mouse.set_visible(False)
while not Bruh:
	clock.tick(60)
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			Bruh = True

	Window.fill((0,0,0))
	editText.update(events, Window)
	cursor.update(events)
	pygame.display.flip()