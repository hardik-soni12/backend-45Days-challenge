'''
#  Foreign keys in SQLAlchemy

- In SQLAlchemy, a foreign key is the fundamental database-level constraint that creates and enforces a link between two tables. 
It's a column (or set of columns) in a child table that directly refers to the primary key of a parent table, 
ensuring that every child record is associated with a valid parent.
'''

'''
#  The Core Concept: A Digital Link

- Think of a foreign key as an official address. Imagine you have a table of Users (the "parent") and a table of Posts (the "child"). 
Each Post needs to know who wrote it. The foreign key is like writing the User's unique ID number directly onto the Post record.

- This creates a concrete link that the database itself understands and enforces. It's not just a convention; it's a strict rule.
'''

'''
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    # ... other columns ...
    
    # This line defines the foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
'''

'''
#  The Key Benefits: Why It's Essential

    - 1) Enforces Relational Integrity: This is the most important benefit. The database will now actively prevent data corruption. 
    For example, if you try to create a Post and set its user_id to 99, but no user with id=99 exists in the user table, 
    the database will raise an error and reject the transaction. This guarantees that every link is valid.

    - 2) Prevents Orphan Data: Because of the integrity enforcement and the nullable=False constraint, you can never have a Post 
    record that "floats" in the database without an author. Every child record is guaranteed to have a parent, 
    preventing inconsistent or meaningless data.

    - 3) Enables Powerful Database Features: Foreign keys allow the database to perform cascading actions. For example, 
    you can configure the foreign key so that if a User is deleted, the database will automatically delete all of their associated 
    Posts (ondelete='CASCADE'). This helps maintain a clean and consistent database state automatically.
'''