import threading, queue, random, time

def productor(c):
	next(c) #切换到consumer
	for i in range(4):
		time.sleep(2)
		num = random.randint(1, 1000)
		print('produce:', num)
		r = c.send(num)  #切换到consumer
		print('produce: consumer return ', r)
	
def consumer():
	r = ''
	while True:
		time.sleep(2)
		n = yield r   #通过yield得到消息，并将结果传回
		if not n:
			return
		print('consumer:', n)
		r = '200 OK'
	
if __name__ == '__main__':
	c = consumer()
	productor(c)
	