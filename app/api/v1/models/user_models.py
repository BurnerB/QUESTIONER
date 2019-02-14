"""This module defines the user model ans associated functions"""
from datetime import datetime



class User(object):
    user_list = []
    """This class encapsulates the functions of the user model"""
    def __init__(self,*args):
        self.firstname = args[0]
        self.lastname = args[1]
        self.email = args[2]
        self.phone_number = args[3]
        self.username = args[4]
        self.password = args[5]
        self.confirmpassword = args[6]
    
    @staticmethod
    def create_user(firstname, lastname, email ,phone_number ,username ,password ,confirmpassword):
        payload = {
            "user_id": len(User.user_list) + 1,
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "phone_number":phone_number,
            "username": username,
            "password":password,
            "confirmpassword" : confirmpassword,
            "registered" : datetime.now(),
            "isAdmin": False
        }
        
        User.user_list.append(payload)
        return payload
    
    @staticmethod
    def get_a_user_by_username(username):
        user = [user for user in User.user_list if user["username"] == username]
        return user

    @staticmethod
    def get_a_user_by_password(password):
        user = [user for user in User.user_list if user["password"] == password]
        return User

    @staticmethod
    def get_a_user_by_id(user_id):
        user = [user for user in User.user_list if user.user_id == user_id]
        return User
    
