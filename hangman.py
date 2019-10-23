import time
import random 

misses = 0
frameList = [
'''
    +---+
    |	|
        |
        |
        |
       ===''','''
    +---+
    |   |
    O   |
        |
        |
       ===''','''
    +---+
    |   |
    O   |
   /    |
        |
       ===''','''
    +---+
    |   |
    O   |
   /|   |
        |
       ===''','''
    +---+
    |   |
    O   |
   /|\\  |
        |
       ===''','''
    +---+
    |   |
    O   |
   /|\\  |
   /    |
       ===''','''
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
       ==='''
]

myWord = ["beautiful", "apples", "ninjas", "pirates", "car"]

myList = list(myWord)
print(myList)
secret = []

for a in myList:
	secret.append(" _ ")
print(secret)

while misses < 7:
	print(frameList[misses])
	guess = input("Guess a letter: ")
	if guess in myWord:
		print("That letter is in the secret word")
	else:
		misses += 1