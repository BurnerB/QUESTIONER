from flask import Flask,Blueprint,request,jsonify,make_response


"""Local imports"""
from app.api.v1.models.questions_models import Question

QuestionModel=Question()

version_1 = Blueprint("questions" ,__name__)

@version_1.route("/questions" ,methods = ["POST"])
def create_question():
        try:
               data = request.get_json()
               meetup_id = data["meetup_id"]
               title = data["title"]
               body = data["body"]

        except Exception as e:
            return jsonify({
                            "error" :"Invalid {} key field".format(e)
                            }),400
        
        if  meetup_id == "" or meetup_id <= 0 or len(title) == 0 or len(body) == 0:
                return jsonify({"status":400,
                                "message":"Input fields cannot be empty"}),400
        response = QuestionModel.ask_question(meetup_id, title ,body)
        return make_response(jsonify({"status":201,
                                        "data": response})),201


@version_1.route("/questions" ,methods = ["GET"])
def get_questions():
        """Method that gets all meetups"""
        if QuestionModel.question_list == []:
                return jsonify({"Message":"Questions list is empty"}),404
        response = QuestionModel.get_questions()
        return jsonify({"Questions":response}),200




@version_1.route("/questions/<int:question_id>/upvote" ,methods = ["PATCH"])
def upvote_question(question_id):
        
        """Checks if the question exists"""
        if not QuestionModel.get_question_by_id(question_id):
                return jsonify({"status":404,
                                "message":"The question does not exist"}),404

        """Checks if the user has already voted"""
        for question in QuestionModel.question_list:
                if question["createdBy"] in QuestionModel.users:
                        return jsonify({"Status":400,
                                        "message":"The user has already voted"}),400
        
        response = QuestionModel.upvote(question_id)
        return make_response(jsonify({"status":200,
                                     "message":response
                                     })),200

@version_1.route("/questions/<int:question_id>/downvote" ,methods = ["PATCH"])
def downvote_question(question_id):
        
        """Checks if the question exists"""
        if not QuestionModel.get_question_by_id(question_id):
                return jsonify({"status":404,
                                "message":"The question does not exist"}),404

        """Checks if the user has already voted"""
        for question in QuestionModel.question_list:
                if question["createdBy"] in QuestionModel.users:
                        return jsonify({"Status":400,
                                        "message":"The user has already voted"}),400
        
        response = QuestionModel.downvote(question_id)
        return make_response(jsonify({"status":200,
                                     "message":response
                                     })),200
