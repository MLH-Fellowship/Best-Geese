# backend/resources/auth.py

from flask import request,Response
from flask_jwt_extended import create_access_token
from database.models import User
from flask_restful import Resource
from http import HTTPStatus
import datetime

class SignupApi(Resource):
    def post(self):
        body = request.get_json(force=True)
        user = User(**body)
        user.hash_password()
        user.save()
        id = user.id
        return {'id':str(id)},HTTPStatus.OK


class LoginApi(Resource):
    def post(self):
        body = request.get_json()
        user = User.objects.get(email=body.get('email'))
        authorized = user.check_password(body.get('password'))
        if not authorized:
            return {'error':'Email or password invalid'},HTTPStatus.UNAUTHORIZED
        
        expires = datetime.timedelta(days=7)
        access_token = create_access_token(identity =str(user.id),expires_delta=expires)
        return {'token':access_token},HTTPStatus.OK