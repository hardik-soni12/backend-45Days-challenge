'''
# Error Handling : 
(try / except / else / finally)

Purpose: Helps deal with unexpected errors gracefully so programs don't 
crash and you can control what happens if things go wrong.
'''

# try : Write code here that might cause an Error.

# except : Run this if somethong goes wrong in the try block.

# else : Run this only if no errors occurs.

# finally : Runs no matter what - for clean-up (like closing files even if an error occurs).

try: 
    Number = int(input("Enter a Number: "))
    result = 100/Number
except ValueError:
    print('You must Enter a Number.!')
except ZeroDivisionError:
    print('Cannot Divide by Zero!!')
else:
    print(f'Division Successful : {result}')
finally:
    print('Thanks for trying this division.')

