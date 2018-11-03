import time, threading

num = 100
lock = threading.Lock()

def run_proc(co):
	print('子线程启动%s'%(threading.current_thread().name))
	global num
	for i in range(1000000):
		lock.acquire()
		try:
			num += co
			num -= co
		finally:
			lock.release()
		#with lock:			#with自动开关
		#	num += co
		#	num -= co
	print('子线程结束%s'%(threading.current_thread().name))
	
if __name__ == '__main__':
	print('主线程启动%s'%(threading.current_thread().name))
	t = threading.Thread(target=run_proc, args=(2,))
	k = threading.Thread(target=run_proc, args=(6,))
	t.start()
	k.start()
	t.join()
	k.join()
	print('主线程结束, num=%d'%num)