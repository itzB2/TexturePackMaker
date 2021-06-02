from utils.widgetUtils import *
from utils.Mask import *
from utils.funcs import * 
import time
ClickedSpriteShape = SpriteShapeAsset(
	"./textures/widgets/Button/Clicked/tL.png", 
	"./textures/widgets/Button/Clicked/t.png", 
	"./textures/widgets/Button/Clicked/tR.png", 
	"./textures/widgets/Button/Clicked/bL.png", 
	"./textures/widgets/Button/Clicked/b.png", 
	"./textures/widgets/Button/Clicked/bR.png", 
	"./textures/widgets/Button/Clicked/l.png", 
	"./textures/widgets/Button/Clicked/c.png", 
	"./textures/widgets/Button/Clicked/r.png",
	{"TL":(4,4),"T":(92,4),"TR":(4,4),
	 "BL":(4,4),"B":(92,4),"BR":(4,4),
	 "L":(4,22),"C":(92,22),"R":(4,22)
	})
NotClickedSpriteShape = SpriteShapeAsset(
	"./textures/widgets/Button/Not Clicked/tL.png", 
	"./textures/widgets/Button/Not Clicked/t.png", 
	"./textures/widgets/Button/Not Clicked/tR.png", 
	"./textures/widgets/Button/Not Clicked/bL.png", 
	"./textures/widgets/Button/Not Clicked/b.png", 
	"./textures/widgets/Button/Not Clicked/bR.png", 
	"./textures/widgets/Button/Not Clicked/l.png", 
	"./textures/widgets/Button/Not Clicked/c.png", 
	"./textures/widgets/Button/Not Clicked/r.png",
	{"TL":(4,4),"T":(92,4),"TR":(4,4),
	 "BL":(4,4),"B":(92,4),"BR":(4,4),
	 "L":(4,22),"C":(92,22),"R":(4,22)
	})

HoveredSpriteShape = SpriteShapeAsset(
	"./textures/widgets/Button/Hovered/tL.png", 
	"./textures/widgets/Button/Hovered/t.png", 
	"./textures/widgets/Button/Hovered/tR.png", 
	"./textures/widgets/Button/Hovered/bL.png", 
	"./textures/widgets/Button/Hovered/b.png", 
	"./textures/widgets/Button/Hovered/bR.png", 
	"./textures/widgets/Button/Hovered/l.png", 
	"./textures/widgets/Button/Hovered/c.png", 
	"./textures/widgets/Button/Hovered/r.png",
	{"TL":(4,4),"T":(92,4),"TR":(4,4),
	 "BL":(4,4),"B":(92,4),"BR":(4,4),
	 "L":(4,22),"C":(92,22),"R":(4,22)
	})

class Button(Widget):
	def __init__(self, pos, size, action, text):
		self.pos = pos
		self.size = size
		self.action = action
		self.state = "Not Clicked"
		self.text = text
		self.enabled = True
		self.objects = [SpriteShape(100, 30, NotClickedSpriteShape, 100*size, 30*size,pos),
						Text(self.text,'./textures/16x.ttf', self.size*8, [pos[0]+8, pos[1]+8])]
		self.coolDown = 0
		self.UpdatedDimensions = [100*size, 30*size]
		self.baseDimensions = [100, 30]
		self.Dimensions = [100*size, 30*size]
		ratio = Ratio(3, 10)
		for obj in self.objects:
			if obj.type=="Text":				
				height = obj.textRect.height
				length = int(ratio.getRatioFromB(height))			
				self.UpdatedDimensions[1] = self.UpdatedDimensions[1] + length
				self.UpdatedDimensions[0] = self.UpdatedDimensions[0] + height
				obj.refresh()
		self.visible = True

	def updateTextures(self, state):
		size = self.size
		pos = self.pos
		if state == "Clicked":
			self.objects[0] = SpriteShape(100, 30, ClickedSpriteShape, 100*size, 30*size,pos)
		if state == "Not Clicked":
			self.objects[0] = SpriteShape(100, 30, NotClickedSpriteShape, 100*size, 30*size,pos)
		if state == "Hovered":
			self.objects[0] = SpriteShape(100, 30, HoveredSpriteShape, 100*size, 30*size,pos)

	def render(self, surface):
		bg, text = self.objects

		bg.objLength = self.UpdatedDimensions[0]
		bg.objheight = self.Dimensions[1]
		bg.refresh()

		bg.render(surface)

		self.objects = [bg, text]
		text.render(surface)

	def update(self, events, surface):
		def checkCollision():

			return mPos[0] > self.pos[0] and mPos[0] < self.pos[0]+self.UpdatedDimensions[0] and mPos[1] > self.pos[1] and mPos[1] < self.pos[1]+self.UpdatedDimensions[1]

		if self.visible:
			self.render(surface)

		if self.enabled:
			mPos = pygame.mouse.get_pos()
			mClicked = pygame.mouse.get_pressed()
			if checkCollision():
				self.updateTextures("Hovered")
				if mClicked[0] == 1:
					self.updateTextures("Clicked")
					if self.coolDown == 0:
						self.action(self)
						self.coolDown = 60
					else:
						self.coolDown -= 1
				else:
					if self.coolDown != 0:
						self.coolDown -= 1
			elif self.coolDown != 0:
				self.coolDown -= 1
				self.updateTextures("Not Clicked")
			else:
				self.updateTextures("Not Clicked")

