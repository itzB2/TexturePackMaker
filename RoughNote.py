class Add:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	@property
	def add(self):
		return self.a + self.b

a = Add(10, 10)

print(a.add)
	