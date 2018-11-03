import time
import functools

def deco_new(func):
	#@functools.wraps(func)		#wrapper.__name__ = func.__name__将原函数的name赋值给func
	def wrapper(*args, **kw):
		startTime = time.time()
		func(args)
		endTime = time.time()
		print(func.__name__)
		msecs = (endTime-startTime)*1000
		print('time is %d ms'%msecs)
	return wrapper


@deco_new		#myhi = deco_new(myhi)等于执行了这一步操作，myhi的name变成了wrapper
def myhi(name):	#执行myhi实际上是在执行wrapper
	name = input();
	print("hello")
	print(name)
	time.sleep(1)

	
myhi()
print(myhi.__name__) #wrapper


def metric(fn):
    @functools.wraps(fn)			#将原函数的name赋值给fn
    def wrapper(*args, **kw):
        start = time.time()
        result = fn(*args)
        end = time.time()
        print('%s execute in %s ms' %(fn.__name__,end-start))
        return result
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

if __name__=='__main__':
	f = fast(11, 22)
	s = slow(11, 22, 33)
	if f == 33:
		print('测试成功!')
	elif s == 7986:
		print('测试成功!')
