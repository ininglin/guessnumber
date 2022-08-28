#1~100隨機猜數字

import random
r = random.randint(1, 100)


while True:
	number = input('請猜一個數字:')
	number = int(number)
	if number == r:
		print('答對了')
		break
	else:
		if number > r:
			print('請輸入較小數字')
		else:
			print('請輸入較大數字')
		
