import random
start = int (input("請決定隨機數字範圍的開始值: "))
end = int(input ("請決定隨機數字範圍的結束值: "))
r = random.randint(start, end)
count = 0 
while True:
	num = int(input("請猜數字"))
	count += 1 
	if num == r:
		print("你猜對了!")
		print("這是你猜的第", count,"次")
		break #逃出while loop
	elif num > r : 
		print("比答案大")
	elif num < r : 
		print("比答案小")
	print("這是你猜的第", count,"次")
