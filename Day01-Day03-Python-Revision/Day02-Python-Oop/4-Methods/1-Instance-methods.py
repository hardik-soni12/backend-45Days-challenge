# Instance Methods: 
'''
    ~Instance methods are functions that do something with an object's specific data. 
    They always take 'self' as their first argument to access the unique variables of that object.
'''

# Example:
'''In this example, get_info is an instance method. It uses self to access the unique name and age of each Person object.'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self): #This is an Instance Method
        return f'Person Name : {self.name}\nPerson age : {self.age}'
    
p1 = Person('Hardik', 24)
print(p1.get_info())
print(p1.name)
print(p1.age)