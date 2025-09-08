'''
#  Virtual Environments (python -m venv)

Purpose: Keeps project dependencies separate so nothing breaks when you use different modules in multiple projects.

Explanation:

Create a new Python environment: python -m venv venv

Activate it:
On Windows: venv\Scripts\activate

Use pip freeze > requirements.txt to save all dependencies.
'''

# example :
'''
python -m venv venv      # Creates a new environment
venv\Scripts\activate    # Windows activation
pip install flask
pip freeze > requirements.txt
'''