import pygame
import os
from PIL import Image
from utils.Mask import *
from utils.funcs import *

class Cursor:
	def __init__(self, normal, clickAnim, surface):
		self.n = pygame.image.load(normal)
		self.clickAnim = []
		clickAnimation = os.listdir(clickAnim)
		for imageDir in clickAnimation:
			self.clickAnim.append(pygame.image.load(os.path.join(clickAnim, imageDir)))
		self.s = surface
		self.cImage = self.n
		self.coolDown = 0
		self.AnimIndex = 0
		self.startAnim = False
		self.state = ""

	def click(self):
		self.coolDown = 0
		self.startAnim = True

	def SetState(self, state):
		self.state = state

	def update(self, events):
		mPos = pygame.mouse.get_pos()
		mClicked = pygame.mouse.get_pressed()
		if mClicked[0] == 1:
			self.click()
		self.cImageRect = self.cImage.get_rect()
		self.cImageRect.center = mPos
		self.s.blit(self.cImage, self.cImageRect)
		if self.startAnim:
			self.coolDown += 1
			self.AnimIndex = clamp(round(self.coolDown/2), 0, 6)
			self.cImage = self.clickAnim[self.AnimIndex]
			if self.coolDown == 14:
				self.cImage = self.n
				self.coolDown = 0
				self.startAnim = False

