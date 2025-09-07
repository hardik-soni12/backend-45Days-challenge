''' Inheritance : Inheritance is a mechanism that allows a new class (a child class or subclass) 
to inherit attributes and methods from an existing class (a parent class or superclass).'''

'''In programming, this means the child class automatically gets all the code from the parent class 
without you having to rewrite it. This promotes code reusability and helps you organize your code logically, 
reflecting real-world hierarchies. We often describe this as an "is-a" relationship'''


# Types of Inheritance in Python
# Python supports five main types of inheritance.

''' 1. Single Inheritance: Single Inheritance is a type of Inheritance where a class Inherits properties 
                        and behaviours from a single parent class. This is the simplest and most common form of Inheritance.'''

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start_engine(self):
        if not self.is_running:
            self.is_running = True
            print(f"The {self.year} {self.make} {self.model}'s engine is now running.")
        else:
            print('The engine is already running!')

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def drive(self):
        if self.is_running:
            print(f'The {self.make} is driving down the road!')
        else:
            print('The engine is off. You need to Start the car first')

    def open_trunk(self):
        print(f'The trunk of the {self.make} is open')

my_car = Car('Honda', 'City', 2026, 4)
print(f"I have a {my_car.year} {my_car.make} {my_car.model} with {my_car.num_doors} doors.")

my_car.start_engine()

my_car.drive()

my_car.open_trunk()