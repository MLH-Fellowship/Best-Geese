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



        body_payload = {

        "text" : "In the 17th century, Isaac Newton and Gottfried Leibniz independently developed the foundations for calculus. Calculus development went through three periods: anticipation, development and rigorization. In the anticipation stage, mathematicians were attempting to use techniques that involved infinite processes to find areas under curves or maximize certain qualities. In the development stage, Newton and Leibniz brought these techniques together through the derivative and integral. Though their methods were not always logically sound, mathematicians in the 18th century took on the rigorization stage, and were able to justify them and create the final stage of calculus. Today, we define the derivative and integral in terms of limits. In contrast to calculus, which is a type of continuous mathematics, other mathematicians have taken a more theoretical approach. Discrete mathematics is the branch of math that deals with objects that can assume only distinct, separated value. Discrete objects can be characterized by integers, whereas continuous objects require real numbers. Discrete mathematics is the mathematical language of computer science, as it includes the study of algorithms. Fields of discrete mathematics include combinatorics, graph theory, and the theory of computation. People often wonder what relevance mathematicians serve today. In a modern world, math such as applied mathematics is not only relevant, it's crucial. Applied mathematics is the branches of mathematics that are involved in the study of the physical, biological, or sociological world. The idea of applied math is to create a group of methods that solve problems in science. Modern areas of applied math include mathematical physics, mathematical biology, control theory, aerospace engineering, and math finance. Not only does applied math solve problems, but it also discovers new problems or develops new engineering disciplines. Applied mathematicians require expertise in many areas of math and science, physical intuition, common sense, and collaboration. The common approach in applied math is to build a mathematical model of a phenomenon, solve the model, and develop recommendations for performance improvement. While not necessarily an opposite to applied mathematics, pure mathematics is driven by abstract problems, rather than real world problems. Much of what's pursued by pure mathematicians can have their roots in concrete physical problems, but a deeper understanding of these phenomena brings about problems and technicalities. These abstract problems and technicalities are what pure mathematics attempts to solve, and these attempts have led to major discoveries for mankind, including the Universal Turing Machine, theorized by Alan Turing in 1937. The Universal Turing Machine, which began as an abstract idea, later laid the groundwork for the development of the modern computer. Pure mathematics is abstract and based in theory, and is thus not constrained by the limitations of the physical world.",
        "tag" : "mathematics",
        "difficulty": "medium",
        "num_of_questions" : 4
        }
        # When 
        response = self.app.post('/api/generate',
            headers = {"Content-Type": "application/json",
                        "Authorization" : f"Bearer {login_token}"},
            data = json.dumps(body_payload))
        
        # # Then
        self.assertEqual(HTTPStatus.OK,response.status_code)
        #self.assertEqual(response.json["error"], "sortBy parameter is invalid")




        
