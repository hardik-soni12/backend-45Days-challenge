'''
# Custom Exceptions (raise, defining classes):

Purpose: Make errors specific for your project (e.g., "NotEnoughBalance" for bank app), 
so you control what kinds of mistakes can happen

# Explanation: 
1. Define a new class inheriting from Exception.
2. Use raise to trigger your custom exception when needed.
'''

class NotEnoughBalance(Exception):
    pass

balance = 15000
print(f"\nCurrent Balance: ₹{balance}\n")
try:
    withdraw = int(input('Enter Amount to Withdraw: '))
except ValueError:
    print('Enter a Numeric Amount!')
else:
    try:
        if withdraw > balance:
            raise NotEnoughBalance('Not Enoungh Balance in you Account!\n')
    except Exception as e:
            print(e)
    else:
        print(f"you've Successfully withdrawed ₹{withdraw}\n")
        print(f'Balance : ₹{balance-withdraw}\n')