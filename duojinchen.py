from multiprocessing import Process
import os
#from time import sleep
balance = 0
def run_proc(name):
	print("启动子进程-%s"%name)
	global balance
	balance += 2
	print("子进程结束-%s-%d"%(name, balance))
	
if __name__ == '__main__':
	print("父进程启动")
	
	p = Process(target=run_proc, args=('test',))
	
	p.start()
	p.join()
	print('父进程结束--%d'%balance)