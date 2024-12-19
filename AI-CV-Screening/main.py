from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# Dummy data for authentication
users = {
    "username": "password"  # Replace this with your desired username and password
}

# Define the authentication function
@auth.verify_password
def verify_password(username, password):
    if users.get(username) == password:
        return username

@app.route('/protected')
@auth.login_required  # This ensures the route is protected by basic auth
def protected():
    return jsonify(message="This is a protected route")

@app.route('/public')
def public():
    return jsonify(message="This is a public route")

if __name__ == '__main__':
    app.run(debug=True)
