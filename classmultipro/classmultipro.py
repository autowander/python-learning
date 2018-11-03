from multiprocessing import Process
import time

class mymulti(Process):
	def __init__(self, name):
		Process.__init__(self)
		self.__name = name
		
	def run(self):
		print('子进程启动%s'%self.__name)
		time.sleep(2.2)
		print('子进程结束')