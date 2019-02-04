"""Test user model file"""

import unittest
# from app.api.v1.models.user_models import user_models

class TestUser(unittest.TestCase):
    """Test Case for user model"""
    def setUp(self):
        User.user_list=[]
    
    def test_create_user(self):
        """Test if a user is added to the data structure"""
        user = User.create_user()
        self.assertEqual(1,len(User.user_list))
        self.assertTrue(user,dict)

    def test_delete_user(self):
        """Test if a user is successfully deleted"""
        user1 = User.create_user()
        self.assertEqual(1,len(User.user_list))
        user=User.delete_user(1)
        self.assertEqual(0,len(User.user_list))

    def tearDown(self):
        User.user_list=[]
    

if __name__ == "__main__":
    unittest.main()



        
        