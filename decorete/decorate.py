

def func1(name):
	print('djfhjgf%s'%name)
	
	
def outer(func):
	def inner():
		print('ccccc')
		func()
	return inner
	
func1 = outer(func1)
func1()
print(func1.__name__)