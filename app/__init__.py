'''Creating app'''

from flask import Flask
from flask_jwt_extended import JWTManager
from instance.config import app_config
from datetime import timedelta

"""importing the configurations from the .config file which is in the instance folder"""

from app.api.v1.endpoints.user_endpoints import version_1 as user_v1
from app.api.v1.endpoints.meetup_endpoints import version_1 as meetup_v1

def create_app(config_name):
    '''creating  the app using the configurations in the dictionary created in the .config file'''
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'super-secret'
    jwt = JWTManager(app)
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=6)

    
    app.register_blueprint(user_v1)
    app.register_blueprint(meetup_v1)
    return app