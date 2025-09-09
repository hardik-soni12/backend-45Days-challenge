'''
# Routes + Methods

- Routes connect URLs to functions.
- The @app.route() decorator tells Flask “If someone visits this URL, run this function”.
'''

# Dynamic Route example: 

from flask import Flask

app = Flask(__name__)

@app.route('/greet/<name>', methods = ['GET'])
def greet(name):
    return {'message': f'hello {name}'} #Visiting /greet/riooo returns {"message": "Hello, riooo!"}.

if __name__ == '__main__':
    app.run(debug=True)