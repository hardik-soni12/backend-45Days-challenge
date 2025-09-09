'''
# Returning JSON responses:

- Flask turns dictionaries you return into JSON automatically.
- If you want more control (set HTTP status, headers): Use jsonify().
'''

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/custom')
def custom_response():
    return jsonify({"status" : "Ok", "msg" : "Custom JSON!"})

if __name__ == '__main__':
    app.run(debug=True)