from flask_login import UserMixin
import dateitme

from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model.UserMixin):
    '''Users will be able to Register and login.
    They will also get a token that will allow them 
    to make requests'''

    __tablename__ = "users"

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50),unique=True,
                        index = True)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime,default=datetime.now)
    updated_at = db.Column(db.DateTime,onupdate=datetime.now)

    @property # Convert password to a property
    def password(self):
        ''' Prevents access to passwords 
        '''

        raise AttributeError('Password is not a readable attribute.')

    @password.setter
    def password(self,password):
        '''Sets password to a hashed password
        '''
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        ''' Checks if password matches
        '''
        return check_password_hash(self.password_hash,password)

    def generate_auth_token(self,user_id):
        ''' Generates the Auth token and returns
        it .
        '''
        try:
            payload = {
                "exp" : dt.datetime.now() + dt.timedelta(
                    days = 0, seconds = 180000),
                "iat" : dt.datetime.now(),
                "sub" : user_id   
            }
            return jwt.encode(
                payload,
                app.config.get("SECRET_KEY"),
                algorithm="HS256"
            )
        except Exception as e:
            return e
    
    @staticmethod
    def decode_auth_token(auth_token):
        ''' Decodes the auth token
        '''
        try:
            payload = jwt.decode(auth_token,app.config.get('SECRET_KEY'),
                                options ={'verify_iat' : False})
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            return "Signature expired. Please log in again."
        except jwt.InvalidTokenError:
            return "Invalid Token. Please log in again."

    def __repr__(self):
        return f"<User: {self.username}>"

    # Set up user loader
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))