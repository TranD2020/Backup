price = 0
given = 0
change = 0
dollars = 0
halfDollars = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0

price = float(input("What is the price? "))
given = float(input("What is the given amount? "))
change = given - price
print("Change: " + str(change))

halfDollars += dollars * 2
quarters += halfDollars * 2
dimes += quarters * 2.5
nickels += dimes * 2
pennies += nickels * 5


dollars = int(pennies / 100)
pennies = pennies % 100

halfDollars = int(pennies / 50)
pennies = pennies % 50

quarters = int(pennies / 25)
pennies = pennies % 25

dimes = int(pennies / 10)
pennies = pennies % 10 

nickels = int(pennies / 5)
pennies = pennies % 5

print("Dollars: " + dollars)
print("Half-Dollars: " + halfDollars)
print("Quarters: " + quarters)
print("Dimes: " + dimes)
print("Nickels: " + nickels)
print("Pennies: " + pennies)