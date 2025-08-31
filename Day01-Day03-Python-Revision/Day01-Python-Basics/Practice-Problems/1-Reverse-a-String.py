# Reverse a String:

'''Question:
Write a function that takes a string as input and returns the reversed version of that string.
Example Input: "hello"
Expected Output: "olleh"
'''

def method_1(rev):
    return rev[::-1]

def method_2(rev2):
    reversed_string = ''
    for characters in rev2:
      reversed_string = characters + reversed_string
    return reversed_string

def method_3(rev3):
   return "".join(reversed(rev3))

user_input = input('Enter String you want to reverse: ')
reversing1 = method_1(user_input)
reversing2 = method_2(user_input)
reversing3 = method_3(user_input)
 
print(f'Original String = {user_input}')
print(f'Reversed String method1 = {reversing1}')
print(f'Reversed String method2 = {reversing2}')
print(f'Reversed String method3 = {reversing3}')