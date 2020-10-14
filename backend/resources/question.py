# backend/resources/question.py

from flask import Response,request
from flask_jwt_extended import jwt_required
from database.models import Question#,QuestionText
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

class QuestionsApi(Resource):
    @jwt_required
    def get(self):
        """
        '/api/questions'
        Gets all the questions


        Returns:
            questions: As a json response. 
        """
        questions = Question.objects().to_json()
        return Response(questions,
                        mimetype='application/json',
                        status=200)
    @jwt_required
    def post(self):
        """
        Add a new question

        '/api/questions'
        
        """
        try:
            body = request.get_json(force =True)
            question = Question(**body).save()
            id = question.id
            return{'id':str(id)},HTTPStatus.OK
        except(FieldDoesNotExist,ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise QuestionAlreadyExistsError


class QuestionApi(Resource):
    @jwt_required
    def put(self,id):
        """
        Modify a question

        Args:
            id (string): Look for question with the specified "id"

        Returns:
            (int): [HTTPStatus.OK (200)]
        """
        try:
            body = request.get_json(force =True)
            Question.objects.get(id=id).update(**body)
            return '',HTTPStatus.OK
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingQuestionError
        except Exception:
            raise InternalServerError
    
    @jwt_required
    def delete(self,id):
        """
        Remove a question from the collection.

        Args:
            id (string): Look for question with the specified "id"

        Returns:
            (int): HTTPStatus.OK (200)
        """
        try:
            question = Question.objects.get(id=id).delete()
            return '',HTTPStatus.OK
        except DoesNotExist:
            raise DeletingMovieError
        except Exception:
            raise InternalServerError

    def get(self,id):
        """
        Get a single question 

        Args:
            id (string): Look for question with the specified "id"
        
        Returns:
            question: As a json response. 

        """
        try:
            questions = Question.objects.get(id=id).to_json()
            return Response(questions,
                            mimetype="application/json",
                            status = 200)
        except DoesNotExist:
            raise QuestionNotExistsError
        except Exception:
            raise InternalServerError





