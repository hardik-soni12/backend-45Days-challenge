'''
# Hybrid Inheritance : 

Hybrid inheritance is a combination of two or more types of inheritance. 
It's a way to model complex, real-world relationships that don't fit into a single simple inheritance pattern. 
It's often a blend of hierarchical and multiple inheritance.
'''

'''
Example: A University System Reimagined 

Let's expand on our university example. We can have a Person at the top of the hierarchy, and from that, 
two separate specialized roles, Student and Teacher. We can then combine these roles using 
multiple inheritance to create a TeachingAssistant class. This is a perfect example of a hybrid structure.
'''

class Person:
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}.")


class Teacher(Person):
    def __init__(self, subject, **kwargs):
        super().__init__(**kwargs)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")


class Student(Person):
    def __init__(self, major, **kwargs):
        super().__init__(**kwargs)
        self.major = major

    def study(self):
        print(f"{self.name} is studying {self.major}.")


class TeachingAssistant(Student, Teacher):
    def __init__(self, name, major, subject):
        # Call constructors for both parent classes
        super().__init__(name = name, major=major, subject= subject)
        
    def assist(self):
        print(f"{self.name} is assisting with a class.")

# Let's see it in action
ta = TeachingAssistant("Riooo", "Flask", "Python")

# Access methods from all three classes
ta.introduce()  # From Person (hierarchical)
ta.study()      # From Student (multiple)
ta.teach()      # From Teacher (multiple)
ta.assist()     # Unique to TeachingAssistant