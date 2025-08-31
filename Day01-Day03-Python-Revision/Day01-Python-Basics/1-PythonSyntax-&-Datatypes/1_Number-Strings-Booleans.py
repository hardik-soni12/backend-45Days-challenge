# Python Syntax & Data Types
'''Python syntax means the rules for how code is written—for example, using colons for blocks, 
indentation for code grouping, and using # for comments.'''

'''Data types define what kind of values you can store in variables,
 such as numbers, text, sequences, or mappings.'''

# Numbers, Strings, and Booleans
# 1) Numbers(int, float):
    # int: whole numbers, without a decimal point, like 5, -3, 0.
    # float: numbers with a decimal point, like 3.14, -0.5.

# example: 
age = 24 #int type
height = 5.9 #float type
print(f'Age : {age} \nHeight : {height}')


# 2) Strings(Str):
    # Strings store text inside single, double, or triple quotes:
    #  'hello', "Python", '''long text'''.

# example:
name = 'Hardik' #str type
city = 'Nagpur'
print(f'Name : {name} \nCity : {city}')


# 3) Booleans(bool):
    # Boolean values are just True or False. They answer yes/no or on/off type questions.
    # They are useful for conditions, logic checks, and loops.

is_adult = True if age > 18 else False #bool type
print(f'is_adult : {is_adult}')