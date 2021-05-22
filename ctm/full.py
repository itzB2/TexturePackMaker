from ctm.utils import *
from ctm.Constants import *
from PIL import Image
import os

def calculateSides(path, el):
	image = Image.open(path)
	res = image.size[0]
	sides = []
	for edge in range(1, el+1):
		top = [(edge,edge-1), (res-(edge+1), edge-1)]
		left = [(edge-1,1+(edge-1)), (edge-1, res-(edge+1))]
		bottom = [(1, res-edge), (res-(edge+1), res-edge)]
		right = [(res-edge, 1), (res-edge, res-(edge+1))]
		topLeft = (edge-1,edge-1)
		topRight = (res-edge, edge-1)
		bottomLeft = (edge-1, res-edge)
		bottomRight = (res-edge, res-edge)

		EdgeLoop = {
		"T":top,
		"B":bottom,
		"L":left,
		"R":right,
		"TL":topLeft,
		"TR":topRight,
		"BL":bottomLeft,
		"BR":bottomRight,
		}

		# print(EdgeLoop)
		sides.append(EdgeLoop)

	return sides

def getClearPixels(sidesFull, clear):
	clearImage = Image.open(clear)
	el = len(sidesFull)

	clearPixels = []
	for EdgeLoop in range(el):
		left = []
		right = []
		top = []
		bottom = []
		topLeft = ()
		topRight = ()
		bottomLeft = ()
		bottomRight = ()
		sides = sidesFull[EdgeLoop]
		#Top Side
		for topIndex in tupleRange(sides["T"][0], sides["T"][1]):
			top.append(clearImage.getpixel(topIndex))

		#Bottom Side
		for bottomIndex in tupleRange(sides["B"][0], sides["B"][1]):
			bottom.append(clearImage.getpixel(bottomIndex))

		#Left Side
		for leftIndex in tupleRange(sides["L"][0], sides["L"][1]):
			left.append(clearImage.getpixel(leftIndex))

		#Right Side
		for rightIndex in tupleRange(sides["R"][0], sides["R"][1]):
			right.append(clearImage.getpixel(rightIndex))

		#Corners
		topLeft = clearImage.getpixel(sides["TL"])
		topRight = clearImage.getpixel(sides["TR"])
		bottomLeft = clearImage.getpixel(sides["BL"])
		bottomRight = clearImage.getpixel(sides["BR"])
		# print(bottomRight)

		clearPixelsED = {
		"T":top,
		"B":bottom,
		"L":left,
		"R":right,
		"TL":topLeft,
		"TR":topRight,
		"BL":bottomLeft,
		"BR":bottomRight,
		}

		clearPixels.append(clearPixelsED)

	return clearPixels

class Full():
	def __init__(self, path, directory, noSidesImage, blockID, blockName, metadata, EdgeLength, sideMethod = "", preset = CTMFULLDEFAULTPRESET):
		self.p = path
		self.dir = directory
		self.sides = calculateSides(path, EdgeLength)
		self.clearSides = getClearPixels(self.sides, noSidesImage)
		self.preset = preset
		self.id = blockID
		self.name = blockName
		self.sidsMethod = sideMethod
		self.m = metadata
		self.el = EdgeLength

	def run(self):
		for currentFileName in list(range(47)):
			currentFilePath = os.path.join(self.dir, str(currentFileName)+".png")
			currentFile = Image.open(self.p)
			currentFileImage = currentFile.load()
			presetLookup = self.preset[currentFileName]

			for eLoop in range(self.el):
				EdgeSides = self.sides[eLoop]
				EdgeClearSides = self.clearSides[eLoop]
				if presetLookup.T == 0:
					for topIndex, clearPixels in zip(tupleRange(EdgeSides["T"][0], EdgeSides["T"][1]), EdgeClearSides["T"]):
						currentFileImage[topIndex[0], topIndex[1]] = clearPixels
				if presetLookup.B == 0:
					for bottomIndex, clearPixels in zip(tupleRange(EdgeSides["B"][0], EdgeSides["B"][1]), EdgeClearSides["B"]):
						currentFileImage[bottomIndex[0], bottomIndex[1]] = clearPixels
				if presetLookup.R == 0:
					for rightIndex, clearPixels in zip(tupleRange(EdgeSides["R"][0], EdgeSides["R"][1]), EdgeClearSides["R"]):
						currentFileImage[rightIndex[0], rightIndex[1]] = clearPixels
				if presetLookup.L == 0:
					for leftIndex, clearPixels in zip(tupleRange(EdgeSides["L"][0], EdgeSides["L"][1]), EdgeClearSides["L"]):
						currentFileImage[leftIndex[0], leftIndex[1]] = clearPixels
				if presetLookup.TR == 0:
					currentFileImage[EdgeSides["TR"][0], EdgeSides["TR"][1]] = EdgeClearSides["TR"]
				if presetLookup.TL == 0:
					currentFileImage[EdgeSides["TL"][0], EdgeSides["TL"][1]] = EdgeClearSides["TL"]
				if presetLookup.BR == 0:
					currentFileImage[EdgeSides["BR"][0], EdgeSides["BR"][1]] = EdgeClearSides["BR"]
				if presetLookup.BL == 0:
					currentFileImage[EdgeSides["BL"][0], EdgeSides["BL"][1]] = EdgeClearSides["BL"]				

			currentFile.save(currentFilePath)
		genProps(self.sidsMethod, self.name, self.id, self.dir, 46, "ctm", self.m)
