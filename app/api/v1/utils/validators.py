"""Validators Module"""
import re
from app.api.v1.endpoints.user_endpoints import User
# from app.api.v1.endpoints.meetup_endpoints import Meetup

class Validators():
    """Validators class"""

    def check_names(self, name):
        """ Validate firstname and lastname"""
        regex ="^[a-zA-Z]{3,}$"
        return re.match(regex, name)
    
    def valid_email(self, email):
        """ valid email """
        regex = "^[-\w\.]+@([\w-]+\.)+[\w-]{2,4}$"
        return re.match(regex, email)

    def valid_phone_number(self, phone_number):
        """Validate phone number"""
        regex = "^[\d]{,10}$"
        return re.match(regex, phone_number)

    def valid_username(self, username):
        """validate username"""
        regex = "^[a-zA-Z0-9]{3,}$"
        return re.match(regex, username)
    
    def valid_password(self, password):
        """ valid password """
        regex = "^[a-zA-Z0-9@_+-.]{6,}$"
        return re.match(regex, password)

    def check_email_exists(self, email):
        """Check if the email exists"""
        for user in User.user_list:
            if user["email"] == email:
                return True
        return False
    
    def check_username_exists(self, username):
        """checks if the username exists"""
        for user in User.user_list:
            if user["username"] == username:
                return True
        return False
