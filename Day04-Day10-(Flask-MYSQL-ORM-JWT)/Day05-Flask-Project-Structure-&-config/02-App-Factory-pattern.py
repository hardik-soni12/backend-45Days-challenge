'''
# App Factory Pattern: 

What It Is: Instead of creating your Flask app globally, create it inside a function called create_app().

# Why Use It:
- Testing: Create multiple app instances with different settings for testing.
- Flexibility: Load different configurations (development, production) dynamically.
- Clean Architecture: Avoid circular imports and global state issues.
'''

# exmaple implementation: (app/__init__.py)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name = 'development'):
    app = Flask(__name__)

    # load configuration
    app.config.from_object(f'config.{config_name.title()}.Config')

    # Initialise extensions
    db.init_app(app)

    # Register blueprints
    from app.routes import main_bp # type: ignore
    app.register_blueprint(main_bp)

    return app

# Use Case: This pattern is essential for any Flask app that will be deployed to production or needs automated testing.