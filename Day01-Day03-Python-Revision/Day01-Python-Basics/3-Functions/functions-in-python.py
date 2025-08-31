# Functions in Python
'''A function is a block of code that runs only when called. 
Functions let you reuse code and make large programs easier to manage.'''



def greet():
    print('\nhello!')
greet()
print('--------------')


# Default Arguments
'''You can give function parameters default values. 
If a value isn’t provided, the default is used.'''

def greet(name='Hardik'):
    print(f'Hello, {name}')
greet()
greet('Riooo')
print('--------------')


# *args (Variable Positional Arguments)
'''You can pass any number of arguments to a function. 
The *args parameter collects extra arguments into a tuple.'''

def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

result1 = add(2,4,6,8)
result2 = add(3,6)

print(f"Result1: {result1}")
print(f"Result2: {result2}")
print('--------------')



# **kwargs (Variable Keyword Arguments)
# **kwargs lets a function accept any number of keyword arguments; inside, kwargs is a dictionary.

def create_profile(username, **user_info):
    print(f'creating profiles for : {username}')
    for key, value in user_info.items():
        print(f'- {key} : {value}')

create_profile('Hardik', age=24, city='Nagpur')
print('-------------')
create_profile('Riooo', age=24, city='Nagpur', salary=85000)
print('-------------')



# Return Values
# Functions can send a value back using return. If there’s no return, the function returns None by default.

def multiply(a,b):
    result = a * b
    return result

product = multiply(23,22)
print(f'Multiplication : {product}')
print('-------------')


# Scope: Local vs Global
    # Local variables: Defined inside a function, used only there.

def my_function():
    x = 10  # Local variable
    print(f'Local Variable : {x}')

my_function()
print('-------------')

    # Global variables: Defined outside all functions, accessible everywhere.

y = 50

def glob_func():
    print(f'Global Variable : {y}')
glob_func()
print('-------------')
