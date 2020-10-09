from flask import Flask,Response,request,jsonify
from http import HTTPStatus
from database.db import initialize_db
from database.models import Question
import json


app = Flask(__name__)

# questions = [
#     {
#       "tag" : "biology",
#       "difficulty" : "easy",
#       "question" : "What is respiration?",
#       "option_1" : "breathing",
#       "option_2" : "singing",
#       "option_3" : "sleeping",
#       "option_4" : "eating",
#       "correct_answer " : "option_1"
#     },
#     ]


app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/Best-Geese'
}

initialize_db(app)


@app.route('/')
def hello():
    return {'Hello':'World'}
    
@app.route('/questions')
def get_questions():
    questions = Question.objects().to_json()
    return Response(questions,
                    mimetype='application/json',
                    status=200)


@app.route('/questions',methods=['POST'])
def add_question():
    body = request.get_json()
    question = Question(**body).save()
    id = question.id
    return{'id':str(id)},HTTPStatus.OK


@app.route('/questions/<id>',methods=['PUT'])
def update_question(id):
    body = request.get_json()
    
    if body is None:
        return {'Error':'Question not found'},HTTPStatus.NO_CONTENT
    
    Question.get(id=id).update(**body)
    return '',HTTPStatus.OK

@app.route('/questions/<id>',methods=['DELETE'])
def delete_question(id):
    question = Question.objects.get(id=id).delete()
    return '',HTTPStatus.OK

@app.route('/questions/<id>')
def get_question(id):
    questions = Question.objects.get(id=id).to_json()
    return Response(questions,
                    mimetype="application/json",
                    status = 200)

if __name__ == "__main__":
    app.run(debug=True)