# Make a list
myClasses = ["Algebra", "English", "World History"]
print(myClasses)

# add an item to the list
# append or insert
# append will add to the back of the list 
myClasses.append("Coding")
print(myClasses)
favClass = input("What is your favorite class? ")
myClasses.append(favClass)
print(myClasses)
# insert
myClasses.insert(3, "Art")
print(myClasses)
# overwrite
myClasses[4] = "Science"
print(myClasses)

# remove list items
# remove, pop
# remove will remove a specific item
myClasses.remove("Science")
print(myClasses)
# myClasses.remove("Lunch")
# pop will remove the item at a specific index
myClasses.pop() # erases the last item
print(myClasses)
myClasses.pop(1)
print(myClasses)
# len - it returns the length of a list
print("myClasses is " + str(len(myClasses)) + " items long")

print(myClasses[len(myClasses) - 1])

# loop through a list
count = 1
for aClass in myClasses:
	print("Item " + str(count) + " is " + aClass)
	count = count + 1

numbers = [1, 23, 47, 65, 89, 32, 54, 76]
# challenge: loop through the list add the numbers and print the sum
total = 0
for aNum in numbers:
	total += aNum

print(total)
myClasses.append("cooking")
#.append("cooking")
if "cooking" in myClasses:
	print("Have fun cooking")
else: 
	print("Ok then")
