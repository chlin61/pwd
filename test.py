import random
r = random.randint(1,100)
count = 0
while True:
	count = count + 1
	n = int(input('輸入你要猜的數字:'))
	##print('這是你猜了第', n, '次...')
	if n > r:
		print('你猜的結果比答案大')
	elif n < r:
		print('你猜的結果比答案小')
	else:
		print('你猜對了!，你共猜了', count,'次')
		break


