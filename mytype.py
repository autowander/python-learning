def fn(self, name="world"):
	print("Hello , %s"%name)
	
Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
h.hello('yyp')

class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value: self.append(value)
		return type.__new__(cls, name, bases, attrs)
		#return type(name, bases, attrs)
		
class MyList(list, metaclass=ListMetaclass):			#会将类名name,父类bases,属性attr传给元类
	pass
	
L = MyList()
L.add(1)
print(L)
l = list()
l.append(20)
#l.add(2)
print(l)