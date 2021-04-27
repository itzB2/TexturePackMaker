from ctm.utils import *
from ctm.Constants import *
from PIL import Image
import os

def calculateSides(path):
	image = Image.open(path)
	res = image.size[0]
	top = [(1,0), (res-2, 0)]
	left = [(0,1), (0, res-2)]
	bottom = [(1, res-1), (res-2, res-1)]
	right = [(res-1, 1), (res-1, res-2)]
	topLeft = (0,0)
	topRight = (res-1, 0)
	bottomLeft = (0, res-1)
	bottomRight = (res-1, res-1)
	# print(bottomRight)

	sides = {
	"T":top,
	"B":bottom,
	"L":left,
	"R":right,
	"TL":topLeft,
	"TR":topRight,
	"BL":bottomLeft,
	"BR":bottomRight,
	}

	return sides

def getClearPixels(sides, clear):
	clearImage = Image.open(clear)
	left = []
	right = []
	top = []
	bottom = []
	topLeft = ()
	topRight = ()
	bottomLeft = ()
	bottomRight = ()

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

	clearPixels = {
	"T":top,
	"B":bottom,
	"L":left,
	"R":right,
	"TL":topLeft,
	"TR":topRight,
	"BL":bottomLeft,
	"BR":bottomRight,
	}

	return clearPixels

class Full():
	def __init__(self, path, directory, noSidesImage, blockID, blockName, metadata, sideMethod = "", preset = CTMFULLDEFAULTPRESET):
		self.p = path
		self.dir = directory
		self.sides = calculateSides(path)
		self.clearSides = getClearPixels(self.sides, noSidesImage)
		self.preset = preset
		self.id = blockID
		self.name = blockName
		self.sidsMethod = sideMethod
		self.m = metadata

	def run(self):
		for currentFileName in list(range(47)):
			currentFilePath = os.path.join(self.dir, str(currentFileName)+".png")
			currentFile = Image.open(self.p)
			currentFileImage = currentFile.load()
			presetLookup = self.preset[currentFileName]
			# print(currentFileName, currentFilePath, presetLookup)
			if presetLookup.T == 0:
				for topIndex, clearPixels in zip(tupleRange(self.sides["T"][0], self.sides["T"][1]), self.clearSides["T"]):
					currentFileImage[topIndex[0], topIndex[1]] = clearPixels
			if presetLookup.B == 0:
				for bottomIndex, clearPixels in zip(tupleRange(self.sides["B"][0], self.sides["B"][1]), self.clearSides["B"]):
					currentFileImage[bottomIndex[0], bottomIndex[1]] = clearPixels
			if presetLookup.R == 0:
				for rightIndex, clearPixels in zip(tupleRange(self.sides["R"][0], self.sides["R"][1]), self.clearSides["R"]):
					currentFileImage[rightIndex[0], rightIndex[1]] = clearPixels
			if presetLookup.L == 0:
				for leftIndex, clearPixels in zip(tupleRange(self.sides["L"][0], self.sides["L"][1]), self.clearSides["L"]):
					currentFileImage[leftIndex[0], leftIndex[1]] = clearPixels
			if presetLookup.TR == 0:
				currentFileImage[self.sides["TR"][0], self.sides["TR"][1]] = self.clearSides["TR"]
			if presetLookup.TL == 0:
				currentFileImage[self.sides["TL"][0], self.sides["TL"][1]] = self.clearSides["TL"]
			if presetLookup.BR == 0:
				currentFileImage[self.sides["BR"][0], self.sides["BR"][1]] = self.clearSides["BR"]
			if presetLookup.BL == 0:
				currentFileImage[self.sides["BL"][0], self.sides["BL"][1]] = self.clearSides["BL"]
			# print(currentFilePath)
			currentFile.save(currentFilePath)
		genProps(self.sidsMethod, self.name, self.id, self.dir, 46, "ctm", self.m)
