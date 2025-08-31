# For Loop :
    # Used to iterate over a sequence (like a list, tuple, string, or range) or other iterable objects.
    # Syntax: for item in sequence:
    
# Example 1) :
n = 1
for i in range(5):
    print(f'secs = {n + i}')
print('----------------')

# Example 2) :
Alphabets = ['R', 'i', 'o', 'o', 'o']
for Alphabet in Alphabets:
    print(f'{Alphabet}', end='')
print('\n----------------')


# While loop : 
    # Repeats a Block of code as long as a condition is true.

# Example 1) :
n = 1
while n <= 5:
    print(f'count = {n}')
    n += 1
print('----------------')

# Example 2) :
password = ''
while password != 'password123':
    password = input('Enter the password: ')
print('Access granted!')
print('----------------')


# Break and Continue: 
    # break:  Immediately exits the loop (for or while), even if the condition hasn’t finished.
    # continue: Skips the current iteration and moves to the next.

# Example 1) of Break :

names = ['Rahul', 'Rohit', 'Rakesh', 'Hardik', 'riooo', 'supriya']
search_name = input('Enter the name to search: ')
for name in names:
    if name == search_name:
        print(f'Name {search_name} found!')
        break
    
    print(f'Searching {name}...')
print('----------------')


# Example 2) of Break :

while True:
    command = input('Enter a command (exit to quit): ')
    if command == 'exit':
        break
    print(f'You entered: {command}')
print('----------------')


# Example 1) of Continue :

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number % 2 == 1:
        continue
    print(f'Even numbers: {number}')
print('----------------')


# Example 2) of Continue :

data = ["valid1", "", "valid2", "invalid_data", "valid3"]
for item in data:
    if item == "" or "invalid" in item:
        continue
    print(f'Valid data: {item}')
print('----------------')