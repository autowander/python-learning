#from multiprocessing import Pool
import time, os
import threading

def copy(fpath, tpath):
	fr = open(fpath, 'rb')
	fw = open(tpath, 'wb')
	
	context = fr.read()
	fw.write(context)
	fr.close()
	fw.close()
	
if __name__ == '__main__':
	filelist = os.listdir(r'C:\Users\wfengcd\Desktop\1')

#	start = time.time()
#	p = Pool(2)
#	for filename in filelist:
#		p.apply_async(copy, args=(os.path.join(r'C:\Users\wfengcd\Desktop\1', filename), os.path.join(r'C:\Users\wfengcd\Desktop\2', filename)))
#		
#	p.close()
#	p.join()
#	end = time.time()
#	print('总耗时%.2f'%(end-start))
	
#	start = time.time()
#	for filename in filelist:
#		copy(os.path.join(r'C:\Users\wfengcd\Desktop\1', filename), os.path.join(r'C:\Users\wfengcd\Desktop\2', filename))
#	end = time.time()
#	print('总耗时%.2f'%(end-start))
	