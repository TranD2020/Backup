price = 0
given = 0
change = 0
dollars = 0
halfDollars = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0

price = float(input("What is the price? $"))
given = float(input("What is the given amount? $"))
change = given - price
print("Change: " + str(change))

pennies = change * 100


dollars = int(pennies / 100)
pennies = pennies % 100

halfDollars = int(pennies / 50)
pennies = pennies % 50

quarters = int(pennies / 25)
pennies = pennies % 25

dimes = int(pennies / 10)
pennies = pennies % 10 

nickels = int(pennies / 5)
pennies = int(pennies % 5)

print("Dollars: " + str(dollars))
print("Half-Dollars: " + str(halfDollars))
print("Quarters: " + str(quarters))
print("Dimes: " + str(dimes))
print("Nickels: " + str(nickels))
print("Pennies: " + str(pennies))