'''
# Installing and using External modules with pip

Purpose: Add extra power to your code using tools made by others (e.g., Flask, requests).

Explanation:

Use pip install <module> in terminal to add new modules.

Import and use them just like built-in ones.
'''

import requests
response = requests.get('https://google.com')
print(response.status_code)