'''
# Creating Your Own Module & Importing Functions

Purpose: Organize your code in separate files and reuse them easily (just like built-in modules).

Explanation: Make a file, say mymodule.py, define functions there, then import those functions in your main app.

'''

# Example:

# myModule.py
def Greet(name):
    return f'Hello {name}'

# main.py
# from myModule import Greet
print(Greet('Riooo'))