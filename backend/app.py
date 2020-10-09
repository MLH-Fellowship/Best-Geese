from http import HTTPStatus
from resources.routes import initialize_routes
from database.db import initialize_db
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask import Flask
from flask_jwt_extended import JWTManager

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

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')
api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/BestGeese'
}

initialize_db(app)
initialize_routes(api)

@app.route('/')
def hello():
    return {'Hello':'World'}
    
if __name__ == "__main__":
    app.run(debug=True)