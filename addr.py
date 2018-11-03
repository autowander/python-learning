class MyObject(object):
	def __init__(self):
		self.x = 9
	def add(self):
		self.y = 20
		return self.x + self.x
	def sub(self):
		return self.x - self.x
	def mul(self):
		return self.x * self.x

def run(x):
	inp = input("method>")
	if hasattr(computer, inp):
		func = getattr(computer, inp)
		print(func())
	else:
		setattr(computer, inp, lambda x:x+1)
		func = getattr(computer, inp)
		print(func(x))


if __name__ == "__main__":		
	computer = MyObject()
	#print(computer.add())
	run(10)
	print(computer.y)