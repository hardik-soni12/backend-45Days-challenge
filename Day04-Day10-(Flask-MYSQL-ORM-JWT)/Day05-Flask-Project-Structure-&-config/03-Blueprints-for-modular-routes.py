'''
# Bluepints for Modular routes:
- What Are Blueprints: Think of blueprints as mini-applications that organize related routes, templates, and static files together.

# Why Use Them: 
    - Organization: Group related functionality (user management, blog posts, API endpoints).
    - Reusability: Use the same blueprint across multiple projects.
    - Team Development: Different developers work on different blueprints independently.
'''

# Example Implementation:(app/routes.py)

from flask import Blueprint, render_template, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html')

@main_bp.route('/api/users')
def get_users():
    return jsonify({'users': ['Alice', 'Bob', 'Charlie']})


# Registration in Factory:

# In create_app function
from app.routes import main_bp #type: ignore
app.register_blueprint(main_bp) #type: ignore


# Use Case: Essential for any Flask app with more than 5-6 routes. Makes code modular and maintainable.