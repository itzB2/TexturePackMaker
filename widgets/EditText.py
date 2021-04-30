from utils.ImageMask import *
from utils.widgets import *
from utils.funcs import *

class EditText(Widget):
	def __init__(self, pos, size, text):
		self.pos = pos
		self.size = size
		self.text = text
		self.enabled = True
		self.visible = True
		self.state = "Not Clicked"		
		self.objects = [
		Rect(100*size, 30*size, pos, Material((0,0,0), Image.open("./textures/widgets/LabelBG.png"))),
		Text(self.text,'./textures/16x.ttf', self.size*8, [pos[0]+8, pos[1]+8]),
		]
		self.UpdatedDimensions = [100*size, 30*size]
		self.baseDimensions = [100, 30]
		self.Dimensions = [100*size, 30*size]
		pointerPos = []
		ratio = Ratio(3, 10)
		self.tPRatio = Ratio(10, 30)
		for obj in self.objects:
			if obj.type=="Text":				
				length = obj.textRect.height
				height = int(ratio.getRatioFromB(length))			
				self.UpdatedDimensions[1] = self.UpdatedDimensions[1] + height
				self.UpdatedDimensions[0] = self.UpdatedDimensions[0] + length
				obj.refresh()
				self.pointerPos = [obj.textRect.right, obj.pos[1]]
		# print(pointerPos)
		self.textPointer = Rect(10, 20, self.pointerPos, Material((0,0,0), r"./textures/cursors/TextPointer.png", True))

	def updateTextures(self, state):
		self.state = state
		if state == "Clicked":
			self.objects[0] = Rect(100*self.size, 30*self.size, self.pos, Material((0,0,0), Image.open("./textures/widgets/TextEditClicked.png")))
		if state == "Not Clicked":
			self.objects[0] = Rect(100*self.size, 30*self.size, self.pos, Material((0,0,0), Image.open("./textures/widgets/LabelBG.png")))

	def refreshBG(self, factor):
		text = self.objects[1]
		length = text.textRect.height*factor
		height = int(self.tPRatio.getRatioFromB(length))			
		self.UpdatedDimensions[1] += height
		self.UpdatedDimensions[0] += length

	def render(self, surface):
		if self.state == "Clicked":
			bg, text, textPointer = self.objects

			bg.p = (0,0)
			bg.a = self.UpdatedDimensions[0]
			bg.b = self.UpdatedDimensions[1]
			bg.refresh()

			self.pointerPos = [text.textRect.right, text.pos[1]]

			textPointer.a = int(self.tPRatio.getRatioFromB(20*self.size))
			textPointer.b = int(20*self.size)
			textPointer.p = (self.pointerPos[0], self.pointerPos[1])
			textPointer.scaleTranspTexture((textPointer.a, textPointer.b))

			# bg.debug = True

			dest = Surface(self.baseDimensions)
			surRect = surface.get_rect()
			bg.render(dest)

			scaledSurface = pygame.transform.scale(dest, self.UpdatedDimensions)
			scaledRect = pygame.Rect(self.pos, self.UpdatedDimensions)

			surface.blit(scaledSurface, scaledRect)
			self.objects = [bg, text, textPointer]
			text.render(surface)
			textPointer.render(surface)

		else:
			bg, text = self.objects
			bg.p = (0,0)
			bg.a = self.UpdatedDimensions[0]
			bg.b = self.UpdatedDimensions[1]
			bg.refresh()
			# bg.debug = True

			dest = Surface(self.baseDimensions)
			bg.render(dest)

			scaledSurface = pygame.transform.scale(dest, self.UpdatedDimensions)
			scaledRect = pygame.Rect(self.pos, self.UpdatedDimensions)

			surface.blit(scaledSurface, scaledRect)			
			self.objects = [bg, text]
			
			text.render(surface)

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
							if len(textObj.text) > 4:
								self.refreshBG(-1)
							if self.visible:
								self.render(surface)
					else:
						textObj.text += events.unicode
						textObj.refresh()
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
