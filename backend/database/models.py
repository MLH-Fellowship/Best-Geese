# backend/database/models.py

from .db import db
from flask_bcrypt import generate_password_hash,check_password_hash
import mongoengine_goodjson as gj # To get a clean json id tag instead of MongoDB style.


class Question(gj.Document):
    
    """    
    Skeleton:

    questions = [
        {
        "tag" : "biology",
        "difficulty" : "easy",
        "question" : "What is respiration?",
        "option_1" : "breathing",
        "option_2" : "singing",
        "option_3" : "sleeping",
        "option_4" : "eating",
        "correct_answer " : "option_1"
        },
    ]

    parameters:
    tag  :  Subjects ( e.g Biology, Chemistry, Physics)
    difficulty : Easy, Medium, Hard, Mix
    question : Unique Id
    
    """
    tag = db.StringField(required=True)                  
    difficulty = db.StringField(required=True)           
    question = db.StringField(required=True,unique=True) # Question (Unique Id)
    option_1 = db.StringField(required=True)
    option_2 = db.StringField(required=True)
    option_3 = db.StringField(required=True)
    option_4 = db.StringField(required=True)
    correct_answer = db.StringField(required=True)


class User(gj.Document):
    """
    users = [
        {
            "email" : "name@server.com",
            "password": "**********"
        }
    ]
    """

    email = db.EmailField(required=True,unique=True)
    password = db.StringField(required=True,min_length=6)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self,password):
        return check_password_hash(self.password,password)

# class UserStats(User):
#     number_of_games_played = db.IntField(default=0),
#     number_of_games_won = db.IntField(default=0),
#     number_of_games_list = db.IntField(default=0)


class QuestionText(gj.Document):
    text = db.StringField(required=True)
    tag = db.StringField(required=True)
    difficulty = db.StringField(required=True)
    num_of_questions = db.IntField(required = True)
