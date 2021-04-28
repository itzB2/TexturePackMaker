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
		for obj in self.objects:
			if obj.type=="Text":				
				height = obj.textRect.height-74
				length = int(ratio.getRatioFromB(height))			
				self.UpdatedDimensions[1] = self.UpdatedDimensions[1] + length
				self.UpdatedDimensions[0] = self.UpdatedDimensions[0] + height
				obj.pos[0] = self.pos[0]+int(height/2)+(10*self.size)
				obj.pos[1] = self.pos[1]+int(length/2)+5
				obj.refresh()
				self.pointerPos = [obj.textRect.right+((2*self.size)+(10*self.size)), obj.pos[1]]
		# print(pointerPos)
		self.textPointer = Rect(10, 30, self.pointerPos, Material((0,0,0), r"./textures/cursors/TextPointer.png", True))

	def updateTextures(self, state):
		self.state = state
		if state == "Clicked":
			self.objects[0] = Rect(100*self.size, 30*self.size, self.pos, Material((0,0,0), Image.open("./textures/widgets/TextEditClicked.png")))
		if state == "Not Clicked":
			self.objects[0] = Rect(100*self.size, 30*self.size, self.pos, Material((0,0,0), Image.open("./textures/widgets/LabelBG.png")))

	def render(self, surface):
		if self.state == "Clicked":
			bg, text, textPointer = self.objects
			bg.p = (0,0)
			bg.a = self.UpdatedDimensions[0]
			bg.b = self.UpdatedDimensions[1]
			bg.refresh()

			textPointer.p = ((self.pointerPos[0])+(2*text.textRect.width)+5, self.pointerPos[1])
			textPointer.scaleTranspTexture((10*self.size, 30*self.size))
			textPointer.refresh()

			# bg.debug = True

			dest = Surface(self.baseDimensions)
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

	def update(self, surface):
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
