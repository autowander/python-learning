import asyncio

async def execute(n):
	print("Numbersss:", n)
	return n
	
corutine = execute(2)
print('Corutine:', corutine)
print('After calling execute')

loop = asyncio.get_event_loop()
task = loop.create_task(corutine)
print('Task:', task)
loop.run_until_complete(task)
print('Task:', task)
print('After calling loop')