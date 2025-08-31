# Context Manager (with Statement):
'''
# The with statement is the recommended way to handle files.
It's a special construct called a context manager that ensures resources are properly handled.

    # Automatic Cleanup: The with statement automatically calls the file's .close() 
      method for you when the block of code is finished, even if an error occurs.

    # Safer Code: This prevents common bugs like files being left open,
     which can lead to memory leaks or data corruption.
'''

with open(r'D:\backend-45Days-challenge\Day01-Day03-Python-Revision\Day01-Python-Basics\4-Basic-File-Handling\with-method.txt', 'w') as file:
    file.write('Writing file using with statement.')


with open(r'D:\backend-45Days-challenge\Day01-Day03-Python-Revision\Day01-Python-Basics\4-Basic-File-Handling\with-method.txt', 'r') as file:
    content = file.read()
    print(content)