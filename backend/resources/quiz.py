from flask import Response,request
from flask_jwt_extended import jwt_required
from database.models import Question
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


class QuizApi(Resource):
    
    @jwt_required
    def get(self):
        """
        Get questions that match the parameters requested.

        Args:
            tag (string) : Subject Name
            difficulty (string) : Easy, Medium, Hard, Mix
            num_of_questions(int) 

        Returns:
            questions : As a json response. 
        """
    
        # Parse URL arguments/parameters
        # Tags
        tag = request.args.get('tag',None,str).lower()
        if (tag not in ['biology','physics','chemistry','mathematics','computer science','art']) or (tag is None):
            return InvalidTagError
        difficulty = request.args.get('difficulty').lower()
        if (difficulty not in ['easy','medium','hard','mix']) or (difficulty is None): #
            return InvalidDifficultyError,HTTPStatus.BAD_REQUEST

        # Number of Questions
        num_of_questions = int(request.args.get('num_of_questions'))
        if (num_of_questions is None) or  ((num_of_questions < 10) or (num_of_questions > 50)):
            return InvalidNumOfQuestionsError, HTTPStatus.BAD_REQUEST

        try:
            if difficulty == 'mix':
                 questions = Question.objects(tag=tag).limit(num_of_questions).to_json()
            else:
                questions = Question.objects(tag=tag,difficulty=difficulty).limit(num_of_questions).to_json()
            return Response(questions, mimetype="application/json", status = 200)
        except DoesNotExist:
            raise QuestionNotExistsError
        except Exception:
            raise InternalServerError
