#!flask/bin/python
from flask import Flask,jsonify,request
from pymongo import MongoClient
from http import HTTPStatus

app = Flask(__name__)

client = MongoClient("mongodb://127.0.0.1:27017") # host uri 
db = client.mymongodb # Select the database
question_collection = db.question # Sellect the collection name
initial_questions = [question for question in question_collection.find()]


if (len(initial_questions)) == 0:
    question_collection.insert({
      "id" : 1,
      "tag" : "biology",
      "difficulty" : "easy",
      "question" : "What is respiration?",
      "option_1" : "breathing",
      "option_2" : "singing",
      "option_3" : "sleeping",
      "option_4" : "eating",
      "correct_answer " : "option_1",
    })
    question_collection.insert({
      "id" : 2,
      "tag" : "biology",
      "difficulty" : "easy",
      "question" : "What are enzymes?",
      "option_1" : "fiction",
      "option_2" : "micro-organisms",
      "option_3" : "the answer to everything",
      "option_4" : "moleculular structures",
      "correct_answer " : "option_2",
    })

@app.route('/api/questions',methods=['GET'])
def get_guestions():
    get_questions = question_collection.find()
    question_list = []
    for question in get_questions:
        question_list.append({"tag" : question['tag'],
                            "difficulty" :question['difficulty'],
                            "question" :question['question'],
                            "option_1" :question['option_1'],
                            "option_2" :question['option_2'],
                            "option_3" :question['option_3'],
                            "option_4" : question['option_4'],
                            "correct_answer":question["correct_answer"],
                            "id" : question['id']
        })
    return jsonify({'questions': question_list})


@app.route('/api/create-question',methods = ['GET'])
def create_question():
    # questions.append({
    #   "id" : len(questions),
    #   "tag" : "physics",
    #   "difficulty" : "medium",
    #   "question" : "What is the strongest substance in the universe?",
    #   "option_1" : "anti-matter",
    #   "option_2" : "dark-matter",
    #   "option_3" : "protons",
    #   "option_4" : "nuclear pasta",
    #   "correct_answer " : "option_4"
	# })
    questions = question_collection.find()
    new_question = {"id":questions.count(),
                    "tag" : "math",
                            "difficulty" :'hard',
                            "question" :"In reality c in e = mc^2 means? ",
                            "option_1" :'speed of light',
                            "option_2" :'speed of continuity',
                            "option_3" :'causation energy',
                            "option_4" : 'speed of causation',
                            "correct_answer":"option_4",
                     }
    question_collection.insert(new_question)
    all_questions = question_collection.find()
    question_list = []
    for question in all_questions:
        question_list.append({"tag" : question['tag'],
                            "difficulty" :question['difficulty'],
                            "question" :question['question'],
                            "option_1" :question['option_1'],
                            "option_2" :question['option_2'],
                            "option_3" :question['option_3'],
                            "option_4" : question['option_4'],
                            "correct_answer":question['correct_answer'],
                            "id" : question['id']
        })
    return jsonify({'questions': question_list})

@app.route('/api/questions/<int:question_id>',methods=['GET'])
def get_question(question_id):
    question =  question_collection.find({'id': question_id})
    if question.count() == 0:
        return jsonify({'question': None})
    return jsonify({'question': question})#,HTTPStatus.OK

@app.route('/api/questions/<int:question_id>',methods=['DELETE'])
def delete_question(question_id):
    question =  question_collection.find({'id': question_id})
    if question.count() == 0:
        return jsonify({'question': None})

    question_collection.remove({question})

    return {},HTTPStatus.NO_CONTENT

if __name__ == '__main__':
    app.run(debug=True)