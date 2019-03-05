from flask import Flask, Blueprint, request ,jsonify ,make_response
import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.exceptions import BadRequest, NotFound, Unauthorized, Forbidden, MethodNotAllowed

from app.api.v1.utils.validators import Validators

Validators = Validators()

""" local imports"""
from app.api.v1.models.meetup_models import Meetup
MeetupModel = Meetup()
from instance.config import Config

version_1 = Blueprint("Meetups" ,__name__)


@version_1.route("/meetups",methods=["POST"])
@jwt_required
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
                raise BadRequest("{} is lacking. It is a required field".format(e))

    if not Validators.check_topic(topic):
        raise BadRequest("Topic contains invalid characters")
    
    if not Validators.check_location(location):
        raise BadRequest("Location contains invalid characters")


    try:
        datetime.datetime.strptime(happening_On, '%d/%m/%Y')
    except Exception as e:
        raise BadRequest("Incorrect data format, should be DD/MM/YYYY")
    
    # if not Validators.check_hapenningOn_date(happening_On):
    #     raise BadRequest("Date entered has already passed")
    #                    
    
    if Validators.check_image == None:
        raise BadRequest("Unsupported image type")
        
    
    if len(topic)== 0 or len(location) == 0 or len(happening_On) == 0 or len(tags)== 0 or len(image) == 0:
        raise BadRequest("cannot be an empty string")

    meetup = MeetupModel.create_meetup(topic, location, happening_On ,tags ,image)
    return jsonify({"message":"Successfully Created Meetup",
                    "data":data}),201

@version_1.route("/meetups/upcoming", methods=["GET"])
@jwt_required
def get_upcoming_meetups():
    """Method that gets all meetups"""
    if MeetupModel.db == []:
        raise NotFound("Meetup list is empty")
        
    response = MeetupModel.get_upcoming_meetups()
    return jsonify({"Meetups":response}),200


@version_1.route('/meetups/<int:meetup_id>',methods=['GET'])
@jwt_required
def get_specific_meetup(meetup_id):
    meetup = MeetupModel.get_meetup(meetup_id)
    if meetup == False:
        raise NotFound("meetup doesn't exist")
    return jsonify({'Question':meetup}),200

@version_1.route('/meetups/<int:meetup_id>/delete',methods=['DELETE'])
@jwt_required
def delete_meetup(meetup_id):
    meetup = MeetupModel.get_meetup(meetup_id)
    if meetup == None:
        raise NotFound("meetup doesn't exist")
    if MeetupModel.delete_meetup(meetup_id) == False:
        raise NotFound("meetup doesn't exist")
    return jsonify({"message":"Successfully deleted meetup"}),200

@version_1.route('/meetups/<int:meetup_id>/rsvps', methods=['POST'])
@jwt_required
def add_rsvp(meetup_id):

    try:
        data = request.get_json()
        answer = data["answer"]
         
    except Exception as e:
        raise BadRequest("{} is lacking. It is a required field".format(e))

    """Check if the meetup exists"""
    if not MeetupModel.get_meetup(meetup_id):
        raise NotFound("The meetup does not exist")
    
    responses = ["Yes","No","Maybe"]
    if answer not in responses:
        raise BadRequest('Invalid rsvp answer')
       
    
    for meetup in MeetupModel.db:
        if meetup["meetup_id"] == meetup_id:
            return jsonify({
                            'status': 200,
                            'message': 'Responded successfully',
                            'data': {
                                    'meetup_id': meetup['meetup_id'],
                                    'topic' : meetup['topic'],
                                    "Happening On":meetup["happening_On"],
                                    'Answer': answer
                                            }
                                    }), 200

