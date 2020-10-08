#!flask/bin/python
from flask import Flask,jsonify

app = Flask(__name__)

questions = [
    {
      "id" : 1,
      "tag" : "biology",
      "difficulty" : "easy",
      "question" : "What is respiration?",
      "option_1" : "breathing",
      "option_2" : "singing",
      "option_3" : "sleeping",
      "option_4" : "eating",
      "correct_answer " : "option_1"
    }, {
      "id" : 2,
      "tag" : "biology",
      "difficulty" : "easy",
      "question" : "What are enzymes?",
      "option_1" : "fiction",
      "option_2" : "micro-organisms",
      "option_3" : "the answer to everything",
      "option_4" : "moleculular structures",
      "correct_answer " : "option_2"
	}
]

@app.route('/BestGeese/api/v1.0/questions',methods=['GET'])
def get_guestions():
    return jsonify({'questions': questions})


@app.route('/BestGeese/api/v1.0/create-question',methods = ['GET'])
def create_question():
    questions.append({
      "id" : len(questions),
      "tag" : "physics",
      "difficulty" : "medium",
      "question" : "What is the strongest substance in the universe?",
      "option_1" : "anti-matter",
      "option_2" : "dark-matter",
      "option_3" : "protons",
      "option_4" : "nuclear pasta",
      "correct_answer " : "option_4"
	})

@app.route('/BestGeese/api/v1.0/questions/<int:question_id>',methods=['GET'])
def get_question(question_id):
    question = [question for question in questions if question['id'] == question_id]
    if len(question) == 0:
        abort(404)
    return jsonify({'question': question[0]})

if __name__ == '__main__':
    app.run(debug=True)