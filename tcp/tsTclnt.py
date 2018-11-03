from socket import *

HOST = 'wfengcd.cn'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
	data = input('>')
	if not data:
		break
	tcpCliSock.send(data.encode())
	data = tcpCliSock.recv(BUFSIZ)
	if not data:
		break
	print(data.decode('utf-8'))
tcpCliSock.close()