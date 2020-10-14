from flask import Response,request
from flask_jwt_extended import jwt_required
from database.models import Question,QuestionText
from flask_restful import Resource
from http import HTTPStatus

from flask_mongoengine import MongoEngine
from mongoengine.queryset import QuerySet
import random

from mongoengine.errors import FieldDoesNotExist, \
    NotUniqueError,DoesNotExist,ValidationError,InvalidQueryError

from resources.errors import SchemaValidationError, QuestionAlreadyExistsError, \
    InternalServerError, UpdatingQuestionError, DeletingQuestionError, QuestionNotExistsError, \
        InvalidTagError, InvalidDifficultyError, InvalidNumOfQuestionsError

from ml.texttoquestion import TextToQuestion

class GenerateAIQuestion(Resource):

    @jwt_required
    def post(self):
        try:
            body = request.get_json()

            questionText = QuestionText(**body)
            
            text = questionText['text']
            tag = questionText['tag']
            difficulty = questionText['difficulty']
            num_of_questions = questionText['num_of_questions']

            ml_pipeline = TextToQuestion()
            questions = ml_pipeline.generateQuestions(text, num_of_questions)    

            wo_prob = ml_pipeline.remove_prob_and_send_to_db('questions.json')
            id_list = []

            for i in wo_prob:
                i['tag'],i['difficulty'] = tag.lower(),difficulty.lower()
                question = Question(**i).save()
                id = question.id
                id_list.append(id)

            return {'id':[str(iD) for iD in id_list]},HTTPStatus.OK
        
        except DoesNotExist:
            raise QuestionNotExistsError
        except Exception:
            raise InternalServerError
        
