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
myList = list(myWord)
secret = []

for word in myList:
  secret.append("_")

while True:
  if choice == myWord:
    print("It's a correct match. You won!!")
    break
  else:
    print("Not a match")
    pass
    misses = 0
    while misses < 7:
      print(frameList[misses])
      guess = input("Guess a letter: ")
      if guess in myList:
        print("That letter is in the word")
        print(myList)
      else:
        misses += 1
        if misses == 7: 
          print("Game Over. Please try again.")

print(myList)