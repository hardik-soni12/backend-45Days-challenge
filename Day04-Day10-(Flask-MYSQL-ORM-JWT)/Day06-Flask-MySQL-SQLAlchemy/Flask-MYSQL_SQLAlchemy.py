'''
# MySQL Integration with Flask

- Purpose: To store app data (like users and tasks) in a reliable database that works across many platforms.
'''

# How to Set Up:
# - Ensure MySQL is running and you’ve created a database (e.g., mydb).
#  - Install necessary packages:

pip install flask flask_sqlalchemy pymysql flask-migrate #type: ignore


# Configure Flask to use MySQL:

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/mydb' #type: ignore

# Replace username, password, and mydb with your actual MySQL credentials.


'''
# SQLAlchemy ORM Setup
- What is ORM? Object Relational Mapper lets you use Python classes to represent database tables—no need for raw SQL!

'''

# How to use: 
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

# Now db handles all database interactions using Python code.

'''
# Defining Models:
- What is a Model? It's a Python class used to describe a table's structure—columns, types, and constraints.

'''
# Example: 

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(80), nullable = False, unique = True)

# Every time you add a new field (like age), your database table design changes.


'''
#  CRUD Operations with routes: 
- CRUD: Create, Read, Update, Delete—basic actions for working with data in your app.
'''

# Example: 

# Create a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user = User(name=data['name'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return {"id": user.id}, 201

# Read all users
@app.route('/users')
def get_users():
    users = User.query.all()
    return [{"id": u.id, "name": u.name, "email": u.email} for u in users]

# Update a user
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    db.session.commit()
    return {"message": "Updated"}

# Delete a user
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return {"message": "Deleted"}


# Each route lets your frontend or API clients interact with your data easily.


'''
# Adding Database Migrations with Flask-Migrate

- Why Migrations? When your models change, you need an easy way to update the database schema without losing data.
'''
# Setup in your app:

from flask_migrate import Migrate  # type: ignore
migrate = Migrate(app, db)


# Initialize Migrations Folder

flask db init           #type: ignore


#  Generate Migration Scripts

flask db migrate -m "Initial migration."        #type: ignore



# Apply The Changes

flask db upgrade    #type: ignore



# This allows your team to track and apply database changes safely—even on production servers.