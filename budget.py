class SimpleBudget:

    def __init__(self, category, balance):
        self.balance = balance
        self.category = category

    def __str__(self):
        return f"A {self.category} budget with N{self.balance}"
    #methods
    def deposit(self, amount):
        self.balance += amount
        print(f"You have successfully deposited N{amount}. Your new balance is N{self.balance}")
        return self.balance

    def check_balance(self, amount):
        if self.balance < amount:
            return False
        else:
            return True

    def withdraw(self, amount):
        if self.check_balance(amount) == True:
            self.balance -= amount
            print(f"You have successfully withdrawn N{amount}. Your new balance is N{self.balance}")
            return self.balance
        else:
            return "Insufficient Funds. Check balance"
        

    def transfer(self, amount, category):
        if self.check_balance(amount) == True:
            self.balance -= amount
            category.balance += amount
            return f"You have successfully transferred N{amount} to {category.category}"
        else:
            return "Insufficient Funds. Check your balance"


    

