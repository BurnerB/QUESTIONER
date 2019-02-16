from flask import Flask, Blueprint, request ,jsonify ,make_response
import datetime
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash


""" local imports"""
from app.api.v1.models.user_models import User
from app.api.v1.utils.validators import Validators
from instance.config import Config

Validate = Validators()


version_1 = Blueprint("users" ,__name__)

@version_1.route("/api/v1/user/auth/signup", methods=["POST"])

def create_user():
        """ method that creates a user /user sign up"""
        try:
                data = request.get_json()
                firstname = data["firstname"]
                lastname = data["lastname"]
                email = data["email"]
                phone_number = data["phone_number"]
                username = data["username"]
                password = data["password"]
                confirmpassword = data["confirmpassword"]
        
                """checks if any key missing"""
        except Exception as e:
                return jsonify({"status":400,
                        "error" :"Invalid {} key field".format(e)
                                }),400
        
        """Check if firstname is valid"""
        if not Validate.check_names(firstname):
                return jsonify({"status":400,
                        "error" :"Invalid firstname field"
                        }),400
        
        """Check if lastname is valid"""
        if not Validate.check_names(lastname):
                return jsonify({"status":400,
                        "error" :"Invalid lastname field"
                        }),400
        
        """Check if email format is valid"""
        if not Validate.valid_email(email):
                return jsonify({"status":400,
                        "error" :"Invalid Email field"
                        }),400
        
        """Check if phone_number format is valid"""
        if not Validate.valid_phone_number(phone_number):
                return jsonify({"status":400,
                                "error" :"Invalid phone_number"
                                }),400
        
        """Check if username format is valid"""
        if not Validate.valid_username(username):
                return jsonify({"status":400,
                        "error" :"Invalid username field"
                        }),400
        
        """Check if password format is valid"""
        if not Validate.valid_password(password):
                return jsonify({"status":400,
                        "error" :"Invalid password field"
                        }),400  
        
        """ Checks if email already used to register """
        if Validate.check_email_exists(email):
                return jsonify({"Error":"The email already exists for an account,log in"}),400
        
        """ Checks if username already used to register """
        if Validate.check_username_exists(username):
                return jsonify({"Error":"The username already exists for an account,log in"}),400
                
        
        """Check if any string value is empty"""
        if len(firstname) ==0 or len(lastname) == 0 or len(email) == 0 or len(phone_number) == 0 or len(username) == 0 or len(password) == 0 or len(confirmpassword) == 0 :
            return make_response(jsonify({"status":400,
                                "error":"Field cant be empty"}),400)
        
        """Check if password matches with confirm password"""
        if password == confirmpassword:
                """ register user if fields pass"""
                password = generate_password_hash(data["password"])
                confirmpassword = generate_password_hash(data["confirmpassword"])
                data = User.create_user(firstname, lastname, email ,phone_number ,username ,password ,confirmpassword)
                return jsonify({"message":"successful regisration"}), 201
        else:
                return jsonify({"error": "Passwords don't match"}), 400

@version_1.route("/api/v1/user/auth/signin", methods=["POST"])
def signIn_user():
        """User sign in method/user log in"""
        try:
                data = request.get_json()
                username = data["username"]
                password = data["password"]
        
                """checks if any key missing """
        except Exception as e:
                return jsonify({"status":400,
                        "error" :"Invalid {} key field".format(e)
                                }),400

        """method checks if any key value is empty"""
        if len(username) == 0 or len(password) == 0:
                return make_response(jsonify({"status":400,
                                        "error":"Field cant be empty"}),400)
        
        """Check if username format is valid"""
        if not Validate.valid_username(username):
                return jsonify({"status":400,
                        "error" :"Invalid username field"
                        }),400
        
        """ Checks if username exists"""
        if not Validate.check_username_exists(username):
                return jsonify({"status":404,
                                "error" :"Username does not exist"
                                }),404


        """ create token"""
        # public_id = user_value[0]['public_id']
        access_token = create_access_token(identity = username)

        
        """ method checks if key values pair in associated with the username given ,match with the password given"""
        user_value = User.get_a_user_by_username(username)
        if check_password_hash(user_value[0]["password"], password):
                return make_response(jsonify({"status" : 200 ,
                                              "message":"User logged in successfully",
                                              "access_token": access_token}),200)
                
        return make_response(jsonify({"status":401,
                                        "error":" Password not accepted"}),401)


                

        