"""This module defines the meetup models and associated functions"""
from flask import jsonify, abort, json
from datetime import datetime

class Meetup(object):
    """This class encapsulates the functions of the meetup model"""
    def __init__(self):
        self.db = []
   
    def create_meetup(self, topic ,location ,happening_On ,tags ,image):
        payload = {
            "meetup_id" : len(self.db)+1,
            "topic":topic,
            "location":location,
            "happening_On":happening_On,
            "tags":tags,
            "created_on":datetime.now(),
            "images": image
        }
        self.db.append(payload)
        return payload
    

    def get_upcoming_meetups(self):
        return self.db

    def get_meetup(self, meetup_id):
        for meetup in self.db:
            if meetup["meetup_id"] == meetup_id:
                return meetup
        return False
    
    def delete_meetup(self, meetup_id):
        Meetup = [Meetup for Meetup in self.db if Meetup['meetup_id'] == meetup_id]
        if Meetup:
            self.db.remove(Meetup[0])
            return True
        return False