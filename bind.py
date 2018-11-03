from types import MethodType

class Student(object):
	__slots__ = ('name', 'age')		# 用tuple定义允许绑定的属性名称

class Sdf(Student):
	__slots__ = ('score',)
	def __len__(self):
		return 4

def set_age(self, age):
	self.age = age

def set_score(self, score):
	self.score = score

'''
s = Student()
s.name = 'yyp'
print(s.name)

s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

s2 = Student()
s2.name = 'xww'
Student.set_score = set_score
s.set_score(101)
s2.set_score(120)
print(s.score, s2.score)
'''
df = Sdf()
df.age = 20
#df.score = 20
print(df.age)
print(len(Sdf()))
