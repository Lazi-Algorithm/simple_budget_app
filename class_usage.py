from budget import SimpleBudget

print("Welcome to the Simple Budget app built with python!")

proceed = False
count = 0
categories = []
print("Please create at least two budgets")
while proceed == False:
    category = input("Please enter a budget category ==>> ")
    categories.append(category)
    balance = int(input(f"Enter an amount for the {category} category ==>> "))
    categories[count] = SimpleBudget(category, balance)
    print(categories[count])
    stop = input("Do you want to enter another category? [Y/N]==>> ")
    if stop == "Y":
        count += 1
        proceed = False
    elif stop == "N":
        proceed = True
    else:
        print("Invalid option selected")

print("[INFO]: Budget successfully created!!!")
print("Your budget list are: ")
for i in range(len(categories)):
    print(categories[i])

print("What operation do you want to perform?")


