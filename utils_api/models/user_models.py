from pydantic import BaseModel, Field

class RequestBodyUsuarios(BaseModel):
    nome: str
    email: str
    password: str
    administrador: str

class CadastroComSucesso(BaseModel):
    message: str
    id: str = Field(..., alias="_id")

class ErrorEmailJaUtilizado(BaseModel):
    message: str

class AlteradoComSucesso(BaseModel):
    message: str
