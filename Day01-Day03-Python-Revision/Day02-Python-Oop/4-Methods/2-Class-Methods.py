# Class Methods :
'''
    Class methods are functions that do something with the class itself, not a specific object. 
    They always take cls (the class) as their first argument and are used for actions that affect the entire class, 
    like creating an object in a unique way.
'''

# Example :

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_string(cls, book_string):
        """Creates a Book instance from a string like "Title by Author"."""
        title, author = book_string.split(" by ")
        return cls(title, author)

# Standard way to create a Book
book1 = Book("The Hitchhiker's Guide", "Douglas Adams")

# Using the class method 
book_data = "To Kill a Mockingbird by Harper Lee"
book2 = Book.from_string(book_data)

print(book2.title)  
print(book2.author)