# backend/resources/question.py

from flask import Response,request
from flask_jwt_extended import jwt_required
from database.models import Question
from flask_restful import Resource
from http import HTTPStatus

from flask_mongoengine import MongoEngine
from mongoengine.queryset import QuerySet
import random

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
        body = request.get_json(force =True)
        question = Question(**body).save()
        id = question.id
        return{'id':str(id)},HTTPStatus.OK


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
        body = request.get_json(force =True)
        Question.objects.get(id=id).update(**body)
        return '',HTTPStatus.OK
    
    @jwt_required
    def delete(self,id):
        """
        Remove a question from the collection.

        Args:
            id (string): Look for question with the specified "id"

        Returns:
            (int): HTTPStatus.OK (200)
        """
        question = Question.objects.get(id=id).delete()
        return '',HTTPStatus.OK

    def get(self,id):
        """
        Get a single question 

        Args:
            id (string): Look for question with the specified "id"
        
        Returns:
            question: As a json response. 

        """
        questions = Question.objects.get(id=id).to_json()
        return Response(questions,
                    mimetype="application/json",
                    status = 200)


class PlayApi(Resource):
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

                 # Step 1 - Error Messages and Printing Error messages if wrong input.
        tag_message = {'error' : 'Tags parameter is invalid'}
        difficulty_message = {'error' : 'Difficulty is invalid'}
        num_of_questions_message = {'error' : 'Number of Questions Parameter is invalid'}

    
        # Parse URL arguments/parameters

        # Tags
        tag = request.args.get('tag',None,str).lower()
        if (tag not in ['biology','physics','chemistry','mathematics','computer science','art']) or (tag is None):
            print('None')
            return tag_message, HTTPStatus.BAD_REQUEST

        # Difficulty
        difficulty = request.args.get('difficulty').lower()
        if (difficulty not in ['easy','medium','hard','mix']) or ( difficulty is None):
            return difficulty_message,HTTPStatus.BAD_REQUEST

        # Number of Questions
        num_of_questions = int(request.args.get('num_of_questions'))
        if (num_of_questions is None) or  ((num_of_questions < 10) or (num_of_questions > 50)) :
            return num_of_questions_message, HTTPStatus.BAD_REQUEST

        if difficulty == 'mix':
            questions = Question.objects(difficulty=difficulty).limit(num_of_questions).to_json()
        
        questions = Question.objects(tag=tag,difficulty=difficulty).limit(num_of_questions).to_json()

        return Response(questions,
                    mimetype="application/json",
                    status = 200)


                    