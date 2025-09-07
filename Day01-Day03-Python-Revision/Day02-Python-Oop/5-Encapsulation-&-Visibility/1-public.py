# Encapsulation and Visibility :

'''
Encapsulation in Python is about bundling data and methods that operate on that data into a single unit (a class). 
Visibility controls how accessible that data is from outside the class.
'''

# 1.Public (name):
# Public attributes are accessible from anywhere.(Accessible anywhere)

class BankAccount:
    def __init__(self, initial_balance):
        self._balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance = self._balance + amount
            print(f"Deposited ₹{amount}. New Balance : ₹{self._balance}")
        else:
            print('Deposit Amount should be Positive.')

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance = self._balance - amount
            print(f'Withdrawal ₹{amount}. New Balance : ₹{self._balance}')

    def get_balance(self):
        return self._balance

myAccount = BankAccount(10000)
myAccount.withdraw(3000)
myAccount.deposit(10000)
print(myAccount.get_balance())