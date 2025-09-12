'''
#  Flask Migrate

- Think of it as Git for your database. When you change your code (like adding a User model), you use Git to track and apply 
that change. Similarly, when you change your database models (like adding an email column to the User model), 
you use Flask-Migrate to safely track and apply that change to your actual database.

- It saves you from ever having to write manual SQL commands like ALTER TABLE
'''

'''
# The Simple 3-Step Workflow

-After a one-time setup, you just repeat these steps whenever you change your models:

    - Change your models in your Python code (e.g., models.py).
    - Generate the migration script with this command:

        flask db migrate -m "Describe your change here"  # This looks at your changes and creates an "update plan".


    - Apply the changes to the database with this command:

        flask db upgrade # This runs the "update plan" and modifies your database.
'''

# That's it. This simple process keeps your database schema perfectly in sync with your models as your application grows.