from flask import Flask, Blueprint, request ,jsonify ,make_response
import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.api.v1.utils.validators import Validators

Validators = Validators()

""" local imports"""
from app.api.v1.models.meetup_models import Meetup
MeetupModel = Meetup()
from instance.config import Config

version_1 = Blueprint("Meetups" ,__name__)


@version_1.route("/meetups",methods=["POST"])
# @jwt_required
def create_meetup():
    try:
        data=request.get_json()
        topic = data["topic"]
        location = data["location"]
        happening_On = data["happening_On"]
        tags = data["tags"]
        image = data["image"]
    
        """checks if any key missing"""
    except Exception as e:
            return jsonify({"status":400,
                            "error" :"Invalid {} key field".format(e)
                                    }),400

    if not Validators.check_topic(topic):
        return jsonify ({"status":400,
                            "error":"Topic contains invalid characters"}),400
    
    if not Validators.check_location(location):
        return jsonify ({"status":400,
                        "error":"Location contains invalid characters"}),400


    try:
        datetime.datetime.strptime(happening_On, '%d/%m/%Y')
    except Exception as e:
        return jsonify({"status":400,
                        "error" :"Incorrect data format, should be DD/MM/YYYY"
                                }),400
    
    # if not Validators.check_hapenningOn_date(happening_On):
    #     return jsonify ({"status":400,
    #                     "error":"Date has already passed"}),400
    
    if Validators.check_image == None:
        return jsonify ({"status":400,
                        "error":"Unsupported image type"}),400
    
    if len(topic)== 0 or len(location) == 0 or len(happening_On) == 0 or len(tags)== 0 or len(image) == 0:
        return jsonify({"message":"cannot be an empty string"}),400

    MeetupModel.create_meetup(topic, location, happening_On ,tags ,image)
    return jsonify({"message":"Successful"}),201

@version_1.route("/meetups/upcoming", methods=["GET"])
def get_upcoming_meetups():
    """Method that gets all meetups"""
    if MeetupModel.db == []:
        return jsonify({"Message":"Meetup list is empty"}),404
    response = MeetupModel.get_upcoming_meetups()
    return jsonify({"Meetups":response}),200


@version_1.route('/meetups/<int:meetup_id>',methods=['GET'])
def get_specific_meetup(meetup_id):
    meetup = MeetupModel.get_meetup(meetup_id)
    if meetup == None:
        return jsonify({"message":"meetup doesn't exist"}),404
    return jsonify({'Question':meetup}),200

@version_1.route('/meetups/<int:meetup_id>/delete',methods=['DELETE'])
def delete_meetup(meetup_id):
    meetup = MeetupModel.get_meetup(meetup_id)
    if meetup == None:
        return jsonify({"message":"meetup doesn't exist"}),404
    if MeetupModel.delete_meetup(meetup_id) == False:
        return jsonify({"message":"meetup doesn't exist"}),404
    return jsonify({"message":"Successfully deleted meetup"}),200
