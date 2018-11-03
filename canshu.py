def add_end(t=[]):
	t.append('END')
	print(id(t))
	return t

a = add_end()
b = add_end()
#c = add_end()
print(a)
print(id(a))

#可变参数
def calc(*nums):
	sum = 0
	for n in nums:
		sum = sum + n*n
	return sum

print(calc(1,2,3))
print(calc(*[1,2,3,4]))

#关键字参数
def person(name, age, **kw):
	print('name:', name)
	print('age:', age)
	print('kw:', kw)
	
person('wf', '21', city='jiax')

#命名关键字参数
def kid(name, age, *, city):
	print('name:', name)
	print('age:', age)
	print('city:', city)

kid('yyp', '17', city='chaoyang')