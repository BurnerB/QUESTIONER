"""Test user model file"""
import unittest
from app.api.v1.models.meetup_models import meetup_list,Meetup

Meetup = Meetup()


class TestMeetup(unittest.TestCase):
    """Test Case for meetup model"""
    def setUp(self):
        pass
       

    
    def test_create_meetup(self):
        """Test if a meetup is added to the data structure"""
        
        topic = "Bio"
        location = "Nairobi"
        happening_On = "2019/02/27"
        tags = "data science"
        image = "an_image.png"
        meetup = Meetup.create_meetup(topic ,location , happening_On,tags ,image)
        self.assertEqual(2,len(meetup_list))

    def test_get_meetup(self):
        """ Test if a user can search a specific meetup"""
        result = Meetup.get_meetup(2)
        self.assertEqual(2,result["meetup_id"])

    def test_delete_meetup(self):
        """Test if an admin can delete a meetup"""
        result = Meetup.delete_meetup(1)
        self.assertTrue(result)


    def tearDown(self):
        meetup_list = []
    

if __name__ == "__main__":
    unittest.main()
