from flask import Blueprint,Response,request
from database.models import Question


questions = Blueprint('questions',__name__)

@questions.route('/questions')
def get_questions():
    questions = Question.objects().to_json()
    return Response(questions,
                    mimetype='application/json',
                    status=200)


@questions.route('/questions',methods=['POST'])
def add_question():
    body = request.get_json()
    question = Question(**body).save()
    id = question.id
    return{'id':str(id)},HTTPStatus.OK


@questions.route('/questions/<id>',methods=['PUT'])
def update_question(id):
    body = request.get_json()
    
    if body is None:
        return {'Error':'Question not found'},HTTPStatus.NO_CONTENT
    
    Question.get(id=id).update(**body)
    return '',HTTPStatus.OK

@questions.route('/questions/<id>',methods=['DELETE'])
def delete_question(id):
    question = Question.objects.get(id=id).delete()
    return '',HTTPStatus.OK

@questions.route('/questions/<id>')
def get_question(id):
    questions = Question.objects.get(id=id).to_json()
    return Response(questions,
                    mimetype="application/json",
                    status = 200)
