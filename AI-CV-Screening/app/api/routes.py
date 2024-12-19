from flask import Blueprint, jsonify
from app import auth

api_blueprint = Blueprint('api', __name__)

# Dummy data for authentication
users = {
    "username": "password"  # Replace this with your desired username and password
}

# Define the authentication function
@auth.verify_password
def verify_password(username, password):
    if users.get(username) == password:
        return username

@api_blueprint.route('/protected')
@auth.login_required  # This ensures the route is protected by basic auth
def protected():
    return jsonify(message="This is a protected route")

@api_blueprint.route('/public')
def public():
    return jsonify(message="This is a public route")



