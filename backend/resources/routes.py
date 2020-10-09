from .question import QuestionsApi,QuestionApi
from .auth import SignupApi, LoginApi

def initialize_routes(api):
    api.add_resource(QuestionsApi,'/api/questions')
    api.add_resource(QuestionApi,'/api/questions/<id>')



    api.add_resource(SignupApi,'/api/auth/signup')
    api.add_resource(LoginApi,'/api/auth/login')