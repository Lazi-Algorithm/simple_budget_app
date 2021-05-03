class SimpleBudget:

    def __init__(self, category, balance):
        self.balance = balance
        self.category = category

    def __str__(self):
        return f"A {self.category} budget with N{self.balance}"
    #methods
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def check_balance(self, amount):
        if self.balance < amount:
            return False
        else:
            return True

    def withdraw(self, amount):
        if self.check_balance(amount) == True:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient Funds. Check balance"
        

    def transfer(self, amount, category):
        if self.check_balance(amount) == True:
            self.amount -= amount
            category.balance += amount
            return f"You have successfully transferred N{amount} to {category.category}"
        else:
            return "Insufficient Funds. Check your balance"


    
# obj1 = SimpleBudget("School", 10000)
# obj2 = SimpleBudget("Gorceries", 5000)
# obj3 = SimpleBudget("Transportation", 2000)


# print(f"You have successfully deposited N{amount}. Your new balance is N{self.balance}")

# print(
#     f"You have successfully withdrawn N{amount}. Your new balance is N{self.balance}")
# print(obj1.deposit(300))
# print(obj2.withdraw(400))


