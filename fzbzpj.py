count = 0
while count < 100:
	count += 1
	print(count)
	if count % 3==0:
		print(str(count) + " Fizz")
	if count % 5==0:
		print(str(count) + " Buzz")
	if count % 3 and 5==0:
		print(str(count) + " Fizz" + " Buzz")
