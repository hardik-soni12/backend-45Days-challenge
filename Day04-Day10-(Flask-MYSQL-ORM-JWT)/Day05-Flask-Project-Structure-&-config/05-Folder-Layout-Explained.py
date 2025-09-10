''' # Folder Layout Explained

<|app name|>
├── app/
│   ├── __init__.py          # App factory + extensions
│   ├── routes.py            # Blueprint with routes
│   ├── models.py            # Database models
│   ├── config.py            # Configuration classes
├── run.py                   # Entry point to run app
├── requirements.txt         # Python dependencies
'''

'''
# File Purposes:
    - app/__init__.py: Contains create_app() factory function and initializes extensions.

    - routes.py: All your routes organized in blueprints.

    - models.py: Database table definitions (User, Post, etc.)

    - config.py: Environment-specific settings.

    - run.py: Simple file to start your application.

    - requirements.txt: List of all Python packages needed.

'''

'''
# Professional Benefits:

    - Easy for new team members to understand.

    - Simple to add new features in appropriate files.

    - Follows Flask community standards.

    - Ready for production deployment.

'''
