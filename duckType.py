class N1:
	def read(self):
		print('N1 reading')
		
# 继承N1
class N2(N1):
	def read(self):
		print('N2 reading')

# 没有继承关系的类		
class C:
	def read(self):
		print('C reading')

# 执行者类型		
class Do:
	def do_something(self, N1):
		N1.read()

if __name__ == '__main__':
	print(N1)
	N1 = N2()
	print(N1)
	N1.read()