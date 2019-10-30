num = int(input("What number to check: "))

print("Checking number... ")

for num in range(100):
	count(num)

if num % 3 == 0:
	print("Your number is a multiple of 3")
else:
	print("Your number is not a multiple of 3")
if num % 5 == 0:
	print("Your number is a multiple of 5")
else:
	print("Your number is not a multiple of 5")


print("Fizz")
print("Buzz")

print("Fizz", end="")
print(" Buzz")
