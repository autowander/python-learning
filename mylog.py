import logging
logging.basicConfig(level=logging.INFO)
def bar(s):
	return 10/int(s)

def main():
	try:
		bar('0')
	except Exception as e:
		logging.exception(e)
		
if __name__ == '__main__':
	main()
	logging.info('log info')
	print("END")