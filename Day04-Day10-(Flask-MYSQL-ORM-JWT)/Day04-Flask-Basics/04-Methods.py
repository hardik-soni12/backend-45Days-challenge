'''
# Methods (GET, POST, etc):

- Web routes can respond to different HTTP methods (GET for fetching, POST for sending data):
'''

from flask import Flask, request
app = Flask(__name__)

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()  # gets JSON from the POST body
    return {"sum": data["a"] + data["b"]}

if __name__ == '__main__':
    app.run(debug=True)

'''
# Use POST for things like submitting forms or uploading data.

# Example Use Case:

- Dynamic route: Profile pages, product pages.
- POST method: Sending form data, creating new items in a database.
'''