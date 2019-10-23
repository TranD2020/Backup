print("Welcome to the To Do List!")
todoList = []
while True:
	print("Enter a to add an item")
	print("Enter r to remove an item")
	print("Enter p to print the list")
	print("Enter q to quit")
	choice = input("Make your choice: ")

	if choice == "q":
		break
	elif choice == "a":
		# add an item to the list 
		Add = input("Add an item: ")
		todoList.append(Add)
		pass
	elif choice == "r":
		# remove an item from the list
		Rev = input("Remove an item: ")
		todoList.remove(Rev)
		pass
	elif choice == "p":
		# print the list
		print(todoList)
	else:
		print("This was not a choice, try again")