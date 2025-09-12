'''
#  Understanding the One-to-Many Relationship: 

- In database design, a one-to-many relationship is a fundamental concept. It means that one record in a particular table 
(the "one" side) can be associated with multiple records in another table (the "many" side). 
However, each record on the "many" side can only be linked to a single record on the "one" side.

        - Example: One User can write many Posts, but each Post is written by exactly one User. The User is the "one" (the parent), 
        and the Post is the "many" (the child).

SQLAlchemy uses two key components to create this link: db.ForeignKey and db.relationship.
'''


'''
#  The "Many" Side: Post Model and db.ForeignKey

    - The db.ForeignKey is the database-level instruction. It tells the actual SQL database how to link the tables together.
'''
'''

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    # This is the crucial line for the database link
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)'''



'''
# The "One" Side: User Model and db.relationship

    - The db.relationship is the SQLAlchemy ORM-level instruction. It doesn't create any columns in the database. 
    Instead, it provides a powerful, Pythonic way to navigate between the linked objects in your code.
'''
'''


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    # This is the crucial line for Python-level access
    posts = db.relationship('Post', backref='author', lazy=True)'''


# In simple terms: The relationship is a dynamic helper that lets you effortlessly navigate the link created by the ForeignKey, 
# making your Python code clean and intuitive.

