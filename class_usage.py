import time
from budget import SimpleBudget as Sb


obj1 = Sb("Food", 10000)
obj2 = Sb("Entertainement", 5000)
obj3 = Sb("Clothing", 2000)


print(f"Depositing on {obj1.category} budget")
time.sleep(1)
print(obj1.deposit(300))

time.sleep(1)
print(f"Withdrawing from {obj2.category} budget")
time.sleep(1)
print(obj2.withdraw(400))

time.sleep(1)
print(f"Checking balance of {obj3.category} budget")
time.sleep(1)
print(obj3.balance)

time.sleep(1)
print(f"Transferring from {obj1.category} to {obj2.category}")
time.sleep(1)
print(obj1.transfer(3000, obj2))
time.sleep(1)
print(f"{obj1.category} New balance == {obj1.balance}")
print(f"{obj2.category} New balance == {obj2.balance}")
