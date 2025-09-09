'''
# First Flask App
- simple Flask app starts by importing Flask and creating an app instance.
- you define a route (URL) using @app.route("/"). This tells Flask: When someone visits the homepage, run the function below.
- The function returns a JSON response (dictionary), which Flask auto-converts into a valid HTTP response.
- if __name__ == "__main__": lets you run the app directly (good for development).
'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {'message' : 'welcome to Flask Revision'}

if __name__ == '__main__':
    app.run(debug=True) # debug mode helps catch problems 
    
# This structure is the starting template for nearly every Flask web app or REST API you build.