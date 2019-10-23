import time
import random 
myWord = ["beautiful", "apples", "ninjas", "pirates", "car"]
Mr = 0
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

print(frameList[Mr]) 

for frame in frameList:
	pass


myString = "arizona"
myList = list(myWord)
print(myList)
secret = []

for a in myList:
	secret.append(" _ ")
print(secret)