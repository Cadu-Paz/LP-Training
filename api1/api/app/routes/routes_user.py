from fastapi import  APIRouter, FastAPI, Depends, HTTPException, status, Response

from  database import engine,SessionLocal, BaseModel
from schema import UserSchema
from sqlalchemy.orm import Session
from models import User 




BaseModel.metadata.create_all(bind=engine)
router = APIRouter(prefix='/users')


def get_db():
    try:
        db = SessionLocal()
        #TODO 
        yield db
    finally:
        db.close()




@router.post("/add")
async def add_user(request:UserSchema, db: Session = Depends(get_db)):
    user_on_db = User(id=request.id, username=request.username, password=request.password)
    db.add(user_on_db)
    db.commit()
    db.refresh(user_on_db)
    return user_on_db

@router.get("/{user_name}", description="Listar o usuario pelo nome")
def get_users(user_name,db: Session = Depends(get_db)):
    user_on_db= db.query(User).filter(User.username == user_name).first()
    return user_on_db

@router.get("/listar", description="Listar todos usuarios")
def get_users_all(db: Session = Depends(get_db)):
    users= db.query(User).a
    return users

@router.delete("/{id}", description="Deletar o usuario pelo id")
def delete_usuario(id: int, db: Session = Depends(get_db)):
    user_on_db = db.query(User).filter(User.id == id).first()
    if user_on_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Sem usuario com este id')
    db.delete(user_on_db)
    db.commit()
    return f"Banco with id {id} deletado.", Response(status_code=status.HTTP_200_OK)

@router.put("/{id}", )
async def update_todo(id: int, users = User, body: dict) -> dict:
    user_on_db = db.query(User).filter(users.id == id).first()
    for todo in users:
        if int(todo["id"]) == id:
            todo["username"] = body["username"]
            return {
                 "data": f"Todo with id {id} has been updated."
             }

    return {
         "data": f"Todo with id {id} not found."
     }

@app.put("/produto/{id}",response_model=User)
async def update_produto(request:UserSchema, id: int, db: Session = Depends(get_db)):
     produto_on_db = db.query(User).filter(User.id == id).first()
     print(produto_on_db)
     if produto_on_db is None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Sem usuario com este id')
     produto_on_db = User(id=request.id, item=request.item, peso=request.peso, numero_caixas=request.numero_caixas)
     db.up
     db(user_on_db)
     db.commit()
     db.refresh(produto_on_db)
     return produto_on_db, Response(status_code=status.HTTP_204_NO_CONTENT)


router = APIRouter()
