# Reading and Writing Files

'''
#  Read: Use .read() to get the file’s contents.

#  Write: Use .write() to put new content in the file.

#  Don’t forget to .close() when you’re done!
'''

# file reading example:

file = open(r'D:\backend-45Days-challenge\Day01-Day03-Python-Revision\Day01-Python-Basics\4-Basic-File-Handling\test.txt','r')
content = file.read()
print(content)
file.close()



# file writing example: 

w_file = open(r'D:\backend-45Days-challenge\Day01-Day03-Python-Revision\Day01-Python-Basics\4-Basic-File-Handling\test.txt','w')
w_file.write("hello World!\n")
w_file.write("Hey i've Updated this File.")
w_file.close()