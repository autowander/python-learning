import asyncio, requests, time

#异步协程版
async def request(url):
	status = requests.get(url)
	return status
	
def callback(res):
	print('Status:', res.result())
	
#corutine = request('https://www.baidu.com')
#task = asyncio.ensure_future(corutine)
#task.add_done_callback(callback)
urls = [
	'https://www.baidu.com',
	'https://www.baidu.com',
	'https://www.sohu.com',
]
tasks = [asyncio.ensure_future(request(url)) for url in urls]
#tasks.add_done_callback(callback)
print('Tasks:', tasks)

loop = asyncio.get_event_loop()
start = time.time()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print('time:', end - start)
#print('Task:', task)
