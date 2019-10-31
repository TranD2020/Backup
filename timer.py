import time
import os

# variables
hours = 0
minutes = 0
seconds = 0

# input
print("Enter the number of hours, minutes, and seconds to set the timer")
hours = int(input("hours: "))
minutes = int(input("minutes: "))
seconds = int(input("seconds: "))

# for cash register use price = float(input("Price"))
# convert to seconds
minutes += hours * 60
seconds += minutes * 60
# set minutes and hours to 0
minutes = 0
hours = 0

while seconds >= 0:
	# convert to hours and minutes
	minutes = int(seconds / 60)
	seconds = seconds % 60


	hours = int(minutes/60)
	minutes = minutes % 60

	print(str(hours)+ ":" + str(minutes) + ":" + str(seconds))

	# convert to seconds
	minutes += hours * 60
	seconds += minutes * 60
	# set minutes and hours to 0
	minutes = 0
	hours = 0

	# pause for 1 second
	time.sleep(1)
	# clear the screen
	os.system("cls")
	seconds -= 1

print("Time's up!")