'''Creating app'''

from flask import Flask,request, make_response, jsonify, json
from flask_jwt_extended import JWTManager
from instance.config import app_config
from datetime import timedelta

"""importing the configurations from the .config file which is in the instance folder"""

from app.api.v1.endpoints.user_endpoints import version_1 as user_v1
from app.api.v1.endpoints.meetup_endpoints import version_1 as meetup_v1
from app.api.v1.endpoints.question_endpoints import version_1 as question_v1


def error_handler(error, message):
    """This function creates a custom dictonary for the error functions"""
    request_data = ""
    if not request.data.decode():
        request_data = "Request body is empty"
    else:
        request_data = json.loads(request.data.decode().replace("'", '"'))

    error_dict = {
        "path_accessed": str(request.path),
        "message": message,
        "request_data": request_data,
        "error": str(error)
    }

    return error_dict


def not_found(error):
    """This function returns a custom JSON response when a resource is not found"""
    message = "The path accessed / resource requested cannot be found, please check"
    error_dict = error_handler(error, message)
    response = make_response(jsonify(error_dict), 404)
    return response


def bad_request(error):
    """This function creates a custom JSON response when a bad request is made"""
    message = "The request made had errors, please check the headers or parameters"
    response = make_response(jsonify(error_handler(error, message)), 400)
    return response


def method_not_allowed(error):
    """This function creates a custom JSON response if the request method is not allowed."""
    message = "The request method used is not allowed"
    return jsonify(error_handler(error, message)), 400


def forbidden(error):
    """Return an error message if the request is forbidden"""
    message = "Sorry, You are not allowed to do that"
    return jsonify(error_handler(error, message)), 403


def unauthorized(error):
    """Unauthorsed access creds"""
    message = "Access denied"
    response = make_response(jsonify(error_handler(error, message)), 401)
    return response

def server_error(error):
    """Internal server error"""
    message = "Name error check your URL"
    response = make_response(jsonify(error_handler(error, message)), 500)
    return response

def create_app(config_name):
    '''creating  the app using the configurations in the dictionary created in the .config file'''
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'super-secret'
    jwt = JWTManager(app)
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=6)

    
    app.register_blueprint(user_v1)
    app.register_blueprint(meetup_v1)
    app.register_blueprint(question_v1)

    app.register_error_handler(400, bad_request)
    app.register_error_handler(401, unauthorized)
    app.register_error_handler(404, not_found)
    app.register_error_handler(405, method_not_allowed)
    app.register_error_handler(403, forbidden)
    app.register_error_handler(500, server_error)

    return app