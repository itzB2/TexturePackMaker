from PIL import Image
from utils.Image import *
from utils.funcs import *
from utils.ctm.genFiles import *
import os

CTMFULLDEFAULTPRESET = {
	0:arrangement(),
	1:Top()+Left()+Down(),
	2:Top()+Down(),
	3:Top()+Right()+Down(),
	4:Top()+Left()+DownRight(),
	5:Top()+Right()+DownLeft(),
	6:Left()+TopRight()+DownRight(),
	7:Top()+DownLeft()+DownRight(),
	8:TopLeft()+DownLeft()+DownRight(),
	9:DownLeft()+TopLeft()+TopRight(),
	10:TopLeft()+DownLeft(),
	11:DownLeft()+DownRight(),
	12:Left()+Right()+Top(),
	13:Top()+Left(),
	14:Top(),
	15:Top()+Right(),
	16:Left()+Down()+TopRight(),
	17:Right()+Down()+TopLeft(),
	18:Down()+TopLeft()+TopRight(),
	19:Right()+TopLeft()+DownLeft(),
	20:DownLeft()+DownRight()+TopRight(),
	21:TopLeft()+TopRight()+DownRight(),
	22:TopLeft()+TopRight(),
	23:TopRight()+DownRight(),
	24:Left()+Right(),
	25:Left(),
	26:arrangement([[0,0,0],[0,0,0],[0,0,0]]),
	27:Right(),
	28:Left()+TopRight(),
	29:Top()+DownRight(),
	30:Left()+DownRight(),
	31:Top()+DownLeft(),
	32:DownRight(),
	33:DownLeft(),
	34:TopLeft()+DownRight(),
	35:TopRight()+DownLeft(),
	36:Left()+Right()+Down(),
	37:Left()+Down(),
	38:Down(),
	39:Down()+Right(),
	40:Down()+TopRight(),
	41:Right()+DownLeft(),
	42:Down()+TopRight(),
	43:Right()+TopLeft(),
	44:TopRight(),
	45:TopLeft(),
	46:TopLeft()+TopRight()+DownLeft()+DownRight()
}

def full(path, noSidesImage, directory, blockID, blockName, metadata, save, EdgeLength=1, sideMethod = "", preset = CTMFULLDEFAULTPRESET):

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
		clearImage = BlockTexture(Image.open(clear).size[0], Image.open(clear).size[1], Image.open(clear))
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
			top = clearImage.getPixels(tupleRange(sides["T"][0], sides["T"][1]))

			#Bottom Side
			bottom = clearImage.getPixels(tupleRange(sides["B"][0], sides["B"][1]))

			#Left Side
			left = clearImage.getPixels(tupleRange(sides["L"][0], sides["L"][1]))

			#Right Side
			right = clearImage.getPixels(tupleRange(sides["R"][0], sides["R"][1]))

			#Corners
			topLeft = clearImage.getPixel(sides["TL"])
			topRight = clearImage.getPixel(sides["TR"])
			bottomLeft = clearImage.getPixel(sides["BL"])
			bottomRight = clearImage.getPixel(sides["BR"])

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

	p = path
	dir = directory
	sides = calculateSides(path, EdgeLength)
	clearSides = getClearPixels(sides, noSidesImage)
	id = blockID
	name = blockName
	m = metadata
	el = EdgeLength

	ctmImages = {}

	for currentFileName in list(range(47)):
		currentFilePath = os.path.join(dir, str(currentFileName)+".png")
		currentFile = BlockTexture(16, 16, Image.open(p))
		presetLookup = preset[currentFileName]

		for eLoop in range(el):
			EdgeSides = sides[eLoop]
			EdgeClearSides = clearSides[eLoop]
			if presetLookup.T == 0:
				currentFile.setPixels(tupleRange(EdgeSides["T"][0], EdgeSides["T"][1]), EdgeClearSides["T"])
			if presetLookup.B == 0:
				currentFile.setPixels(tupleRange(EdgeSides["B"][0], EdgeSides["B"][1]), EdgeClearSides["B"])
			if presetLookup.R == 0:
				currentFile.setPixels(tupleRange(EdgeSides["R"][0], EdgeSides["R"][1]), EdgeClearSides["R"])
			if presetLookup.L == 0:
				currentFile.setPixels(tupleRange(EdgeSides["L"][0], EdgeSides["L"][1]), EdgeClearSides["L"])
			if presetLookup.TR == 0:
				currentFile.setPixel(EdgeSides["TR"], EdgeClearSides["TR"])
			if presetLookup.TL == 0:
				currentFile.setPixel(EdgeSides["TL"], EdgeClearSides["TL"])
			if presetLookup.BR == 0:
				currentFile.setPixel(EdgeSides["BR"], EdgeClearSides["BR"])
			if presetLookup.BL == 0:
				currentFile.setPixel(EdgeSides["BL"], EdgeClearSides["BL"])

		if save:
			currentFile.save(currentFilePath)
		else:
			ctmImages[currentFileName] = currentFile
	if save:
		genProps(sideMethod, name, id, dir, 46, "ctm", m, save)
	else:
		ctmProps = genProps(sideMethod, name, id, dir, 46, "ctm", m, save)

		ctmImages["Properties"] = ctmProps
