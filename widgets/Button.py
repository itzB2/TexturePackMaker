from utils.widgets import *
from utils.ImageMask import *
import time

class Button(Widget):
	def __init__(self, pos, size, action, text):
		self.pos = pos
		self.size = size
		self.action = action
		self.state = "Not Clicked"
		self.text = text
		self.enabled = True
		self.objects = [Rect(30*size, 100*size, pos, Material((0,0,0), Image.open("./textures/widgets/Button.png"))),
						Text(self.text,'./textures/16x.ttf', self.size*8, (pos[0]+8, pos[1]+6))]
		super().__init__()
		self.coolDown = 0
		self.UpdatedDimensions = [30*size, 100*size]
		self.baseDimensions = [30, 100]
		self.Dimensions = [30*size, 100*size]
		for obj in self.objects:
			if obj.type=="Text":
				length = obj.textRect.width+10
				height = obj.textRect.height+5
				self.UpdatedDimensions[1] = self.UpdatedDimensions[1] + length
				self.UpdatedDimensions[0] = self.UpdatedDimensions[0] + height

	def updateTextures(self, state):
		if state == "Clicked":
			self.objects[0] = Rect(30*self.size, 100*self.size, self.pos, Material((0,0,0), Image.open("./textures/widgets/ButtonClicked.png")))
		if state == "Not Clicked":
			self.objects[0] = Rect(30*self.size, 100*self.size, self.pos, Material((0,0,0), Image.open("./textures/widgets/Button.png")))
		if state == "Hovered":
			self.objects[0] = Rect(30*self.size, 100*self.size, self.pos, Material((0,0,0), Image.open("./textures/widgets/ButtonHovered.png")))

	def render(self, surface):
		bg, text = self.objects

		bg.p = (0,0)
		bg.a = self.UpdatedDimensions[0]
		bg.b = self.UpdatedDimensions[1]

		dest = Surface(self.baseDimensions)
		bg.render(dest)

		scaledSurface = pygame.transform.scale(dest, self.UpdatedDimensions)
		scaledRect = pygame.Rect(self.pos, (scaledSurface.get_rect().width, scaledSurface.get_rect().height))

		surface.blit(scaledSurface, scaledRect)

		self.objects = [bg, text]

	def update(self, events, surface):
		mPos = pygame.mouse.get_pos()
		mClicked = pygame.mouse.get_pressed()

		def checkCollision():

			return mPos[0] > self.pos[0] and mPos[0] < self.pos[0]+self.UpdatedDimensions[1] and mPos[1] > self.pos[1] and mPos[1] < self.pos[1]+self.UpdatedDimensions[0]

		self.render(surface)
		if checkCollision() and self.enabled == True:
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

