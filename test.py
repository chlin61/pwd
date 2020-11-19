import random
r = random.randint(1,100)

while True:
	n = int(input('輸入你要猜的數字'))
	if n > r:
		print('答案比較小')
	elif n < r:
		print('答案比較大')
	else:
		print('你猜對了!')
		break


