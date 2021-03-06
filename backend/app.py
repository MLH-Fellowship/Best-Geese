# backend/app.py

from http import HTTPStatus

from resources.errors import errors
from database.db import initialize_db
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask import Flask
from flask_jwt_extended import JWTManager
#from flask_mail import Mail


app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')


# imports requiring app and mail
from resources.routes import initialize_routes
#api = Api(app)
CORS(app)
api = Api(app,errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)



app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/BestGeese'
}

# MONGODB_SETTINGS = {
 #    'host': 'mongodb://localhost/best-geese'
# }

initialize_db(app)
initialize_routes(api)


@app.route('/')
def hello():
    """
    Dummy Hello Page
    """
    return {'Hello':'World'}

