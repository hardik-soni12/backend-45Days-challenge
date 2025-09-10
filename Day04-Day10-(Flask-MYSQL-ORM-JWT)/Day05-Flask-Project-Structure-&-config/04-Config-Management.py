'''
#  Config Management : 
- What It Is: Centralized way to manage different settings for development, testing, and production environments.

# Why It Matters: 
    - Security: Keep secrets (API keys, database passwords) separate from code.
    - Environment-Specific: Different database URLs, debug settings for dev vs production.
    - Deployment: Easy to switch configurations without changing code.
'''

# Example Configuration setup: (config.py)


import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'


# Enviroment Variable Example : 

# Set in terminal or .env file
export SECRET_KEY="your-super-secret-key"   #type: ignore
export DATABASE_URL="postgresql://user:pass@localhost/prod_db"      #type: ignore
export FLASK_ENV="production"   #type: ignore



# Use Case: Critical for any Flask app that will be deployed. Keeps sensitive data secure and enables smooth deployment.