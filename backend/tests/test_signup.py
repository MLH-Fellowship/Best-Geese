# ~best-geese/backend/tests/test_signup.py

import unittest
import json
from app import app
from database.db import db

from tests.BaseCase import BaseCase
from http import HTTPStatus

class SignupTest(BaseCase):

    def test_successful_signup(self):
        # Given
        payload = json.dumps({
            "email" : "shayanariyaz@gmail.com",
            "password": "passpasspass"
        })

        # When 
        response = self.app.post('/api/auth/signup',
                                 headers = {"Content-Type":"application/json"},
                                 data = payload)

        # Then 
        self.assertEqual(str,type(response.json['id']))
        self.assertEqual(HTTPStatus.OK,response.status_code)
