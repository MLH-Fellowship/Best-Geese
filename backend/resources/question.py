from flask import Response,request
from database.models import Question
from flask_restful import Resource
from http import HTTPStatus


class QuestionsApi(Resource):
    
    def get(self,):
        questions = Question.objects().to_json()
        return Response(questions,
                        mimetype='application/json',
                        status=200)

    def post(self):
        body = request.get_json(force =True)
        question = Question(**body).save()
        id = question.id
        return{'id':str(id)},HTTPStatus.OK


class QuestionApi(Resource):
    def put(self,id):
        body = request.get_json(force =True)
        Question.objects.get(id=id).update(**body)
        return '',HTTPStatus.OK

    def delete(self,id):
        question = Question.objects.get(id=id).delete()
        return '',HTTPStatus.OK

    def get(self,id):
        questions = Question.objects.get(id=id).to_json()
        return Response(questions,
                    mimetype="application/json",
                    status = 200)
