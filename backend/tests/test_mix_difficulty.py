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

        question_payload = {
            "tag" : "physics",
            "difficulty" : "hard",
            "question" : "These are light, elementary particles that are not made up of quarks.",
            "option_1" : "Gluons",
            "option_2" : "Leptons",
            "option_3" : "electron",
            "option_4" : "Baryon",
            "correct_answer" : "option_2"
        }

        # When 
        response = self.app.post('/api/questions',
            headers = {"Content-Type": "application/json",
                        "Authorization" : f"Bearer {login_token}"},
            data = json.dumps(question_payload))

        
        question_payload = {
            "tag" : "physics",
            "difficulty" : "hard",
            "question" : "a hadron with one quark and one antiquark",
            "option_1" : "neutron",
            "option_2" : "meson",
            "option_3" : "baryon",
            "option_4" : "electron",
            "correct_answer" : "option_2"
        }

        # When 
        response = self.app.post('/api/questions',
            headers = {"Content-Type": "application/json",
                        "Authorization" : f"Bearer {login_token}"},
            data = json.dumps(question_payload))


        question_payload = {
            "tag" : "physics",
            "difficulty" : "hard",
            "question" : "All baryons are assigned a baryon number of ___, all ﻿﻿anti-baryons are assigned ___, and all non-baryons are ___",
            "option_1" : "-1, +1, 0",
            "option_2" : "-1, 0, +1",
            "option_3" : "+1, -1, 0",
            "option_4" : "0, -1, +1",
            "correct_answer" : "option_3"
        }

        # When 
        response = self.app.post('/api/questions',
            headers = {"Content-Type": "application/json",
                        "Authorization" : f"Bearer {login_token}"},
            data = json.dumps(question_payload))


        question_payload = {
            "tag" : "physics",
            "difficulty" : "hard",
            "question" : "hadron composed of one up quark and two down quarks",
            "option_1" : "neutron",
            "option_2" : "proton",
            "option_3" : "composite particle",
            "option_4" : "baryon number",
            "correct_answer" : "option_1"
        }

        # When 
        response = self.app.post('/api/questions',
            headers = {"Content-Type": "application/json",
                        "Authorization" : f"Bearer {login_token}"},
            data = json.dumps(question_payload))

        
        question_payload = {
            "tag" : "physics",
            "difficulty" : "hard",
            "question" : "Which quarks form a neutron?",
            "option_1" : "up, up, down",
            "option_2" : "down, down, down",
            "option_3" : "up, up, up",
            "option_4" : "up, down, down",
            "correct_answer" : "option_4"
        }

        # When 

        tag = "Physics"
        difficulty = "mix"
        num_of_questions = 10
        response = self.app.get("/api/quiz/" + f"?tag={tag}&difficulty={difficulty}&num_of_questions={num_of_questions}",
            headers = {"Content-Type": "application/json",
                        "Authorization" : f"Bearer {login_token}"})
        
        # # Then
        self.assertEqual(HTTPStatus.OK,response.status_code)
        #self.assertEqual(response.json["error"], "sortBy parameter is invalid")




        
