count = 1
while count <= 100:
	print(count, end="")
	if count % 3==0:
		print("Fizz ", end="")
	if count % 5==0:
		print("Buzz", end="")
	print("")
	count += 1
