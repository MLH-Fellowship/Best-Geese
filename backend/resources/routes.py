# backend/resources/routes.py

from .question import QuestionsApi,QuestionApi
from .auth import SignupApi, LoginApi
from .quiz import QuizApi
from .ai_generate import GenerateAIQuestion

def initialize_routes(api):

    api.add_resource(QuestionsApi,'/api/questions')
    api.add_resource(QuestionApi,'/api/questions/<id>')
    

    api.add_resource(SignupApi,'/api/auth/signup')
    api.add_resource(LoginApi,'/api/auth/login')

    api.add_resource(QuizApi,'/api/quiz/')

    api.add_resource(GenerateAIQuestion,'/api/generate')