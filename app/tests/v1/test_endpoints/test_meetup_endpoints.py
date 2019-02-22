import unittest
import json
from app import create_app
from app.api.v1.models.meetup_models import meetup_list,Meetup
MeetupModel =Meetup()


class TestMeetupEndpoints(unittest.TestCase):
    """The set up method is called for each test method"""
    """This is the same for teardown"""
    def setUp(self):
        """Performs variable definition and app initialization"""
        self.app = create_app("testing")
        self.client = self.app.test_client()
        # meetup_list=[]
        # MeetupModel.create_meetup("Bio","Nairobi", "27/3/2019", "data science", "an_image.png")
        # self.assertTrue(len(meetup_list) == 1)


    def post_data(self,data,path="/meetups"):
        return self.client.post(path,data=json.dumps(data),headers={},content_type="application/json")

    def get_data(self,path='/meetups/upcoming'):
        return self.client.get(path)
    
    def get_specific_data(self, meetup_id):
        path = "/meetups/"
        path += str(meetup_id)
        return self.client.get(path)

    def delete_data(self,meetup_id):
        path = "/meetups/"
        path += str(meetup_id)
        return self.client.delete(path)

    def test_good_add_meetup(self):
        meetup ={
                    "topic":"Bio",
                    "location":"Nairobi",
                    "happening_On": "27/7/2019",
                    "tags" : "data science",
                    "image" : "an_image.png"
        }
        """test good meetup data"""
        response = self.post_data(meetup)
        self.assertEqual(response.status_code,201)

    def test_no_topic_meetup(self):
        meetup ={
                    "topic":"",
                    "location":"Nairobi",
                    "happening_On": "27/7/2019",
                    "tags" : "data science",
                    "image" : "an_image.png"
        }
        """method tests no topic"""
        response = self.post_data(meetup)
        self.assertEqual(response.status_code,400)

    def test_no_location_meetup(self):
        meetup ={
                    "topic":"Bio",
                    "location":"",
                    "happening_On": "27/7/2019",
                    "tags" : "data science",
                    "image" : "an_image.png"
        }
        """test no location"""
        response = self.post_data(meetup)
        self.assertEqual(response.status_code,400)

    def test_no_date_meetup(self):
        meetup ={
                    "topic":"Bio",
                    "location":"Nairobi",
                    "happening_On": "",
                    "tags" : "data science",
                    "image" : "an_image.png"
        }
        """test no happeningOn date"""
        response = self.post_data(meetup)
        self.assertEqual(response.status_code,400)

    def test_no_tags_meetup(self):
        meetup ={
                    "topic":"Bio",
                    "location":"Nairobi",
                    "happening_On": "27/7/2019",
                    "tags" :"",
                    "image" : "an_image.png"
        }
        """test no tag"""
        response = self.post_data(meetup)
        self.assertEqual(response.status_code,400)
    
    def test_no_image(self):
        meetup = {
                    "topic":"Bio",
                    "location":"Nairobi",
                    "happening_On": "27/7/2019",
                    "tags" : "data science",
                    "image" :""

        }
        """test no image"""
        response = self.post_data(meetup)
        self.assertEqual(response.status_code,400)

    def test_get_upcoming_meetups_if_present(self):
        response = self.get_specific_data(1)
        self.assertEqual(response.status_code,200)

    def test_get_upcoming_meetups_if_absent(self):
        meetup_one = self.get_data()
        """Test get upcoming meetups if meetups absent"""
        self.assertEqual(meetup_one.status_code,404)

    def test_get_meetup_present(self):
        meetup_one = self.get_specific_data(1)
        """Test get a specific meetup when present"""
        self.assertEqual(meetup_one.status_code,200)

    # def test_delete_meetup_present(self):
    #     meetup_one = self.delete_data(1)
    #     """Test delete a meetup when it exists"""
    #     self.assertEqual(meetup_one.status_code,200)

    # def test_delete_meetup_absent(self):
    #     meetup_one=self.delete_data(1)
    #     """Test  delete a meetup that doesnt exist"""
    #     self.assertEqual(meetup_one.status_code,404)
    
    def tearDown(self):
        meetup_list =[]

if __name__ == "__main__":
    unittest.main()