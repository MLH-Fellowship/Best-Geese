# backend/app.py

from http import HTTPStatus
from resources.routes import initialize_routes
from resources.errors import errors
from database.db import initialize_db
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask import Flask
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')
CORS(app)
api = Api(app,errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/BestGeese'
}

initialize_db(app)
initialize_routes(api)

@app.route('/')
def hello():
    """
    Dummy Hello Page
    """
    return {'Hello':'World'}

if __name__ == "__main__":
    app.run(port=5000,debug=True)