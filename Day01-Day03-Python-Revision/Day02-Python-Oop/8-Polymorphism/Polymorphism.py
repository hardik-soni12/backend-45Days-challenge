'''
#  Polymorphism : 

Polymorphism means "many forms." In object-oriented programming, it refers to the ability of different objects to 
respond to the same method call in their own, unique ways. It allows you to write code 
that can work with objects of different classes without needing to know their specific type, 
as long as they share a common interface (like a shared method).
'''

'''
# Example: A Drawing Program

Imagine you're building software that can draw different shapes like a Circle, a Rectangle, and a Triangle. 
Each shape needs to be able to "draw" itself on a screen, but the specific steps for drawing each one are different.
'''

class Shape:
    def draw(self):
        raise NotImplementedError('Subclass must implement abstract method.')
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        print(f"Drawing a circle with radius {self.radius}.")
        print("Using a compass to draw the perfect curve.")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        print(f"Drawing a rectangle with width {self.width} and height {self.height}.")
        print("Using a ruler to draw four straight lines.")

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def draw(self):
        print(f"Drawing a triangle with sides {self.side1}, {self.side2}, and {self.side3}.")
        print("Connecting three points with straight lines.")

shapes_to_draw = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5)
]

for shape in shapes_to_draw:
    print("---")
    shape.draw()
