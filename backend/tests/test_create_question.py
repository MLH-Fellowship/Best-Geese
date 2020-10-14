#~/best-geese/backend/tests/test_create_question.py

import json
from tests.BaseCase import BaseCase
from http import HTTPStatus

class TestUser(BaseCase):

    def test_successful_login(self):
        # Given
        email = "shayanariyaz@gmail.cm"
        password = "passpasspass"
        user_payload = json.dumps({
            "email" : email,
            "password" : password
        })

        self.app.post('/api/auth/signup',
                    headers={"Content-Type": "application/json"},
                    data=user_payload)
        
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=user_payload)
        login_token = response.json['token']

        question_payload = {
            "tag" : "physics",
            "difficulty" : "hard",
            "question" : "In the standard model, the particle considered to be an elementary particle is a(n)",
            "option_1" : "proton",
            "option_2" : "neutron",
            "option_3" : "electron",
            "option_4" : "alpha particle",
            "correct_answer" : "option_3"
        }

        # When 
        response = self.app.post('/api/questions',
            headers = {"Content-Type": "application/json",
                        "Authorization" : f"Bearer {login_token}"},
            data = json.dumps(question_payload))

        # Then
        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(HTTPStatus.OK,response.status_code)

        