# 3. Private (__secret):
'''
A private method in a class is a function that's only intended for internal use by other methods within that same class. 
It's not part of the public interface and can't be called from outside the class. In Python, 
you make a method private by prefixing its name with two underscores (__). This triggers a mechanism called name mangling, 
which makes it difficult to access the method directly from outside the class.
'''

# Example :

class Voter:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        # A private method is called here during initialization
        self.__is_eligible = self.__check_eligibility()

    def __check_eligibility(self):
        print('checking voter eligibility..')
        return self.age >= 18
    
    def cast_vote(self):
        if self.__is_eligible:
            print(f"{self.name} is eligible to vote and can now cast a ballot.")
        else:
            print(f"{self.name} is not eligible to vote.")

voter1 = Voter('Hardik', 24)
voter1.cast_vote()

voter2 = Voter('Aarna', 23)
voter2.cast_vote()

# Trying to call the private method directly will raise an error
try:
    voter1.__check_eligibilitis()
except AttributeError as e:
    print(f"\nError: {e}")