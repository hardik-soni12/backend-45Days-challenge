'''
# Hierarchical Inheritance: 

Hierarchical inheritance is when multiple child classes inherit from a single parent class. 
This is perfect for situations where you have a general, shared concept with several different, 
specialized variations. Think of it like a parent class acting as a blueprint for multiple distinct child classes. 
Each child class is unique but shares the common foundation provided by the parent. 
The key relationship is that a Manager is an Employee and a Developer is also an Employee.
'''

# Example: A University System

'''
Imagine a university with different types of people: students, professors, and administrative staff. 
They are all considered a Person in the university's system and share common attributes like a name and an ID. 
However, they each have unique characteristics and behaviors. Hierarchical inheritance is the perfect way to model this.
'''

# parent class : person
class Person:
    def __init__(self, name, person_id):
        self.name = name
        self.person_id = person_id

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.person_id}")

# Child Class 1: Student
class Student(Person):
    def __init__(self, name, person_id, major):
        super().__init__(name, person_id)
        self.major = major

    def enroll(self, course):
        print(f"{self.name} is enrolling in {course}.")

# Child Class 2: Professor
class Professor(Person):
    def __init__(self, name, person_id, department):
        super().__init__(name, person_id)
        self.department = department

    def teach(self, subject):
        print(f"{self.name} is teaching {subject}.")


student1 = Student("Hardik", "S-101", "Computer Science")
professor1 = Professor("Dr. Smith", "P-202", "DBMS")

print("--- Student Info ---")
student1.display_info()  # Inherited from Person
student1.enroll("Intro to Python") # Unique to Student

print("\n--- Professor Info ---")
professor1.display_info() # Inherited from Person
professor1.teach("Quantum Mechanics") # Unique to Professor