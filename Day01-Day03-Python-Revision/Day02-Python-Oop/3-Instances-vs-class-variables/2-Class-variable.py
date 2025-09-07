# 2. Class Variables

'''
Class variables are shared by all instances of a class. They belong to the class itself, not to any specific object.
Using our car analogy, a class variable would be something like the number of wheels on a car.
Every car created from the blueprint will have four wheels. If you decide to change the blueprint to make
 all cars have six wheels, that change applies to all cars built from that point forward.
'''

'''
Example:
In this example, species is a class variable. Every Dog instance will share the same species value.
'''

class Dog:
    species = 'Bulldog'

    def __init__(self, name):
        self.name = name

d1 = Dog('Jack')
d2 = Dog('Bruno')

print(d1.species)
print(d2.species)

print(Dog.species)