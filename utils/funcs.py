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
