import time
import os

frameList = [
'''
    +---+
    O   |
   /|\  |
   / \  |
       ===''','''
    +---+
   \O/  |
    |   |
    \\\\  |
       ===''','''
    +---+
        |  I'm Free!
    O   |
   /|\\  |
   / \\ ==='''
]

while True:
	for frame in frameList:
		os.system("cls")
		print(frame)
		time.sleep(5)

