"""Test user model file"""
import unittest
from app.api.v1.models.meetup_models import Meetup

MeetupModel = Meetup()


class TestMeetup(unittest.TestCase):
    """Test Case for meetup model"""
    def setUp(self):
        self.topic = "Bio"
        self.location = "Nairobi"
        self.happening_On = "2019/02/27"
        self.tags = "data science"
        self.image = "an_image.png"
        # MeetupModel.db.append(data)
       
    def tearDown(self):
        MeetupModel.db = []
    
    def test_create_meetup(self):
        """Test if a meetup is added to the data structure"""
        
        topic = "Bio"
        location = "Nairobi"
        happening_On = "2019/02/27"
        tags = "data science"
        image = "an_image.png"
        meetup = MeetupModel.create_meetup(topic ,location , happening_On,tags ,image)
        self.assertEqual(1,len(MeetupModel.db))

    def test_get_meetup(self):
        """ Test if a user can search a specific meetup"""
        meetup = MeetupModel.create_meetup(self.topic ,self.location , self.happening_On,self.tags ,self.image)
        self.assertEqual(1,len(MeetupModel.db))
        result = MeetupModel.get_meetup(1)
        self.assertEqual(1,result["meetup_id"])

    def test_delete_meetup(self):
        """Test if an admin can delete a meetup"""
        meetup = MeetupModel.create_meetup(self.topic ,self.location , self.happening_On,self.tags ,self.image)
        self.assertEqual(1,len(MeetupModel.db))
        result = MeetupModel.delete_meetup(1)
        self.assertTrue(result)


    
    

if __name__ == "__main__":
    unittest.main()
