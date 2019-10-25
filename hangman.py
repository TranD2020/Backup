import time
import random 

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

choice = input("Type a word: ")
myWord = "beautiful"
guessList = list("_________")

if choice == myWord:
  print("It's a match")
else:
  print("Not a match")

misses = 0

while misses < 7:
	print(frameList[misses])
	guess = input("Guess a letter: ")
	if guess in guessList:
		print("That letter is in the word")
	else:
		misses += 1
   print(guessList)
index = 0
for letter in mystery:
  if letter == guess:
    guessList[index] = guess 
  index += 1

print(guessList)

