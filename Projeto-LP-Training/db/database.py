from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import create_engine
import sqlalchemy.orm
from repository.usuario import UsuariosRepository
from db.config import settings
from fastapi import Depends
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print("Database URL is ",SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# O mecanismo acima cria um objeto adaptado para PostgreSQL, bem como um objeto que estabelecerá um Conexão 


oauth_scheme = OAuth2PasswordBearer(tokenUrl='/user/login')
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
