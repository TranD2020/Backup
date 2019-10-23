# Dennis Tran
# period 6

# variable Declaration and assignment
myVariable = "Dennis" # String variable
myNumber = 12 # int variable
myDecimal = 12.6 # float variable

# Make a variable of type String
myVar = "Hello Com"

# while loops
x = 1
while x <= 10:
	print(x)
	x += 1
# challenge: Make a while loop to count down from 100 to 1
x = 100
while x >= 1:
	print(x)
	x -= 1
# string concatenation
# example
string1 = "Hello "
string2 = "world "
print(string1 + string2 + "!")

# challenge: Make a variable with your favorite movie
Com1 = "Paul Blart Mall Cop 2"
# print "My favorite movie is "
print("My favorite movie is " + Com1)

# input
# Example
yourName = input("What is your name? ")
print("Hello " + yourName)

# Challenge
# prompt for favorite song
FavSong = input("What is your favorite song? ")
# print your favorite song is ... 
print("Your favorite song is " + FavSong)
# casting change one type into another
myNum = input("Enter a number: ") # myNum is a string type
myNum = int(myNum) + 10 #myNum is now an int
print("The answer is " + str(myNum))

# ask for two numbers, add them, and print the sum
number1 = input("Type a number: ")
number2 = input("Type a 2nd number: ")

print(number1 + "+" + number2 + "=" + str(int(number1) + int(number2)))
# if and if/else
# example
num = int(input("What is your number: "))

if num > 100:
	print("Your number is more than 100")
elif num == 100:
	print("Your number is 100")
else:
	print("Your number is less than 100")

# challenge ask if today is your birthday
# if it is print happy birthday
birthday = input("Is today your birthday(yes/no): ")
if birthday == "yes": 
	print("Happy Birthday")
elif birthday == "no": 
	print("Have a good day anyway")
else:
	print("Please read directions")
