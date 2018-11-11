import asyncio, threading, time

@asyncio.coroutine
def hello():
	print('Hello world! (%s)'%threading.currentThread())
	#异步调用asyncio.sleep(1)
	r = yield from asyncio.sleep(1)		#模拟IO请求延时
	print('Hello again (%s)'%threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()