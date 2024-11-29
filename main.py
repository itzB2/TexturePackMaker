import pygame
import numpy as np

from utils.ui.cursor import Cursor
from utils.ui.Button import Button
from utils.ui.Checkbox import Checkbox
from utils.ui.EditText import EditText
from utils.ui.Listview import ListView #Forgot about the project before this was completed

pygame.init()
# Window = pygame.display.set_mode((1520,768), pygame.SRCALPHA)
Window = pygame.display.set_mode((600,600), pygame.SRCALPHA)
pygame.display.set_caption("Minecraft Texture Pack Maker")
clock = pygame.time.Clock()

Bruh = False
cursor = Cursor(r"./textures/cursors/Normal.png", r"./textures/cursors/MouseClick/", Window)
pygame.key.set_repeat(1,100)
pygame.mouse.set_visible(False)

def reactionBtn(btn):
	print(btn.text)

btn = Button((100,100),2,"Yo", reactionBtn)
box = Checkbox((300,100),"You Sure?")
editText = EditText((100,200), 1, "") #Really buggy 

@box.onChanged
def checkboxReaction(chckBox, state):
	print(state)

@editText.onChanged
def textEdited(editTextObject):
	print(editTextObject.text)

while not Bruh:
	clock.tick(60)
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			Bruh = True

	Window.fill((0,0,0,255))

	btn.update(events,Window)
	box.update(Window)
	editText.update(events,Window)

	cursor.update(events)
	pygame.display.flip()