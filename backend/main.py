import helper
import json
from flask import Flask,request,Response

app= Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/quiz/new', methods=['POST'])
def add_quiz():
    # Get quiz from the POST body
    req_data = request.get_json()
    quiz = req_data['quiz']

    # Add quiz to the list
    res_data = helper.add_quiz_to_list(quiz)

    # Return error if item not added
    if res_data is None:
        response = Response("{'error': 'Quiz not added - " + quiz + "'}",
        status = 400,
        mimetype = 'application/json')
        return response


    response = Response(json.dumps(res_data), mimetype='application/json')
    return response

@app.route('/quizzes/all')
def get_all_quizzes():

    # Get items from the helper
    res_data = helper.get_all_quizzes()

    # Return response
    response = Response(json.dumps(res_data),
                        mimetype='application/json')
    return response

@app.route('/quiz/status',methods=['GET'])
def get_quiz():
    # Get parameter from the URL
    quiz_number = request.args.get('name')

    # Get items from the helper
    status = helper.get_quiz(quiz_number)

    # Return 404 if item not found
    if status is None:
        response = Response("{'error' : 'Quiz Not Found - %s'}" % quiz_number,
            status = 404,
            mimetype='application/json')
        return response

    # Return status
    res_data = {
        'status' : status
    }

    response = Response(json.dumps(res_data),status = 200,
    mimetype = 'application/json')
    return response

def update_quiz_status(quiz,status):
    # Check if the passed status is a valid value
    if (status.lower().strip() == 'not started'):
        status = NONSTARTED
    elif (status.lower().strip() == ' in progress'):
        status = INPROGRESS
    elif (status.lower().strip() == 'completed'):
        status = COMPLETED 
    else:
        print("Invalid Status: " + status)
        return None
    
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('update items set status=? where quiz=?',(status,quiz))
        conn.commit()
        return {quiz:status}
    except EXCEPTION as e:
        print('ErrorL ',e)
        return None
        
if "__main__" == __name__:
    app.run(port=5000,debug=True)