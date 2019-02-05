"""This module defines the user model and associated functions"""

from datetime import datetime


class User(object):
    user_list = []
    """This class encapsulates the functions of the user model"""
    def __init__(self, user_id, firstname,lastname,email,phone_number ,username ,password ,confirmpassword, registerd, isAdmin):
        self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone_number = phone_number
        self.username = username
        self.password = password
        self.confirmpassword = confirmpassword
        self.registered  =  registerd
        self.isAdmin =  isAdmin

    @staticmethod
    def create_user(firstname,lastname,email,phone_number ,username ,password ,confirmpassword):
        user = User(len(User.user_list) + 1, firstname,lastname, email, phone_number ,username ,password  ,confirmpassword, datetime.now(), False)
        User.user_list.append(user)

  
    @staticmethod
    def get_a_user_by_username(username):
        for user in self.db:
            if user["username"] == username:
                return user

    @staticmethod
    def get_a_user_by_id(user_id):
        for user in User.user_list:
            if user.user_id == user_id:
                return user
        return None
    
    @staticmethod 
    def delete_user(user_id):
        user = User.get_a_user_by_id(user_id)
        if user == None:
            return False
        User.user_list.remove(user)
        return True