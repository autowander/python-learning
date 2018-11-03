from classmultipro import mymulti

if __name__ == '__main__':
	print('主进程启动')
	m = mymulti('yyp')
	m.start()
	m.join()
	print('主进程结束')