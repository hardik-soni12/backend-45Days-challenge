print('\n-------------\nPractice Set\n-------------')

''' 1) Create a file "myfile.txt" and write "This is my first file!" to it.'''

my_file = r'D:\backend-45Days-challenge\Day01-Day03-Python-Revision\Day01-Python-Basics\4-Basic-File-Handling\practice-set.txt'

file = open(my_file, 'w')
file.write('This is my Practice set file!')
file.close()



''' 2) Open "myfile.txt" and read its contents—print them.'''

file = open(my_file, 'r')
content = file.read()
print(f'\n{content}')
file.close()
print('------------')



''' 3) Using with, write "Python makes file handling easy!" to "myfile.txt".'''

my_file2 = r'D:\backend-45Days-challenge\Day01-Day03-Python-Revision\Day01-Python-Basics\4-Basic-File-Handling\myFile.txt'

with open(my_file2, 'w') as file:
    file.write('Python makes file handling easy!')



''' 4) Open "myfile.txt" in read mode, using with, and print only the first 12 characters.'''

with open(my_file2, 'r') as file:
    content = file.read(12)
    print(f'First 10 characters of the File : {content}')
    print('------------')
    