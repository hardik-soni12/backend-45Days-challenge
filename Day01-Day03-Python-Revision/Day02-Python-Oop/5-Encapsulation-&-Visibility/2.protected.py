# 2. protected(_age);
'''
Protected attributes are meant for internal use by the class and its subclasses. 
You declare them with a single leading underscore (_). Python doesn't strictly enforce this, 
so you can still access it from the outside, but it's a convention that says,
"Hey, this is for internal use. Don't mess with it unless you know what you're doing."
'''

# Example :

class Car:
    def __init__(self, fuel_level):
        self._fuel_level = fuel_level

    def _is_fuel_sufficient(self):
        return self._fuel_level > 0
    
    def start_engine(self):
        if self._is_fuel_sufficient():
            print('Engine Started Successfully!')
        else:
            print('Cannot Start Engine. Please Add fuel!')

my_car = Car(fuel_level=5)
my_car.start_engine() # Called Public method

# This is discouraged but possible:
# print(my_car._is_fuel_sufficient())