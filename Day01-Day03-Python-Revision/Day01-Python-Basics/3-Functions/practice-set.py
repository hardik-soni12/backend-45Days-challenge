''' 1)Write a function greet that takes an 
optional name and greets the person (default: "Guest").'''

def greet(name='Guest'):
    print(f'Hello, Mr.{name}')

greet('Hardik')
print('------------')



''' 2) Write a function to sum any number of given numbers using *args.'''

def Add(*add):
    sum = 0
    for num in add:
        sum += num
    return sum
result = Add(2,6)
print(f'The Sum of Result is {result}')
print('-----------')



''' 3) Write a function that prints all key-value pairs given to it using **kwargs.'''

def Student(name, **info):
    print(f'Data of Student Name : {name}')
    for key, value in info.items():
        print(f'{key} : {value}')

Student('Hardik', id=23, Age=24, city='Nagpur')
print('-----------')



''' 4) Write a function that multiplies two numbers and returns the result.'''

def multiply(a,b):
    mul = a * b
    return mul
print(f'Multiplication of 2 x 5 = {multiply(2,5)}')
print('----------')