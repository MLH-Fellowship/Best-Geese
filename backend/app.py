# backend/app.py

from http import HTTPStatus

from resources.errors import errors
from database.db import initialize_db
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask import Flask
from flask_jwt_extended import JWTManager
#from flask_mail import Mail


app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')
#mail = Main(app)

# imports requiring app and mail
from resources.routes import initialize_routes
#api = Api(app)
api = Api(app,errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)



app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/BestGeese'
}

# MONGODB_SETTINGS = {
#     'host': 'mongodb://localhost/movie-bag'
# }

initialize_db(app)
initialize_routes(api)


@app.route('/')
def hello():
    """
    Dummy Hello Page
    """
    return {'Hello':'World'}

