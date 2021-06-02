import os

def cpr(parentFile, pasteDir, names):
	parentFileContent = open(parentFile, "rb").read()
	extension = os.path.splitext(parentFile)[1]
	for name in names:
		name = str(name)
		currentDir = os.path.join(pasteDir, name)+extension
		currentFile = open(currentDir, "wb")
		currentFile.write(parentFileContent)
		currentFile.close()

def xor(a, b):
	aX = 1 if a != 0 else 0
	bX = 1 if b != 0 else 0
	mask = aX | bX
	if mask == 1 and aX == 1:
		val = max(a, b)
	elif mask == 1 and bX == 1:
		val = max(a, b)
	else:
		val = 0

	return val

def tupleRange(a, b):
	xList = []
	yList = []
	for x in zip(range(a[0], b[0]+1)):
		xList.append(x[0])
	for y in zip(range(a[1], b[1]+1)):
		yList.append(y[0])
	tuples = []
	lastX = 0
	lastY = 0
	endAt = max(len(xList), len(yList))
	index = 0
	while True:
		try: 
			lastX = xList[index]
		except:
			pass
		try:
			lastY = yList[index]
		except:
			pass
		tuples.append((lastX, lastY))
		if index >= endAt:
			break
		index += 1
	return tuples

class arrangement():
	def __init__(self, pattern = [
			[1,1,1],
			[1,0,1],
			[1,1,1]
		]):
		self.pat = pattern

	def __add__(self, other):
		newPattern = [[0,0,0], [0,0,0], [0,0,0]]
		for x1, x2, indX in zip(self.pat, other.pat, range(len(other.pat))):
			for y1, y2, indY in zip(x1, x2, range(len(x2))):
				newPattern[indX][indY] = xor(y1, y2)

		return arrangement(newPattern)

	def __repr__(self):
		string = ""
		for x1 in self.pat:
			string += "\n"
			for y1 in x1:
				string += f"{y1}"

		return string

	@property
	def T(self):

		return self.pat[0][1]

	@property
	def B(self):

		return self.pat[2][1]

	@property
	def R(self):

		return self.pat[1][2]

	@property
	def L(self):

		return self.pat[1][0]

	@property
	def TR(self):

		return self.pat[0][2]

	@property
	def BR(self):

		return self.pat[2][2]

	@property
	def TL(self):

		return self.pat[0][0]

	@property
	def BL(self):

		return self.pat[2][0]

class Top(arrangement):
	def __init__(self):
		super().__init__([
			[1,1,1],
			[0,0,0],
			[0,0,0]
		])

class Down(arrangement):
	def __init__(self):
		super().__init__([
			[0,0,0],
			[0,0,0],
			[1,1,1]
		])

class Left(arrangement):
	def __init__(self):
		super().__init__([
			[1,0,0],
			[1,0,0],
			[1,0,0]
		])

class Right(arrangement):
	def __init__(self):
		super().__init__([
			[0,0,1],
			[0,0,1],
			[0,0,1]
		])

class TopLeft(arrangement):
	def __init__(self):
		super().__init__([
			[1,0,0],
			[0,0,0],
			[0,0,0]
		])

class DownLeft(arrangement):
	def __init__(self):
		super().__init__([
			[0,0,0],
			[0,0,0],
			[1,0,0]
		])

class TopRight(arrangement):
	def __init__(self):
		super().__init__([
			[0,0,1],
			[0,0,0],
			[0,0,0]
		])

class DownRight(arrangement):
	def __init__(self):
		super().__init__([
			[0,0,0],
			[0,0,0],
			[0,0,1]
		])

def clamp(num, min_value, max_value):
	return max(min(num, max_value), min_value)

class Ratio:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def getRatioFromA(self, a):
		return a*(self.b/self.a)

	def getRatioFromB(self, b):
		return b*(self.a/self.b)

def stripList(l):
	indices, values = [], []
	for i, indX in zip(l, range(len(l)-1)):
		for j, indY in zip(i, range(len(i)-1)):
			indices.append((indX, indY))
			values.append(j)

	return indices, values

