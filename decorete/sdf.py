def reverse(num):
	if num<0:
		num=-num
		print('-', end='')
	elif num==0:
		print(0)
	while num != 0:
		pet = num%10
		if pet!=0:
			print(pet, end='')
		num = num//10
			
if __name__=='__main__':
	num = int(input())
	reverse(num)