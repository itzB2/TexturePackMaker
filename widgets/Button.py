from utils.widgets import *
from utils.ImageMask import *
from utils.funcs import * 
import time

class Button(Widget):
	def __init__(self, pos, size, action, text):
		self.pos = pos
		self.size = size
		self.action = action
		self.state = "Not Clicked"
		self.text = text
		self.enabled = True
		self.objects = [Rect(100*size, 30*size, pos, Material((0,0,0), Image.open("./textures/widgets/Button.png"))),
						Text(self.text,'./textures/16x.ttf', self.size*8, [pos[0]+8, pos[1]+8])]
		self.coolDown = 0
		self.UpdatedDimensions = [100*size, 30*size]
		self.baseDimensions = [100, 30]
		self.Dimensions = [100*size, 30*size]
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
		self.visible = True

	def updateTextures(self, state):
		if state == "Clicked":
			self.objects[0] = Rect(100*self.size, 30*self.size, self.pos, Material((0,0,0), Image.open("./textures/widgets/ButtonClicked.png")))
		if state == "Not Clicked":
			self.objects[0] = Rect(100*self.size, 30*self.size, self.pos, Material((0,0,0), Image.open("./textures/widgets/Button.png")))
		if state == "Hovered":
			self.objects[0] = Rect(100*self.size, 30*self.size, self.pos, Material((0,0,0), Image.open("./textures/widgets/ButtonHovered.png")))

	def render(self, surface):
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

