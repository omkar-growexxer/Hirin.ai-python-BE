from flask import Blueprint, jsonify
from app import auth
from app.utils.config_loader import Config

api_blueprint = Blueprint('api', __name__)

username = Config.get('Auth','username')
password = Config.get('Auth','password')

# Dummy data for authentication
users = {
    username : password  
}

# Define the authentication function
@auth.verify_password
def verify_password(username, password):
    if users.get(username) == password:
        return username

@api_blueprint.route('/protected')
@auth.login_required
def protected():
    return jsonify(message="This is a protected route")

@api_blueprint.route('/public')
def public():
    return jsonify(message="This is a public route")



