"""Test user model file"""
import unittest
from app.api.v1.models.questions_models import Question

QuestionModel = Question()


class TestQuestion(unittest.TestCase):
    def setUp(self):
        self.meetup_id = "1"
        self.title = "why?"
        self.body = "Why so many questions?"
    
    def tearDown(self):
        QuestionModel.question_list = []
    
    def test_ask_question(self):
        """Test if a question is added to the data structure"""
        meetup_id = "1"
        title = "why?"
        body = "Why so many questions?"
        QuestionModel.ask_question(meetup_id, title, body)
        self.assertEqual(1,len(QuestionModel.question_list))
    
    def test_upvote(self):
        """Test if a question can be upvoted"""
        question = QuestionModel.ask_question(self.meetup_id, self.title, self.body)
        self.assertEqual(1,len(QuestionModel.question_list))
        upvote = QuestionModel.upvote(1)
        self.assertEqual(1,upvote["votes"])
    
    def test_downvote(self):
        """Test if a question can be downvoted"""
        question = QuestionModel.ask_question(self.meetup_id, self.title, self.body)
        self.assertEqual(1,len(QuestionModel.question_list))
        downvote = QuestionModel.downvote(1)
        self.assertEqual(-1,downvote["votes"])
    
    def test_get_question_by_id(self):
        """Test if a question can be gotten by its id"""
        question = QuestionModel.ask_question(self.meetup_id, self.title, self.body)
        self.assertEqual(1,len(QuestionModel.question_list))
        question1 = QuestionModel.get_question_by_id(1)
        self.assertTrue(question1)