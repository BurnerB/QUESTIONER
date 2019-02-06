'''Creating app'''
import os
from flask import Flask
from app.instance.config import app_config

"""importing the configurations from the .config file which is in the instance folder"""

from api.v1.endpoints.user_endpoints import version_1 as user_v1

def create_app(config_name):
    '''creating  the app using the configurations in the dictionary created in the .config file'''
    app = Flask(__name__)
    app.register_blueprint(user_v1)
    return app