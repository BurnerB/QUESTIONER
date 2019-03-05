from flask import jsonify, Blueprint, request, json
from datetime import datetime
from uuid import uuid4


class Question():
    """ Creates the question model """
    def __init__(self):
        self.question_list = []
        self.users = []
        self.questions = []
    
    def ask_question(self, meetup_id, title, body,):
        """ Adds a new question to the all_question_records list """
        new_question = {
            "question_id": len(self.question_list) + 1,
            "createdOn": datetime.now(),
            "createdBy": uuid4().int, # generate userId
            "meetup_id": meetup_id, 
            "title": title,
            "body": body,
            "votes":0
        }
        self.question_list.append(new_question)
        return new_question
    
    def get_questions(self):
        return self.question_list
        
    def upvote(self, question_id):
        question = [question for question in self.question_list if question['question_id'] == question_id]
        if  question:
            question = question[0]
            question['votes'] = question['votes'] + 1
            self.users.append(question["createdBy"])
            self.questions.append(question["question_id"])
            return question
    
    def downvote(self, question_id):
        question = [question for question in self.question_list if question['question_id'] == question_id]
        if  question:
            question = question[0]
            question['votes'] = question['votes'] - 1
            self.users.append(question["createdBy"])
            self.questions.append(question["question_id"])
            return question
    
    def get_question_by_id(self, question_id):
        question = [question for question in self.question_list if question['question_id'] == question_id]
        if  question:
            return True
        return False