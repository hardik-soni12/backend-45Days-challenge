# if/elif/else : 
    # if : checks if a condition is True, if yes, then runs the block of code.
    # elif(else-if) : Checks another condition, only if the previous if (or elif) was false.
    # else : Runs the block of code if none of the above conditions are true.

# Example : 
age = int(input('Enter your age: '))
if age > 18:
    print('You are an adult')
elif age == 18:
    print('You are just an adult')
else:
    print('You are a child')
