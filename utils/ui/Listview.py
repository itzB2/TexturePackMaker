import pygame
from utils.widgetUtils import *
from utils.funcs import *

NotClickedItemSpriteShape = SpriteShapeAsset(
	"./textures/widgets/ListView/Items/tL.png", 
	"./textures/widgets/ListView/Items/t.png", 
	"./textures/widgets/ListView/Items/tR.png", 
	"./textures/widgets/ListView/Items/bL.png", 
	"./textures/widgets/ListView/Items/b.png", 
	"./textures/widgets/ListView/Items/bR.png", 
	"./textures/widgets/ListView/Items/l.png", 
	"./textures/widgets/ListView/Items/c.png", 
	"./textures/widgets/ListView/Items/r.png",
	{"TL":(4,4),"T":(92,4),"TR":(4,4),
	 "BL":(4,4),"B":(92,4),"BR":(4,4),
	 "L":(4,22),"C":(92,22),"R":(4,22)
	})
HoveredItemSpriteShape = SpriteShapeAsset(
	"./textures/widgets/ListView/HoveredItems/tL.png", 
	"./textures/widgets/ListView/HoveredItems/t.png", 
	"./textures/widgets/ListView/HoveredItems/tR.png", 
	"./textures/widgets/ListView/HoveredItems/bL.png", 
	"./textures/widgets/ListView/HoveredItems/b.png", 
	"./textures/widgets/ListView/HoveredItems/bR.png", 
	"./textures/widgets/ListView/HoveredItems/l.png", 
	"./textures/widgets/ListView/HoveredItems/c.png", 
	"./textures/widgets/ListView/HoveredItems/r.png",
	{"TL":(4,4),"T":(92,4),"TR":(4,4),
	 "BL":(4,4),"B":(92,4),"BR":(4,4),
	 "L":(4,22),"C":(92,22),"R":(4,22)
	})

def defaultAction(self, val, ind):
	pass

class Option(Widget):
	def __init__(self, size, pos, text, asset, parent, ind, fO):
		self.pos = pos
		self.size = size
		self.asset = asset
		self.p = parent
		self.text = text
		self.ind = ind
		self.aT = fO
		self.objects = [
		SpriteShape(100, 30, self.asset, 30, self.size[1], (self.pos[0], self.pos[1])),
		Text(text,'./textures/16x.ttf', 8, [self.pos[0]+8, self.pos[1]+8])
		]
		self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[1], 30)

	def update(self):
		def checkCollision(mPos):
			return self.rect.collidepoint(mPos)

		mPos = pygame.mouse.get_pos()
		mClicked = pygame.mouse.get_pressed()
		if checkCollision(mPos):
			self.objects[0].Asset = HoveredItemSpriteShape
			if mClicked[0] == 1:
				self.p.selected(self.aT, self.ind)

		else:
			self.objects[0].Asset = NotClickedItemSpriteShape
		self.objects[0].refresh()

	def render(self, surface):
		self.update()
		for OBJS in self.objects:
			OBJS.render(surface)

class DropdownOption():
	def __init__(self, options, parent, pos, bufferS, rO):
		self.options = options
		self.option = []
		self.buffer = int(bufferS/8)
		self.bs = bufferS
		self.ro = rO
		for text, textInd in zip(self.options, range(len(self.options))):
			if len(text) > self.buffer:
				text = f"{text[:self.buffer]}."
				# text = text
			self.option.append(text)
		self.p = parent
		self.pos = pos
		self.startPos = [0,0]
		self.objects = list(range(0, self.ro[1]))
		self.refresh()

	def render(self, surface):
		for option in self.objects:
			option.render(surface)

	def refresh(self):
		self.pos = [0,0]
		for ind, val in zip(range(self.ro[0], self.ro[1]), range(0, len(self.options)-1)):
			option = self.option[ind]
			fO = self.options[ind]
			self.objects[val] = Option((self.p.UpdatedDimensions[1], self.bs),self.pos,
				option,
				NotClickedItemSpriteShape,
				self.p,
				ind,
				fO)
			self.pos[1] += 30

class ListView():
	def __init__(self, pos, maxSize, size, values, action=defaultAction):
		self.pos = pos
		self.values = values
		self.size = size
		self.mS = maxSize
		self.state = "Not Clicked"
		self.surface = None
		self.action = action
		self.UpdatedDimensions = [100*size, 30*size]
		self.renderObjects = [0, clamp(int(self.mS[1]/30), 0, len(values))]
		self.maxInOneView = clamp(int(self.mS[1]/30), 0, len(values))
		self.maxScrollDistance = min(maxSize[1], len(values)*30)
		self.objects = [
		DropdownOption(values, self, [pos[0], pos[1]], maxSize[0], self.renderObjects)
		]
		self.baseDimensions = [100, 30]
		self.Dimensions = [100*size, 30*size]
		self.collisionDimensions = maxSize
		ratio = Ratio(3, 10)
		self.visible = True
		self.enabled = True
		self.selectedTimer = 0
		self.dropdownOption = DropdownOption(values, self, [pos[0], pos[1]+30], maxSize[0], self.renderObjects)
		self.mask = pygame.Surface((maxSize[0], maxSize[1]))
		self.posInMask = [0,0]
		self.scrollVal = 0

	def selected(self, selectedVal, selectedInd):
		if self.selectedTimer == 0:
			self.action(self, selectedVal, selectedInd)
			self.selectedTimer = 60

	def updateTextures(self, state):
		self.state = state

	def render(self, surface):
		options = self.objects[0]
		options.render(self.mask)
		surface.blit(self.mask, self.pos)
		self.objects = [options]

	def update(self, events, surface):
		if self.selectedTimer != 0:
			self.selectedTimer -= 1
		def checkCollision():
			return mPos[0] > self.pos[0] and mPos[0] < self.pos[0]+self.collisionDimensions[1] and mPos[1] > self.pos[1] and mPos[1] < self.pos[1]+self.collisionDimensions[0]

		for event in events:
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 4:
					self.renderObjects = [
											clamp(self.renderObjects[1]-(1+self.maxInOneView), 0, len(self.values)),
											clamp(self.renderObjects[1]-1, self.maxInOneView, len(self.values))
										 ]
					self.objects[0].ro = self.renderObjects
					self.objects[0].refresh()
				elif event.button == 5:
					self.renderObjects = [
											clamp(self.renderObjects[1]+1, 0, len(self.values))-self.maxInOneView,
											clamp(self.renderObjects[1]+1, 0, len(self.values))
										 ]
					self.objects[0].ro = self.renderObjects
					self.objects[0].refresh()

		if self.visible:
			self.render(surface)

		self.surface = surface