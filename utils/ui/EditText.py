from utils.Mask import *
from utils.widgetUtils import *
from utils.funcs import *

ClickedSpriteShape = SpriteShapeAsset(
	"./textures/widgets/Edit Text/Clicked/tL.png", 
	"./textures/widgets/Edit Text/Clicked/t.png", 
	"./textures/widgets/Edit Text/Clicked/tR.png", 
	"./textures/widgets/Edit Text/Clicked/bL.png", 
	"./textures/widgets/Edit Text/Clicked/b.png", 
	"./textures/widgets/Edit Text/Clicked/bR.png", 
	"./textures/widgets/Edit Text/Clicked/l.png", 
	"./textures/widgets/Edit Text/Clicked/c.png", 
	"./textures/widgets/Edit Text/Clicked/r.png",
	{"TL":(4,4),"T":(92,4),"TR":(4,4),
	 "BL":(4,4),"B":(92,4),"BR":(4,4),
	 "L":(4,22),"C":(92,22),"R":(4,22)
	})
NotClickedSpriteShape = SpriteShapeAsset(
	"./textures/widgets/Edit Text/Not Clicked/tL.png", 
	"./textures/widgets/Edit Text/Not Clicked/t.png", 
	"./textures/widgets/Edit Text/Not Clicked/tR.png", 
	"./textures/widgets/Edit Text/Not Clicked/bL.png", 
	"./textures/widgets/Edit Text/Not Clicked/b.png", 
	"./textures/widgets/Edit Text/Not Clicked/bR.png", 
	"./textures/widgets/Edit Text/Not Clicked/l.png", 
	"./textures/widgets/Edit Text/Not Clicked/c.png", 
	"./textures/widgets/Edit Text/Not Clicked/r.png",
	{"TL":(4,4),"T":(92,4),"TR":(4,4),
	 "BL":(4,4),"B":(92,4),"BR":(4,4),
	 "L":(4,22),"C":(92,22),"R":(4,22)
	})

class EditText(Widget):
	def __init__(self, pos, size, text):
		self.pos = pos
		self.size = size
		self.text = text
		self.enabled = True
		self.visible = True
		self.state = "Not Clicked"	
		self.eventFuncs = []
		self.objects = [
		SpriteShape(100, 30, NotClickedSpriteShape, 100*size, 30*size,pos),
		Text(self.text,'./textures/16x.ttf', self.size*8, [pos[0]+8, pos[1]+8]),
		]
		self.UpdatedDimensions = [100*size, 30*size]
		self.baseDimensions = [100, 30]
		self.Dimensions = [100*size, 30*size]
		# self.buffer = int(20/size)
		pointerPos = []
		ratio = Ratio(3, 10)
		self.tPRatio = Ratio(10, 30)
		for obj in self.objects:
			if obj.type=="Text":				
				length = obj.textRect.height+int(20/obj.textRect.height)
				# height = int(ratio.getRatioFromB(length))
				# self.UpdatedDimensions[1] = self.UpdatedDimensions[1] + height
				self.UpdatedDimensions[0] = self.UpdatedDimensions[0] + length
				obj.refresh()
				self.pointerPos = [obj.textRect.right, obj.pos[1]]
		# print(pointerPos)
		self.textPointer = Rect(10, 20, self.pointerPos, Material((0,0,0), r"./textures/cursors/TextPointer.png", True))

	def updateTextures(self, state):
		self.state = state
		size = self.size
		pos = self.pos
		if state == "Clicked":
			self.objects[0] = SpriteShape(100, 30, NotClickedSpriteShape, 100*size, 30*size,pos)
		if state == "Not Clicked":
			self.objects[0] = SpriteShape(100, 30, NotClickedSpriteShape, 100*size, 30*size,pos)

	def refreshBG(self, factor):
		text = self.objects[1]
		length = text.textRect.height*factor
		# height = int(self.tPRatio.getRatioFromB(length))	
		self.UpdatedDimensions[1] = self.Dimensions[1]
		self.UpdatedDimensions[0] += length

	def render(self, surface):
		if self.state == "Clicked":
			bg, text, textPointer = self.objects

			bg.objLength = self.UpdatedDimensions[0]+40
			bg.objheight = self.Dimensions[1]
			# bg.DEBUG = True
			bg.refresh()

			self.pointerPos = [text.textRect.right, text.pos[1]]

			textPointer.a = int(self.tPRatio.getRatioFromB(20*self.size))
			textPointer.b = int(20*self.size)
			textPointer.p = (self.pointerPos[0], self.pointerPos[1])
			textPointer.scaleTranspTexture((textPointer.a, textPointer.b))

			bg.render(surface)

			self.objects = [bg, text, textPointer]
			text.render(surface)
			textPointer.render(surface)

		else:
			bg, text = self.objects

			try:
				bg.objLength = self.UpdatedDimensions[0]
				bg.objheight = self.Dimensions[1]
				# bg.DEBUG = True
				bg.refresh()

				bg.render(surface)
			except:
				bg = bg[0]
				bg.objLength = self.UpdatedDimensions[0]
				bg.objheight = self.Dimensions[1]
				# bg.DEBUG = True
				bg.refresh()

				bg.render(surface)				

			self.objects = [bg, text]
			
			text.render(surface)

	def onChanged(self, func):
		self.eventFuncs.append(func)

	def update(self, evetns, surface):
		if self.state == "Clicked":
			textObj = self.objects[1]
			self.text = textObj.text
			for events in evetns:
				if events.type == pygame.KEYDOWN:
					if events.key == pygame.K_BACKSPACE:
						if len(textObj.text) > 0:
							textObj.text = textObj.text[:-1]
							textObj.refresh()
							for f in self.eventFuncs:
								f(self)
							if len(textObj.text) > 4:
								self.refreshBG(-1)
							if self.visible:
								self.render(surface)
						elif len(textObj.text) == 0:
							self.UpdatedDimensions[0] = 100*self.size
					else:
						textObj.text += events.unicode
						textObj.refresh()
						for f in self.eventFuncs:
							f(self)
						if len(textObj.text) > 4:
							self.refreshBG(1)
						if self.visible:
							self.render(surface)						

		def checkCollision():
			return mPos[0] > self.pos[0] and mPos[0] < self.pos[0]+self.UpdatedDimensions[0] and mPos[1] > self.pos[1] and mPos[1] < self.pos[1]+self.UpdatedDimensions[1]

		if self.visible:
			self.render(surface)

		if self.enabled:
			mPos = pygame.mouse.get_pos()
			mClicked = pygame.mouse.get_pressed()
			if checkCollision():
				if mClicked[0] == 1:
					self.objects = [self.objects[0], self.objects[1], self.textPointer]
					self.updateTextures("Clicked")
			elif mClicked[0] == 1 and self.state == "Clicked":
				self.updateTextures("Not Clicked")
				try:
					self.objects.pop(2)
				except:
					pass
