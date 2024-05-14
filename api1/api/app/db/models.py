from sqlalchemy import Column, Integer,float, String, DateTime
from database import BaseModel
from sqlalchemy.sql import func
#cria o a tabela tarefas

class Pagamento(BaseModel):
    __tablename__ = 'pagamento'
    id = Column('id_pg', Integer, primary_key=True, autoincrement=True)
    valor = Column('valor', float, nullable=False, unique=False)
    forma_pg = Column('forma_pg', String, nullable=False)
    cpf= Column('cpf', Integer , nullable=True)
    produto= Column('produto', String, nullable=False)
    created_at = Column('created_at', DateTime, server_default=func.now())
    updated_at = Column('updated_at', DateTime, onupdate=func.now())




class User(BaseModel):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String, nullable=False, unique=True)
    password = Column('password', String, nullable=False)
    servico = Column('servico',String , nullable=False)
    idade = Column('idade',String, nullable=False)
    created_at = Column('created_at', DateTime, server_default=func.now())
    updated_at = Column('updated_at', DateTime, onupdate=func.now())

#TODO
