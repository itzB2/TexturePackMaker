import pygame
from utils.widgetUtils import *

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

class Dropdown(Widget):
	def __init__(self, pos, values):
		self.pos = pos
		self.values = values

		self.objects = []