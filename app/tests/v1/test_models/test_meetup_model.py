"""Test user model file"""
import unittest
from app.api.v1.models.meetup_models import Meetup

class TestMeetup(unittest.TestCase):
    """Test Case for meetup model"""
    def setUp(self):
        meetup_id = 1
        topic = "Bio"
        location:"Nairobi",
        happening_On:"27/3/2019",
        tags:"data science"
        created_on:"4 27/2/19"
        image = "an_image.png"
        meetup = Meetup(topic ,location , happening_On,tags ,image)
        Meetup.meetup_list.append(meetup)

    def test_create_meetup(self):
        """Test if a meetup is added to the data structure"""
        Meetup.meetup_list = []
        topic = "Bio"
        location:"Nairobi",
        happening_On:"27/3/2019",
        tags:"data science"
        image = "an_image.png"
        meetup = Meetup.create_meetup(topic ,location , happening_On,tags ,image)
        self.assertEqual(1,len(Meetup.meetup_list))

    def test_get_meetup(self):
        """ Test if a user can search a specific meetup"""
        result = Meetup.get_meetup(1)
        self.assertEqual(1,result.question_id)

    def test_delete_meetup(self):
        """Test if an admin can delete a meetup"""
        result = Meetup.delete_meetup(1)
        self.assertTrue(result)


    def tearDown(self):
        Meetup.meetup_list = []
    

if __name__ == "__main__":
    unittest.main()
