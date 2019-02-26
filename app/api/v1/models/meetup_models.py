"""This module defines the meetup models and associated functions"""
from datetime import datetime

meetup_list = []

class Meetup(object):
    """This class encapsulates the functions of the meetup model"""
    def __init__(self):
        self.db = meetup_list
   
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
    
    def delete_meetup(self, meetup_id):
        meetup = self.get_meetup(meetup_id)
        if meetup == None:
            return False
        meetup_list.remove(meetup)
        return True