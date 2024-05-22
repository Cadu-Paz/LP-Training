from typing import Union

from fastapi import FastAPI , Form
from pydantic import BaseModel
 

app = FastAPI()

class Item(BaseModel):
    name: str
    email: str
    senha: int

@app.get("/")
def read_root():
    return {"Bem-Vindo": "LP-Tranning"}


@app.post("/login/")
def login(nome: str = Form(),email:str= Form(), senha:str = Form()):
    return {"nome": nome, "email":email, "senha": senha}

@app.put("/usuarios/{login}")
def update_login(nome: str = Form(), email:str= Form(),senha:str= Form() ):
    return {"nome": nome, "email":email,"senha": senha }

@app.get("/usuarios/{cadastro}")
def user_name(nome: str,email:str,idade:int,altura:float,peso:float,objetivo:str,obs:str):
    return {"nome": nome, "email":email,"idade":idade,"altura":altura,"peso":peso,"objetivo":objetivo,"obs":obs}


@app.post("/cadastro/")
def login(nome: str = Form(),email:str= Form(), idade:int = Form(),altura:float= Form(),peso:float= Form(),objetivo:str= Form(),obs:str= Form()):
    return {"nome": nome, "email":email, "idade":idade,"altura": altura, "peso": peso, "objetivo":objetivo,"obs":obs}

@app.put("/usuarios/{cadastro}")
def update_login(email:str= Form(),altura:float= Form(),peso:float= Form(),objetivo:str= Form(),obs:str= Form()):
    return {"email":email, "altura":altura,"peso": peso , "objetivo":objetivo, "obs":obs }