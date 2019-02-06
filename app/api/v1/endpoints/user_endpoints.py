from flask import Blueprint, request ,jsonify ,make_response


""" local imports"""
from app.api.v1.models.user_models import User as UserModel

version_1 = Blueprint("users" ,__name__)

@version_1.route("/api/v1/user/auth/signup", methods=["POST"])

def create_user():
        """ method that creates a user """
        data = request.get_json()
        firstname = data["firstname"]
        lastname = data["lastname"]
        email = data["email"]
        phone_number = data["phone_number"]
        username = data["username"]
        password = data["password"]
        confirmpassword = data["confirmpassword"]

        """Check if any string value is empty"""
        if len(firstname) ==0 or len(lastname) == 0 or len(email) == 0 or len(phone_number) == 0 or len(username) == 0 or len(password) == 0 or len(confirmpassword) == 0 :
            return make_response(jsonify({"status":400,
                                "error":"Field cant be empty"}),400)
        
        """ register user if fields pass"""
        UserModel.create_user(firstname, lastname ,email ,phone_number ,username ,password ,confirmpassword)
        return jsonify({"message":"successful"}), 201

@version_1.route("/api/v1/user/auth/signin", methods=["POST"])
def signIn_user():
    """User sign in method"""
    data = request.get_json()
    username = data["username"]
    password=data["password"]


    """method checks if any key value is empty"""
    if len(username) == 0 or len(password) == 0:
        return make_response(jsonify({"status":400,
                                        "error":"Field cant be empty"}),400)

    """ method checks if key values pair in associated with the username given ,match with the password given"""
    user_value = UserModel.get_a_user_by_username(username)
    if  user_value["password"] == password:
        return make_response(jsonify({"status" : 200 ,
                                        "message":"User logged in successfully"}),200)
    return make_response(jsonify({"status":404,
                                    "error":"Not logged in"}),404)