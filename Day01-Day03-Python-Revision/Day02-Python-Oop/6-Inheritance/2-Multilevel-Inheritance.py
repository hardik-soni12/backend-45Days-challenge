'''
# Multilevel Inheritance: 

Multilevel inheritance is a type of inheritance where a class inherits from a parent class, 
and then another class inherits from that child class. This creates a chain of inheritance, 
like a family tree going from a grandparent to a parent to a child. The final child class in 
the chain gets all the attributes and methods from every class above it. 
This is a powerful way to add features incrementally, building upon existing classes without modifying them
'''

'''
# Multilevel Inheritance Example: Company Hierarchy 

Imagine a company with a basic Employee class. Then, you have a Developer class that builds on 
Employee by adding specific development skills. 
Finally, you have a SeniorDeveloper class that adds advanced skills and leadership qualities.
'''

class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def get_details(self):
        return f'Name: {self.name}\nEmployee ID: {self.employee_id}'

class Developer(Employee):
    def __init__(self, name, employee_id, programming_language):
        super().__init__(name, employee_id)
        self.programming_language = programming_language

    def write_code(self):
        print(f'{self.name} is writting code in {self.programming_language}')

class SeniorDeveloper(Developer):
    def __init__(self, name, employee_id, programming_language, team_lead):
        super().__init__(name, employee_id, programming_language)
        self.team_lead = team_lead

    def mentor(self):
        print(f'{self.name} is mentoring junior developers.')


senior_dev = SeniorDeveloper('Hardik', 232225, 'Python', 'Backend Team'  )

print('Senior Developer Details: ')
print(f"Details: {senior_dev.get_details()}")
print(f"Language: {senior_dev.programming_language}")
print(f"Team Lead: {senior_dev.team_lead}")

senior_dev.write_code() # Inherited from Developer
senior_dev.mentor()      # Unique to SeniorDeveloper