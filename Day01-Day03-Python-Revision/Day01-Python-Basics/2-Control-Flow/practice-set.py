print('\nPRACTICE SET:')
print('-----------------')

''' 1) Write an if-elif-else block that prints “Morning”, “Afternoon”, or “Evening” based on a time
 variable (e.g., time = 14).'''

time = int(input('Enter the time: '))
if time < 12:
    print("It's Morning")
elif time < 18:
    print("It's Afternoon")
else:
    print("It's Evening")
print('-----------------')



''' 2) Print each letter of the word "PYTHON" using a for loop.'''

word = "PYTHON"

for letters in word:
    print(letters)
print('-----------------')



''' 3) Use a while loop to print numbers from 1 to 4.'''

n = 1
while n <= 4:
    print(n, end=' ')
    n += 1
print('\n-----------------')



''' 4) Make a loop that stops printing numbers at 7 using break.'''

for i in range(1,10):
    if i == 7:
        break
    print(i)
print('-----------------')



''' 5) Make a loop that prints numbers from 1 to 5 but skips 2 using continue.'''

for i in range(1,6):
    if i == 2:
        continue
    print(i, end=' ')