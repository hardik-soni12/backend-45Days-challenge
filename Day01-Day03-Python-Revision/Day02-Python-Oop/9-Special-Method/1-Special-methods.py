'''
Special methods are methods with a double-underscore prefix and suffix (e.g., __init__, __str__). 
They allow you to define how your objects behave with operators like + or ==, with built-in functions 
 len(), and with specific syntax like obj(). 
They give your objects a consistent, intuitive interface.
'''

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # 1. __str__(): A user-friendly string representation
    def __str__(self):
        return f"'{self.title}' by {self.author}"

    # 2. __repr__(): The official representation for developers
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"

    # 3. __len__(): Define the behavior for the built-in len() function
    def __len__(self):
        return self.pages

    # 4. __add__(): Enable the '+' operator to add two books
    def __add__(self, other):
        # We can't add two books in the real world, but we can combine their page counts
        total_pages = self.pages + other.pages
        return total_pages
    
    # 5. __eq__(): Enable the '==' operator to check for equality
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

# Let's create some Book objects
book1 = Book("Python Crash Course", "Eric Matthes", 544)
book2 = Book("Automate the Boring Stuff", "Al Sweigart", 504)
book3 = Book("Python Crash Course", "Eric Matthes", 544)

# Use the special methods indirectly

# __str__ and __repr__
print(f"User-friendly string: {book1}") # Calls __str__
print(f"Developer representation: {repr(book1)}") # Calls __repr__

# __len__
print(f"\nNumber of pages in book1: {len(book1)}")

# __add__
total_pages = book1 + book2 # Calls book1.__add__(book2)
print(f"Total pages in book1 and book2: {total_pages}")

# __eq__
print(f"\nAre book1 and book2 the same? {book1 == book2}") # Calls book1.__eq__(book2)
print(f"Are book1 and book3 the same? {book1 == book3}")