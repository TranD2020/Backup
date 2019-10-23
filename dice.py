# Name: Dennis Tran
# Period 6
# Dice Rolling Simulator
import random
random.randint(1,6)
# Welcome to Dice Game
print("Welcome to the Dice Game. ")

# Result Score
numOne = 0
numTwo = 0
numThree = 0
numFour = 0
numFive = 0
numSix = 0

def printNum():
	print("1s - " + str(numOne))
	print("2s - " + str(numTwo))
	print("3s - " + str(numThree))
	print("4s - " + str(numFour))
	print("5s - " + str(numFive))
	print("6s - " + str(numSix))
def printPercent():
	print("1s - " + str(numOne / 100 * 100) + "%")
	print("2s - " + str(numTwo / 100 * 100) + "%")
	print("3s - " + str(numThree / 100 * 100) + "%")
	print("4s - " + str(numFour / 100 * 100) + "%")
	print("5s - " + str(numFive / 100 * 100) + "%")
	print("6s - " + str(numSix / 100 * 100) + "%")

print("Input the number of times a 6 sided die will be rolled: ")
numRolls = int(input("how many rolls: "))
x = 1

while x <= numRolls: 
	x += 1
	RandNum = random.randint(1,6)
	print(RandNum)
	if RandNum == 1:
		numOne += 1
	elif RandNum == 2:
		numTwo += 1
	elif RandNum == 3:
		numThree += 1
	elif RandNum == 4:
		numFour += 1
	elif RandNum == 5:
		numFive += 1
	elif RandNum == 6:
		numSix += 1

print("Total Rolls: " + str(numRolls))
printNum()
printPercent()
	
	