# Static method: 
'''
    Static methods are just regular functions that happen to be inside a class. 
    They don't need self or cls and don't interact with the object's or class's data.
    They're used for utility functions that are logically grouped with the class.
'''

# Example :
'''
In this example, is_adult is a static method. It takes an age as an argument and returns a boolean. 
It doesn't need to know anything about a specific Person object or the Person class itself to perform its function.
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_adult(age):
        return age >= 18
    
p = Person('Hardik', 24)
print(Person.is_adult(p.age))