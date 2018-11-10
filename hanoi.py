def hanoi(n, one, two, three):
	if n==1:
		print(one, '-->', three)
		return
	hanoi(n-1, one, three ,two)
	hanoi(1, one, two, three)
	hanoi(n-1, two, one, three)

if __name__=='__main__':
	num = int(input('输入碟子数量:'))
	hanoi(num, 'a', 'b', 'c')