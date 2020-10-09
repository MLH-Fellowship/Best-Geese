from .db import db
from flask_bcrypt import generate_password_hash,check_password_hash
import mongoengine_goodjson as gj

class Question(gj.Document):
    tag = db.StringField(required=True)
    difficulty = db.StringField(required=True)
    question = db.StringField(required=True,unique=True)
    option_1 = db.StringField(required=True)
    option_2 = db.StringField(required=True)
    option_3 = db.StringField(required=True)
    option_4 = db.StringField(required=True)
    correct_answer = db.StringField(required=True)


class User(gj.Document):
    email = db.EmailField(required=True,unique=True)
    password = db.StringField(required=True,min_length=6)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self,password):
        return check_password_hash(self.password,password)

