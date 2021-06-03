import pygame
from utils.widgetUtils import *
from utils.funcs import *

class Checkbox:
	def __init__(self, pos, text):
		self.p = pos
		self.t = text
		self.s = (30,30)

		self.text = Text(text,'./textures/16x.ttf', 8, [pos[0]+38, pos[1]+8])

		self.rect = pygame.Rect(self.p, self.s)

		self.eventFuncs = []

		self.red = pygame.image.load(r"./textures/widgets/Checkbox/RedAnimation/RedBG6.png")
		self.green = pygame.image.load(r"./textures/widgets/Checkbox/GreenAnimation/Green6.png")

		self.n = self.red

		self.GreenClickAnim = []
		self.RedClickAnim = []

		RedAnimation = os.listdir(r"./textures/widgets/Checkbox/RedAnimation/")
		GreenAnimation = os.listdir(r"./textures/widgets/Checkbox/GreenAnimation/")

		for imageDir in GreenAnimation:
			self.GreenClickAnim.append(pygame.image.load(os.path.join(r"./textures/widgets/Checkbox/GreenAnimation/", imageDir)))

		for imageDir in RedAnimation:
			self.RedClickAnim.append(pygame.image.load(os.path.join(r"./textures/widgets/Checkbox/RedAnimation/", imageDir)))

		self.cImage = self.n

		self.coolDown = 0
		self.AnimIndex = 0
		self.startAnim = False

		self.state = False

	def onChanged(self, func):

		self.eventFuncs.append(func)

	def changeState(self):
		self.coolDown = 0
		self.startAnim = True

	def render(self, surface):
		rect = self.cImage.get_rect()
		rect.x = self.p[0]
		rect.y = self.p[1]
		surface.blit(self.cImage, rect)
		self.text.render(surface)

	def update(self, surface):

		mPos = pygame.mouse.get_pos()
		mClicked = pygame.mouse.get_pressed()

		if mClicked[0] == 1:
			if self.rect.collidepoint(mPos) and self.coolDown == 0:
				self.changeState()
				self.state = not self.state
				for func in self.eventFuncs:
					func(self, self.state)
		self.render(surface)

		self.n = self.red if not self.state else self.green

		if self.startAnim:
			self.coolDown += 1
			self.AnimIndex = clamp(round(self.coolDown/8), 0, 5)
			self.cImage = self.GreenClickAnim[self.AnimIndex] if self.state else self.RedClickAnim[self.AnimIndex]
			if self.coolDown == 48:
				self.cImage = self.green if self.state else self.red
				self.coolDown = 0
				self.startAnim = False

