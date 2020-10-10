# backend/resources/errors.py

from http import HTTPStatus


class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class QuestionAlreadyExistsError(Exception):
    pass

class UpdatingQuestionError(Exception):
    pass

class DeletingQuestionError(Exception):
    pass

class QuestionNotExistsError(Exception):
    pass

class EmailAlreadyExistsError(Exception):
    pass

class UnauthorizedError(Exception):
    pass



errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "QuestionAlreadyExistsError": {
         "message": "Question with the same text already exists",
         "status": 400
     },
     "UpdatingQuestionError": {
         "message": "Updating question added by other is forbidden",
         "status": 403
     },
     "DeletingMovieError": {
         "message": "Deleting question added by other is forbidden",
         "status": 403
     },
     "QuestionotExistsError": {
         "message": "Question with given id doesn't exists",
         "status": 400
     },
     "EmailAlreadyExistsError": {
         "message": "User with given email address already exists",
         "status": 400
     },
     "UnauthorizedError": {
         "message": "Invalid username or password",
         "status": 401
     }
}
