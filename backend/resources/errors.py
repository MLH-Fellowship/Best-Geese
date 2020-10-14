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

# class EmailDoesnotExistsError(Exception):
#     pass

# class BadTokenError(Exception):
#     pass

class UnauthorizedError(Exception):
    pass

class InvalidTagError(Exception):
    pass

class InvalidDifficultyError(Exception):
    pass

class InvalidNumOfQuestionsError(Exception):
    pass

# Step 1 - Error Messages and Printing Error messages if wrong input.

errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status":  HTTPStatus.INTERNAL_SERVER_ERROR
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": HTTPStatus.BAD_REQUEST
     },
     "QuestionAlreadyExistsError": {
         "message": "Question with the same text already exists",
         "status": HTTPStatus.BAD_REQUEST
     },
     "UpdatingQuestionError": {
         "message": "Updating question added by other is forbidden",
         "status": HTTPStatus.FORBIDDEN
     },
     "DeletingMovieError": {
         "message": "Deleting question added by other is forbidden",
         "status": HTTPStatus.BAD_REQUEST
     },
     "QuestionotExistsError": {
         "message": "Question with given id doesn't exists",
         "status": HTTPStatus.BAD_REQUEST
     },
     "EmailAlreadyExistsError": {
         "message": "User with given email address already exists",
         "status": HTTPStatus.BAD_REQUEST
     },
     "UnauthorizedError": {
         "message": "Invalid username or password",
         "status": HTTPStatus.UNAUTHORIZED
     },
    # "EmailDoesnotExistsError" : {
    #     "message" : "Couldn't find the user with given email address",
    #     "status" : HTTPStatus.BAD_REQUEST
    # },
    #  "BadTokenError":{
    #      "message" : "Invalid token",
    #      "status" : HTTPStatus.FORBIDDEN
    #  },
     "InvalidTagError" :{
         "message" : 'Tags parameter is invalid',
         "status": HTTPStatus.BAD_REQUEST 
     },
     "InvalidDifficultyError" : {
         "message" : "Difficulty is invalid",
         "status" : HTTPStatus.BAD_REQUEST        
     },
     "InvalidNumOfQuestionsError" : {
         'message' : 'Number of Questions Parameter is invalid',
         'status' : HTTPStatus.BAD_REQUEST}
}
