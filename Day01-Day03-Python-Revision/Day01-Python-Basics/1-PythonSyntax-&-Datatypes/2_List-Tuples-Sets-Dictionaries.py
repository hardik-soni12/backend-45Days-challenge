# Lists : 
    # Ordered, changeable (mutable) collection of items, inside square brackets [ ].
    # Allows duplicate members.
    # Can store different data types.
    # Example: [1, 2, 3, 'a', 'b', 'c']

# Example :
Fruits = ['Mango', 'Banana', 'Strawberry', 'Pineapple', 'Kiwi']
Fruits[0] = 'Avocado' #List can be changed!
print(Fruits)


# Tuples : 
    # Ordered, unchangeable (immutable) collection of items, inside parentheses ( ).
    # Allows duplicate members.
    # Can store different data types.
    # Example: (1, 2, 3, 'a', 'b', 'c')

# Example :
'''cities = ('Pune', 'Mumbai', 'Delhi', 'Nagpur')
cities[2] = 'Nashik' # This will Raise an Error
print(cities)'''


# Sets : 
    # Unordered, unchangeable (immutable), and unindexed collection of items, inside curly braces { }.
    # No duplicate members.
    # Can store different data types.
    # Example: {1, 2, 3, 'a', 'b', 'c'}

# Example :
numbers = {2, 2, 3, 4, 6, 6}
numbers.add(5)
print(numbers)


# Dictionaries :
    # Unordered, changeable (mutable), inside curly braces { }.
    # No duplicate members.
    # Can store different data types.
    # Example: {'name': 'Hardik', 'age': 24, 'city': 'Nagpur'}

# Example :
person = {'name': 'Hardik', 'age': 23, 'city': 'Nagpur'}
person['age'] += 1 # Dictionary can be changed!
print(person)