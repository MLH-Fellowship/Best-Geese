#~/best-geese/backend/tests/test_login.py


import json
from tests.BaseCase import BaseCase
from http import HTTPStatus

class TestUserLogin(BaseCase):

    def test_successful_login(self):

        # Given 
        email = "shayanariyaz@gmail.com"
        password = "passpasspass"
        payload = json.dumps({
            "email" : email,
            "password" : password
        })

        response = self.app.post('/api/auth/signup',
                                headers = {"Content-Type" : "application/json"},
                                data = payload)
        
        # When 
        response = self.app.post('/api/auth/login',
                                headers = {"Content-Type" : "application/json"},
                                data = payload)

        # Then
        self.assertEqual(str, type(response.json['token']))
        self.assertEqual(HTTPStatus.OK,response.status_code)


