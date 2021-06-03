import pygame
from utils.widgetUtils import *
from utils.funcs import *

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

class CustomView:
	def __init__(self):
		pass

class CustomViewLoader:
	def __init__(self, customView, data):
		pass

	def getItems(self):
		pass

class ListView:
	def __init__(self, customViewLoader, pos, action=defaultAction):
		self.v = customViewLoader.getItems()
		self.loader = customViewLoader
		self.pos = pos
		self.action = action