# __init__ Constructor
'''
    # Runs automatically when making an object.
    # Used to set up (initialize) attributes.
'''
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"{self.title} has been checked out.")
        else:
            print(f"{self.title} is already checked out.")

book1 = Book("Whispers from the Grave.", "Tammana Sharma")
print(f"Initial status: {book1.is_checked_out}")
book1.display_info()
book1.check_out()
print(f"New Status: {book1.is_checked_out}")