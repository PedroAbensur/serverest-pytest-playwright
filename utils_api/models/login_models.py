from pydantic import BaseModel

class RequestBodyLogin(BaseModel):
    email: str
    password: str

class LoginComSucesso(BaseModel):
    message: str
    authorization: str

class ErrorEmailSenhaInvalidos(BaseModel):
    message: str
