class Animal(object):
	def run(self):
		print('Amimal is running')
	'''
	def run_twice(Animal):
		Animal.run()
		Animal.run()
	'''
	
class Dog(Animal):
	def run(self):
		print("Dog is running")
	
class Cat(Animal):
	def run(self):
		print("Cat is running")

#只要类中有相同的方法，就可以使用多态
class Dfg(object):
	def run(self):
		print("Dfg is running")


def run_twice(Animal):
		Animal.run()
		Animal.run()		
		
if __name__ == '__main__':
	a = Animal()
	d = Dog()
	c = Cat()
	k = Dfg()		#非animal类型
	
	run_twice(d)
	run_twice(k)	#执行成功了
	#a.run_twice()
	#d.run_twice()
	#c.run_twice()