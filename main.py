import pygame
from widgets.Button import Button

pygame.init()
Window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Minecraft Texture Pack Maker")
clock = pygame.time.Clock()

Bruh = False

def action(self):
	print(self.text)

Button = Button((100,100), 1, action, "")

counter = 0

while not Bruh:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Bruh = True

	Button.update(pygame.event.get(), Window)
	pygame.display.flip()
	# counter += 1
	# if counter == 1:
	# 	Bruh = True