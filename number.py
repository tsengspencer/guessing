import random 
r = random.randint(1,100)
count = 0 
while True:
	count += 1 # count = count + 1
	num = int(input("請猜數字"))
	if num == r:
		print("你猜對了!")
		print("這是你猜的第", count,"次")
		break #逃出while loop
	elif num > r : 
		print("比答案大")
	elif num < r : 
		print("比答案小")
	print("這是你猜的第", count,"次")
