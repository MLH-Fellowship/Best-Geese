from flask import Flask
from http import HTTPStatus
from database.db import initialize_db
from resources.question import questions


app = Flask(__name__)

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


app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/Best-Geese'
}

initialize_db(app)
app.register_blueprint(questions)

@app.route('/')
def hello():
    return {'Hello':'World'}
    
if __name__ == "__main__":
    app.run(debug=True)