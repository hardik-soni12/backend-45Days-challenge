'''
#  Installing Flask-Jwt-Extended

Install via pip:
'''

pip install flask-jwt-extended      #type: ignore

# This extension provides simple decorators and helpers for issuing and verifying JWTs in Flask apps.



'''
#  Setup with JWTManager

Basic Setup: 
'''
from flask import Flask
from flask_jwt_extended import JWTManager

app =  Flask(__name__)
app.config['JWT_SECURITY_KEY']  = 'my-secret-key'

jwt = JWTManager(app)


# The JWT_SECRET_KEY is used to sign every token; keep it safe.
# JWTManager initializes all the JWT mechanisms—encoding, decoding, request parsing.