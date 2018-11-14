import aiohttp, asyncio, time, requests

start = time.time()

async def get(url):
	session = aiohttp.ClientSession()
	response = await session.get(url)
	result = await response.text()
	session.close()
	return result


async def request():
	#url = 'http://127.0.0.1:5000'
	url = 'https://www.baidu.com'
	print('Waiting for', url)
	result = await get(url)
	#print('Get response from', url, 'Result: Hello!')
	
tasks = [asyncio.ensure_future(request()) for _ in range(5)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('Cost time:', end-start)

'''
start = time.time()
 
def request1():
	url = 'http://127.0.0.1:5000'
	#url = 'https://www.baidu.com'
	print('Waiting for', url)
	result = requests.get(url).text
	#print('Get response from', url, 'Result: Hello!')
	
for _ in range(5):
	request1()
	
end = time.time()
print('Cost time:', end - start)'''