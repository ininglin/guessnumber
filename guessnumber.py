#1~100隨機猜數字

import random
start = input('請決定隨機數字範圍的開始值:')
end = input('請決定隨機數字範圍的結束值:')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
	count += 1 #count = count + 1
	number = input('請猜一個數字:')
	number = int(number)
	if number == r:
		print('答對了')
		print('這是你猜的第',count,'次')
		break
	else:
		if number > r:
			print('請輸入較小數字')
		else:
			print('請輸入較大數字')
	print('這是你猜的第',count,'次')
		
