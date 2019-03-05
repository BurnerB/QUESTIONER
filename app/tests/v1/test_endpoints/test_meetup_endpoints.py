import json
from app import create_app

from app.tests.v1.base_test import TestBaseTest as BaseTest

class TestMeetup(BaseTest):
    """ Test class for meetups."""

    def post_data(self,data,path="/meetups"):
        return self.client.post(path,data=json.dumps(data), headers=dict(Authorization="Bearer "+ self.login_user()),content_type="application/json")

    def get_data(self,path='/meetups/upcoming'):
        return self.client.get(path,headers=dict(Authorization="Bearer "+ self.login_user()))
    
    def get_specific_data(self, meetup_id):
        path = "/meetups/"
        path = path + str(meetup_id)
        return self.client.get(path,headers=dict(Authorization="Bearer "+ self.login_user()))

    def delete_data(self,meetup_id):
        path = "/meetups/"
        path =path+str(meetup_id)+"/delete"
        return self.client.delete(path,headers=dict(Authorization="Bearer "+ self.login_user()))
    
    def post_rsvp(self,meetup_id, data):
        path = "/meetups/"
        path = path + str(meetup_id) + "/rsvps"
        return self.client.post(path,data=json.dumps(data), headers=dict(Authorization="Bearer "+ self.login_user()),content_type="application/json")

    def test_good_add_meetup(self):
        meetup1 ={
                    "topic":"Bio",
                    "location":"Nairobi",
                    "happening_On": "27/7/2019",
                    "tags" : "data science",
                    "image" : "an_image.png"
        }
        """test good meetup data"""
        response = self.post_data(meetup1)
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
        response = self.get_data()
        self.assertEqual(response.status_code,200)

    # def test_get_upcoming_meetups_if_absent(self):
    #     meetup_one = self.get_data()
    #     """Test get upcoming meetups if meetups absent"""
    #     self.assertEqual(meetup_one.status_code,404)

    def test_get_meetup_present(self):
        self.create_meetup()
        meetup_one = self.get_specific_data(1)
        """Test get a specific meetup when present"""
        self.assertEqual(meetup_one.status_code,200)

    def test_delete_meetup_present(self):
        meetup_one = self.delete_data(1)
        """Test delete a meetup when it exists"""
        self.assertEqual(meetup_one.status_code,404)

    def test_delete_meetup_absent(self):
        meetup_one=self.delete_data(4)
        """Test  delete a meetup that doesnt exist"""
        self.assertEqual(meetup_one.status_code,404)
    
    def test_rsvp_meetup_present(self):
        payload = {"answer":"Yes"}
        rsvp = self.post_rsvp(1, payload)
        self.assertEqual(rsvp.status_code,200)

    def test_rsvp_meetup_absent(self):
        payload = {"answer":"Yes"}
        rsvp = self.post_rsvp(10, payload)
        self.assertEqual(rsvp.status_code,404)

    def test_rsvp_meetup_invalid_data(self):
        payload = {"answer":"OP"}
        rsvp = self.post_rsvp(1, payload)
        self.assertEqual(rsvp.status_code,400)
    
    def test_rsvp_meetup_blank_data(self):
        payload = {"answer":""}
        rsvp = self.post_rsvp(1, payload)
        self.assertEqual(rsvp.status_code,400)

    

if __name__ == "__main__":
    unittest.main()