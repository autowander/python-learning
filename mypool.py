from multiprocessing import Pool
import os, time, random

def long_time_task(name):
	print('Run task %s (%s)...'%(name, os.getpid()))
	start = time.time()
	time.sleep(random.random()*3)
	end = time.time()
	print('Task %s runs %0.2f second'%(name, (end-start)))
	
if __name__ == '__main__':
	print('Parent process %s'%os.getpid())
	p = Pool()	#默认是cpu核心数
	for i in range(9):
		p.apply_async(long_time_task, args=(i,))
	print('Waiting for all subprocesses done...')
	p.close()	#close后，进程池内无法再加入子进程
	p.join()	#等待所有子进程结束
	print('All subprocesses done')