def test():
	i = 1
	while i<7:
		n = yield i
		if i==6:
			return 100
		i += 1
		
def yf():
	val = yield from test()
	print(val)
	
t = yf()
t.send(None)
j=0
while j<6:
	j+=1
	try:
		print(t.send(j))
	except StopIteration as e:
		print('error')