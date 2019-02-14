"""Test user model file"""
import unittest
from app.api.v1.models.user_models import User

class TestUser(unittest.TestCase):
    """Test Case for user model"""
    def setUp(self):
        user_id = 1
        firstname = "John"
        lastname = "Doe"
        email = "johndoe@gmail.com"
        phone_number = "0272988632"
        username = "Johny"
        password = "baba123"
        confirmpassword = "baba123"
        registered  =  "4 27/2/19"
        isAdmin =  False
        user = User(firstname,lastname,email,phone_number ,username ,password ,confirmpassword)
        User.user_list.append(user)

    
    def test_create_user(self):
        """Test if a user is added to the data structure"""
        User.user_list = []
        firstname = "John"
        lastname = "Doe"
        email = "johndoe@gmail.com"
        phone_number = "0272988632"
        username = "Johny"
        password = "baba123"
        confirmpassword = "baba123"
        user = User.create_user(firstname,lastname,email,phone_number ,username ,password ,confirmpassword)
        self.assertEqual(1,len(User.user_list))

        
    def tearDown(self):
        User.user_list=[]
    

if __name__ == "__main__":
    unittest.main()



        
        