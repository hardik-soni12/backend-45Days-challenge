# The open() Function
'''
The open() function is used to open a file and return a file object. 
which is then used to perform read or write operations.
It's Basic Syntax is:
    open(filename, mode)

    # filename = The name of the file you want to open.
    # mode = A string that specifies the purpose for which the file is opened.

# File Modes:
Understanding the mode is crucial because they dictate what you can and cannot do with the file.

    # Read mode('r')
        - Purpose: To read the contents of a file.
        - Behavior: The file must already exist. If it doesn't, Python will raise a FileNotFoundError.
                    The file pointer is placed at the beginning of the file.

    # Write Mode ("w") 
        - Purpose: To write data to a file.
        - Behavior: If the file does not exist, Python will create a new, empty file for you.
                    If the file already exists, it will be erased completely,
                    and you will start with an empty file.

    # Append Mode ("a")
        - Purpose: To add new data to the end of a file.
        - Behavior: If the file does not exist, Python will create a new, empty file.
                    If the file already exists, the new content is added to the end of the existing content
                    without erasing anything. The file pointer is placed at the end of the file.


Important Note: Closing Files

    - It's a best practice to always close a file after you are done with it using the close() method.
     This frees up system resources and ensures all changes are saved.
    
'''

# Correct Way to Handle Files:

file = open(r'D:\backend-45Days-challenge\Day01-Day03-Python-Revision\Day01-Python-Basics\4-Basic-File-Handling\test.txt', 'w')
file.write('Hello, world!!')
file.close()
