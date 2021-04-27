import pygame

pygame.init()
Window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Minecraft Texture Pack Maker")
clock = pygame.time.Clock()

Bruh = False

counter = 0

scaled = pygame.Surface((250, 250))
pygame.draw.rect(scaled, (255,255,255), pygame.Rect(0, 0, 100, 100))
# scaled = pygame.transform.scale(scaled, (200,200))

while not Bruh:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Bruh = True

	pygame.display.flip()
	# Window.blit(scaled, pygame.Rect(100, 100, 200,200))
	Window.blit(scaled, pygame.Rect(100, 100, 100,100))
	# counter += 1
	# if counter == 1:
	# 	Bruh = True