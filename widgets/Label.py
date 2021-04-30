from utils.ImageMask import *
from utils.widgets import *
from utils.funcs import *

class Label(Widget):
	def __init__(self, pos, size, text):
		self.pos = pos
		self.size = size
		self.text = text
		self.visible = True
		self.objects = [
		Rect(100*size, 30*size, pos, Material((0,0,0), Image.open("./textures/widgets/LabelBG.png"))),
		Text(self.text,'./textures/16x.ttf', self.size*8, [pos[0]+8, pos[1]+8])
		]
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

	def update(self, surface):
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
