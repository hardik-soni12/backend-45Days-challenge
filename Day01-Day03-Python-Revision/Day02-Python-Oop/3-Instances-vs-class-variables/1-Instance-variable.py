# 1. Instance Variables

'''
Instance variables, often called object attributes, are unique to each object (or instance) of a class.
Think of a class like a blueprint for a car. Each car built from that blueprint is a separate instance.
The color of the car is an instance variable. One car might be red, another blue, and a third black.
Changing the color of one car doesn't affect the color of the others. They are independent.
'''

'''
Example:
In the example below, name and age are instance variables. Each Person object will have its own unique name and age.
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
p1 = Person('Hardik', 24)
p2 = Person('Aarna', 23)

print(p1.name)
print(p2.name)