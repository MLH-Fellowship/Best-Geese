from .db import db


class Question(db.Document):
    tag = db.StringField(required=True,unique=True)
    difficulty = db.StringField(required=True,unique=True)
    question = db.StringField(required=True,unique=True)
    option_1 = db.StringField(required=True,unique=True)
    option_2 = db.StringField(required=True,unique=True)
    option_3 = db.StringField(required=True,unique=True)
    option_4 = db.StringField(required=True,unique=True)
    correct_answer = db.StringField(required=True,unique=True)
