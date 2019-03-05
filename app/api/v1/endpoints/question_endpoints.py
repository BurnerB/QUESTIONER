from flask import Flask,Blueprint,request,jsonify,make_response
from werkzeug.exceptions import BadRequest, NotFound, Unauthorized, Forbidden, MethodNotAllowed
from flask_jwt_extended import jwt_required, get_jwt_identity


"""Local imports"""
from app.api.v1.models.questions_models import Question

QuestionModel=Question()

version_1 = Blueprint("questions" ,__name__)

@version_1.route("/questions" ,methods = ["POST"])
@jwt_required
def create_question():
        try:
               data = request.get_json()
               meetup_id = data["meetup_id"]
               title = data["title"]
               body = data["body"]

        except Exception as e:
                raise BadRequest("{} is lacking. It is a required field".format(e))
        
        if  meetup_id == "" or meetup_id <= 0 or len(title) == 0 or len(body) == 0:
                raise BadRequest("Input fields cannot be empty")

        response = QuestionModel.ask_question(meetup_id, title ,body)
        return make_response(jsonify({"status":201,
                                        "data": response})),201


@version_1.route("/questions" ,methods = ["GET"])
@jwt_required
def get_questions():
        """Method that gets all meetups"""
        if QuestionModel.question_list == []:
                raise NotFound("Questions list is empty")
        response = QuestionModel.get_questions()
        return jsonify({"Questions":response}),200




@version_1.route("/questions/<int:question_id>/upvote" ,methods = ["PATCH"])
@jwt_required
def upvote_question(question_id):
        
        """Checks if the question exists"""
        if not QuestionModel.get_question_by_id(question_id):
                raise NotFound("The question does not exist")

        """Checks if the user has already voted"""
        for question in QuestionModel.question_list:
                if (question["createdBy"] in QuestionModel.users) and (question["question_id"] in QuestionModel.questions):
                        raise BadRequest("The user has already voted")
        
        response = QuestionModel.upvote(question_id)
        return make_response(jsonify({"status":200,
                                     "message":response
                                     })),200

@version_1.route("/questions/<int:question_id>/downvote" ,methods = ["PATCH"])
@jwt_required
def downvote_question(question_id):
        
        """Checks if the question exists"""
        if not QuestionModel.get_question_by_id(question_id):
                raise NotFound("The question does not exist")


        """Checks if the user has already voted"""
        for question in QuestionModel.question_list:
                if (question["createdBy"] in QuestionModel.users) and (question["question_id"] in QuestionModel.questions):
                        raise BadRequest("The user has already voted")
        
        response = QuestionModel.downvote(question_id)
        return make_response(jsonify({"status":200,
                                     "message":response
                                     })),200
