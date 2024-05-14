from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    username: str
    password: str 
    servico: str
    idade: int


class PagamentoSchema(BaseModel):
    id_pg: int
    valor: float
    forma_pg: str 
    cpf: int
    produto: str 

#arquivo 3