import pygame
from utils.widgetUtils import *
from utils.funcs import *

NotClickedSpriteShape = SpriteShapeAsset(
	"./textures/widgets/DropDown/Not Clicked/tL.png", 
	"./textures/widgets/DropDown/Not Clicked/t.png", 
	"./textures/widgets/DropDown/Not Clicked/tR.png", 
	"./textures/widgets/DropDown/Not Clicked/bL.png", 
	"./textures/widgets/DropDown/Not Clicked/b.png", 
	"./textures/widgets/DropDown/Not Clicked/bR.png", 
	"./textures/widgets/DropDown/Not Clicked/l.png", 
	"./textures/widgets/DropDown/Not Clicked/c.png", 
	"./textures/widgets/DropDown/Not Clicked/r.png",
	{"TL":(4,4),"T":(92,4),"TR":(4,4),
	 "BL":(4,4),"B":(92,4),"BR":(4,4),
	 "L":(4,22),"C":(92,22),"R":(4,22)
	})
HoveredSpriteShape = SpriteShapeAsset(
	"./textures/widgets/DropDown/Hovered/tL.png", 
	"./textures/widgets/DropDown/Hovered/t.png", 
	"./textures/widgets/DropDown/Hovered/tR.png", 
	"./textures/widgets/DropDown/Hovered/bL.png", 
	"./textures/widgets/DropDown/Hovered/b.png", 
	"./textures/widgets/DropDown/Hovered/bR.png", 
	"./textures/widgets/DropDown/Hovered/l.png", 
	"./textures/widgets/DropDown/Hovered/c.png", 
	"./textures/widgets/DropDown/Hovered/r.png",
	{"TL":(4,4),"T":(92,4),"TR":(4,4),
	 "BL":(4,4),"B":(92,4),"BR":(4,4),
	 "L":(4,22),"C":(92,22),"R":(4,22)
	})
NotClickedItemSpriteShape = SpriteShapeAsset(
	"./textures/widgets/DropDown/ListItems/Items/tL.png", 
	"./textures/widgets/DropDown/ListItems/Items/t.png", 
	"./textures/widgets/DropDown/ListItems/Items/tR.png", 
	"./textures/widgets/DropDown/ListItems/Items/bL.png", 
	"./textures/widgets/DropDown/ListItems/Items/b.png", 
	"./textures/widgets/DropDown/ListItems/Items/bR.png", 
	"./textures/widgets/DropDown/ListItems/Items/l.png", 
	"./textures/widgets/DropDown/ListItems/Items/c.png", 
	"./textures/widgets/DropDown/ListItems/Items/r.png",
	{"TL":(4,4),"T":(92,4),"TR":(4,4),
	 "BL":(4,4),"B":(92,4),"BR":(4,4),
	 "L":(4,22),"C":(92,22),"R":(4,22)
	})
HoveredItemSpriteShape = SpriteShapeAsset(
	"./textures/widgets/DropDown/ListItems/HoveredItems/tL.png", 
	"./textures/widgets/DropDown/ListItems/HoveredItems/t.png", 
	"./textures/widgets/DropDown/ListItems/HoveredItems/tR.png", 
	"./textures/widgets/DropDown/ListItems/HoveredItems/bL.png", 
	"./textures/widgets/DropDown/ListItems/HoveredItems/b.png", 
	"./textures/widgets/DropDown/ListItems/HoveredItems/bR.png", 
	"./textures/widgets/DropDown/ListItems/HoveredItems/l.png", 
	"./textures/widgets/DropDown/ListItems/HoveredItems/c.png", 
	"./textures/widgets/DropDown/ListItems/HoveredItems/r.png",
	{"TL":(4,4),"T":(92,4),"TR":(4,4),
	 "BL":(4,4),"B":(92,4),"BR":(4,4),
	 "L":(4,22),"C":(92,22),"R":(4,22)
	})

def defaultAction(self, val, ind):
	pass

class Option(Widget):
	def __init__(self, size, pos, text, asset, parent, ind):
		self.pos = pos
		self.size = size
		self.asset = asset
		self.p = parent
		self.text = text
		self.ind = ind
		self.objects = [
		SpriteShape(100, 30, self.asset, 30, self.p.UpdatedDimensions[0], (self.pos[0], self.pos[1])),
		Text(text,'./textures/16x.ttf', 8, [self.pos[0]+8, self.pos[1]+8])
		]
		self.rect = pygame.Rect(self.pos[0], self.pos[1], self.p.UpdatedDimensions[0], 30)

	def update(self):
		def checkCollision(mPos):
			return self.rect.collidepoint(mPos)

		mPos = pygame.mouse.get_pos()
		mClicked = pygame.mouse.get_pressed()
		if checkCollision(mPos):
			self.objects[0].Asset = HoveredItemSpriteShape
			if mClicked[0] == 1:
				self.p.selected(self.text, self.ind)

		else:
			self.objects[0].Asset = NotClickedItemSpriteShape
		self.objects[0].refresh()

	def render(self, surface):
		self.update()
		for OBJS in self.objects:
			OBJS.render(surface)

class DropdownOption():
	def __init__(self, options, parent, pos):
		self.option = options
		self.buffer = int(parent.UpdatedDimensions[0]/20)
		for text, textInd in zip(options, range(len(options)-1)):
			if len(text) > self.buffer:
				text = f"{text[:self.buffer]}."
			self.option[textInd] = text
		self.p = parent
		self.pos = pos
		self.objects = []
		self.refresh()

	def render(self, surface):
		for option in self.objects:
			option.render(surface)

	def refresh(self):
		for option, ind in zip(self.option, range(len(self.option))):
			self.objects.append(
				Option(
				(self.p.UpdatedDimensions[1], self.p.UpdatedDimensions[0]),
				self.pos,
				option,
				NotClickedItemSpriteShape,
				self.p,
				ind
				))
			self.pos[1] += 30

class Dropdown():
	def __init__(self, pos, size, values, default, action=defaultAction):
		self.pos = pos
		self.values = values
		self.default = default
		self.size = size
		self.state = "Not Clicked"
		self.surface = None
		self.action = action

		self.objects = [
		SpriteShape(100, 30, NotClickedSpriteShape, 30*size, 100*size,pos),
		Text(self.default,'./textures/16x.ttf', self.size*8, [pos[0]+8, pos[1]+8])
		]
		self.UpdatedDimensions = [100*size, 30*size]
		self.baseDimensions = [100, 30]
		self.Dimensions = [100*size, 30*size]
		ratio = Ratio(3, 10)
		for obj in self.objects:
			if obj.type=="Text":				
				height = int(str(obj.textRect).replace(" ", "").split(",")[2])
				length = int(ratio.getRatioFromB(height))		
				self.UpdatedDimensions[1] = self.UpdatedDimensions[1] + length
				self.UpdatedDimensions[0] = self.UpdatedDimensions[0] + height
				obj.refresh()
		self.visible = True
		self.enabled = True
		self.dropdownOption = DropdownOption(self.values, self, [pos[0], pos[1]+30])

	def selected(self, selectedVal, selectedInd):
		self.default = selectedVal
		self.action(self, selectedVal, selectedInd)

	def updateTextures(self, state):
		size = self.size
		pos = self.pos
		self.state = state
		if state == "Not Clicked" or state == "Clicked":
			self.objects[0].Asset = NotClickedSpriteShape
			self.objects[0].refresh()
		if state == "Hovered":
			self.objects[0].Asset = HoveredSpriteShape
			self.objects[0].refresh()

	def render(self, surface):
		if self.state == "Not Clicked" or self.state == "Hovered":
			bg, text = self.objects

			bg.objLength = self.UpdatedDimensions[0]
			bg.objheight = self.Dimensions[1]
			bg.refresh()

			bg.render(surface)

			self.objects = [bg, text]
			text.render(surface)

		elif self.state == "Clicked":
			bg, text, options = self.objects

			options.render(surface)

			bg.objLength = self.UpdatedDimensions[0]
			bg.objheight = self.Dimensions[1]
			bg.refresh()

			bg.render(surface)
			self.objects = [bg, text, options]
			text.render(surface)

	def update(self, events, surface):
		self.objects[1].text = self.default
		self.objects[1].refresh()
		def checkCollision():
			return mPos[0] > self.pos[0] and mPos[0] < self.pos[0]+self.UpdatedDimensions[0] and mPos[1] > self.pos[1] and mPos[1] < self.pos[1]+self.UpdatedDimensions[1]

		if self.visible:
			self.render(surface)

		if self.enabled:
			mPos = pygame.mouse.get_pos()
			mClicked = pygame.mouse.get_pressed()
			if checkCollision():
				if self.state != "Clicked" and self.state == "Not Clicked":
					self.updateTextures("Hovered")
				if mClicked[0] == 1:
					self.updateTextures("Clicked")
			elif mClicked[0] == 1 and self.state == "Clicked" or self.state == "Hovered":
				self.updateTextures("Not Clicked")
				try:
					self.objects.pop(2)
				except:
					pass
			# else:
			# 	self.updateTextures("Not Clicked")
		if self.state == "Clicked":
			if len(self.objects) == 2:
				self.objects.append(self.dropdownOption)
		self.render(surface)
		if self.state == "Not Clicked":
			try:
				self.objects.pop(2)
			except:
				pass
		self.surface = surface

