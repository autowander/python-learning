def gen():
	data = 'here'
	for i in range(3):
		data = yield data
		print('print200 Ok'+str(i)+data)
		data = '200 Ok'+str(i)+data
	
	
g = gen()
print(next(g))
print(g.send('9'))
print(g.send('10'))