from flask import Flask
from flask_httpauth import HTTPBasicAuth
from flask_swagger_ui import get_swaggerui_blueprint
import os

# Initialize the basic auth
auth = HTTPBasicAuth()

# Initialize the Swagger UI
SWAGGER_URL = '/swagger'
API_URL = os.path.join('/static', 'swagger.json')  # The path to the Swagger file
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={'app_name': "Flask API with Basic Auth"}
)

def create_app():
    app = Flask(__name__)

    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    from app.api.routes import api_blueprint
    app.register_blueprint(api_blueprint)

    return app




