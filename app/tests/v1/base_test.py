import unittest
from app import create_app
import json


class TestBaseTest(unittest.TestCase):
    """ Base class for testcases."""
    """The set up method is called for each test method"""

    def setUp(self):
        """Performs variable definition and app initialization"""

        self.app = create_app('testing')
        self.client = self.app.test_client()

        self.user = {
             "firstname":"Jane",
	         "lastname":"Doe",
	         "email":"janedoe@gmail.com",
	         "phone_number":"073376183",
	         "username":"jenny",
	         "password":"mama123",
	         "confirmpassword":"mama123"
        }     

        self.login = {
            "username":"jenny",
	        "password":"mama123"
        }

    
        
        self.meetup ={
                    "topic":"Bio",
                    "location":"Nairobi",
                    "happening_On": "27/05/2019",
                    "tags" : "data science",
                    "image" : "an_image.png"
        }

        self.question = {
                        "meetup_id" : 1,
                        "title ": "why?",
                        "body" : "Why so many questions?"
        } 
    
    def login_user(self):
        register = self.client.post("/api/v1/user/auth/signup", data=json.dumps(self.user), content_type = "application/json")
        user_login = self.client.post("/api/v1/user/auth/signin", data=json.dumps(self.login), content_type = "application/json")
        login_data = json.loads(user_login.data.decode('utf-8'))
        token = login_data["access_token"]
        return token 

    def create_meetup(self):
        return self.client.post('/meetups', data=json.dumps(self.meetup),headers=dict(Authorization="Bearer "+ self.login_user()), content_type="application/json")
    
    def create_question(self):
        return self.client.post('"/questions"', data=json.dumps(self.question),headers=dict(Authorization="Bearer "+ self.login_user()), content_type="application/json")

    def tearDown(self):
        self.client = None