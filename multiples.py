# how to check if 1 number is a multiple of another

num = int(input("What number to check: "))

print("Checking number... ")

if num % 3 == 0:
	print("Your number is a multiple of 3")
else:
	print("Your number is not a multiple of 3")
if num % 5 == 0:
	print("Your number is a multiple of 5")
else:
	print("Your number is not a multiple of 5")

# how to print without new lines
print("Fizz")
print("Buzz")

# same line
print("Fizz", end="")
print(" Buzz")