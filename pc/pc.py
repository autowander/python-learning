import threading, queue, random, time

def productor(id, q):
	while True:
		time.sleep(3)
		num = random.randint(1, 1000)
		q.put(num)
		print('线程%d生产了数据%d'%(id, num))
	q.task_done()
	
def consumer(id, q):
	while True:
		num = q.get()
		if num is None:
			break
		print('线程%d消费了数据%d'%(id, num))
		time.sleep(2)
	q.task_done()
	
if __name__ == '__main__':
	q = queue.Queue()
	
	for i in range(4):
		threading.Thread(target=productor, args=(i, q)).start()
		
	for i in range(3):
		threading.Thread(target=consumer, args=(i, q)).start()
	