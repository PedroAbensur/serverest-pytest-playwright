from pydantic import BaseModel, Field

class ArrayProduto(BaseModel):
    nome: str
    preco: int
    descricao: str
    quantidade: int
    id: str = Field(..., alias="_id")

class RequestBodyProduto(BaseModel):
    nome: str
    preco: int
    descricao: str
    quantidade: int

class TokenAusenteInvalidoExpirado(BaseModel):
    message: str

class ExisteProdutoComEsseNome(BaseModel):
    message: str

class RotaParaAdministradores(BaseModel):
    message: str