import json
from app import create_app

from app.tests.v1.base_test import TestBaseTest as BaseTest


class TestMeetupEndpoints(BaseTest):
        
    def post_data(self,data,path="/questions"):
        return self.client.post(path,data=json.dumps(data),headers=dict(Authorization="Bearer "+ self.login_user()),content_type="application/json")

    def get_specific_data(self,question_id):
        path = "/meetups/"
        path += str(question_id)
        return self.client.get(path, headers=dict(Authorization="Bearer "+ self.login_user()))
    
    def patch_upvote(self, question_id):
        path='/questions/'+str(question_id)+"/upvote"
        return self.client.patch(path,headers=dict(Authorization="Bearer "+ self.login_user()))
    
    def patch_downvote(self, question_id):
        path='/questions/'+str(question_id)+"/downvote"
        return self.client.patch(path,headers=dict(Authorization="Bearer "+ self.login_user()))
    
    def test_good_ask_question(self):
        question ={
                    "meetup_id":1,
                    "title" : "why?",
                    "body" : "Why so many questions?"
        }
        """test good meetup data"""
        response = self.post_data(question)
        self.assertEqual(response.status_code,201)

    def test_no_meetup_id(self):
        question ={
                    "meetup_id":"",
                    "title" : "why?",
                    "body" : "Why so many questions?"
        }
        """test no meetup id"""
        response = self.post_data(question)
        self.assertEqual(response.status_code,400)
    
    def test_no_title(self):
        question ={
                    "meetup_id":1,
                    "title" : "",
                    "body" : "Why so many questions?"
        }
        """test no title"""
        response = self.post_data(question)
        self.assertEqual(response.status_code,400)

    def test_no_body(self):
        question ={
                    "meetup_id":1,
                    "title" : "Why?",
                    "body" : ""
        }
        """test no body"""
        response = self.post_data(question)
        self.assertEqual(response.status_code,400)

    def test_invalid_meetup_id(self):
        question ={
                    "meetup_id":-1,
                    "title" : "Why?",
                    "body" : "Why so many questions?"
        }
        """invalid meetup id"""
        response = self.post_data(question)
        self.assertEqual(response.status_code,400)
    
    def test_invalid_meetup_id(self):
        question ={
                    "meetup_id":0,
                    "title" : "Why?",
                    "body" : "Why so many questions?"
        }
        """invalid meetup id"""
        response = self.post_data(question)
        self.assertEqual(response.status_code,400)
    
    def test_get_question_if_present(self):
        response = self.get_specific_data(1)
        """Test get question if present"""
        self.assertEqual(response.status_code,200)

    def test_get_upcoming_meetups_if_absent(self):
        question_one = self.get_specific_data(3)
        """Test get upcoming meetups if meetups absent"""
        self.assertEqual(question_one.status_code,404)
    
    # def test_downvote_question_present(self):
    #     self.create_question()
    #     response = self.patch_downvote(1)
    #     """Test downvote a question that is present"""
    #     self.assertEqual(response.status_code,200)
    
    def test_upvote_question_present(self):
        self.create_question()
        response = self.patch_upvote(1)
        """Test upvote a question that is present"""
        self.assertEqual(response.status_code,200)
    
    def test_upvote_question_absent(self):
        response = self.patch_upvote(5)
        """Test upvote a question that is absent"""
        self.assertEqual(response.status_code,404)

    def test_downvote_question_absent(self):
        response = self.patch_downvote(5)
        """Test downvote a question that is absent"""
        self.assertEqual(response.status_code,404)


    


    
