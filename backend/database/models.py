from .db import db
from flask.ext.bycrypt import Bycrypt

class Question(db.Document):
    tag = db.StringField(required=True)
    difficulty = db.StringField(required=True)
    question = db.StringField(required=True,unique=True)
    option_1 = db.StringField(required=True)
    option_2 = db.StringField(required=True)
    option_3 = db.StringField(required=True)
    option_4 = db.StringField(required=True)
    correct_answer = db.StringField(required=True)


class User(db.Document):
    email = db.EmailField(required=True,unique=True)
    password = db.StringField(required=True,min_length=6)