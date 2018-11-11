class ImageRepository:
	def __init__(self):
		self.image_id = -1
		
	def __iter__(self):
		return self
		
	def __next__(self):
		self.image_id += 1
		return self.image_id
		
def iamge_repository():
	image_id = -1
	while True:
		image_id += 1
		yield image_id
		
def odds(n):
	for i in range(n):
		if i%2 == 1:
			yield i

def odd_even(n):
	yield from odds(n)
		
for image in iamge_repository():
	print(image)
	if image==10:
		break
		
for image in ImageRepository():
	print(image)
	if image==10:
		break
		
for odd in odd_even(30):
	print(odd)