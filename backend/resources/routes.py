from .question import QuestionsApi,QuestionApi


def initialize_routes(api):
    api.add_resource(QuestionsApi,'/api/questions')
    api.add_resource(QuestionApi,'/api/questions/<id>')