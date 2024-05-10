from fastapi import  APIRouter, FastAPI, Depends, HTTPException, status, Response

from  database import engine,SessionLocal, Base
from schema import ProdutosSchema
from sqlalchemy.orm import Session
from models import Produtos

#cria a tabela
Base.metadata.create_all(bind=engine)
router = APIRouter(prefix="/produtos")   

def get_db():
    try:
        db = SessionLocal()
        #TODO 
        yield db
    finally:
        db.close()




@router.post("/add")
async def add_produto(request:ProdutosSchema, db: Session = Depends(get_db)):
    produto_on_db = Produtos(id=request.id, item=request.item, peso=request.peso, numero_caixas=request.numero_caixas)
    db.add(produto_on_db)
    db.commit()
    db.refresh(produto_on_db)
    return produto_on_db

@router.get("/{produto_name}", description="Listar o produto pelo nome")
def get_produtos(produto_name,db: Session = Depends(get_db)):
    produto_on_db= db.query(Produtos).filter(Produtos.item == produto_name).first()
    return produto_on_db

@router.get("/listar", description="Listar todos produtos")
def get_produtos_all(db: Session = Depends(get_db)):
    produtos= db.query(Produtos).a
    return produtos

@router.delete("/{id}", description="Deletar o produto pelo id")
def delete_produto(id: int, db: Session = Depends(get_db)):
    produto_on_db = db.query(Produtos).filter(Produtos.id == id).first()
    if produto_on_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Sem produto com este id')
    db.delete(produto_on_db)
    db.commit()
    return f"Banco with id {id} deletado.", Response(status_code=status.HTTP_200_OK)

# @app.put("/produto/{id}",response_model=Produtos)
# async def update_produto(request:ProdutosSchema, id: int, db: Session = Depends(get_db)):
#     produto_on_db = db.query(Produtos).filter(Produtos.id == id).first()
#     print(produto_on_db)
#     if produto_on_db is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Sem produto com este id')
#     produto_on_db = Produtos(id=request.id, item=request.item, peso=request.peso, numero_caixas=request.numero_caixas)
#     db.up
#     db.(produto_on_db)
#     db.commit()
#     db.refresh(produto_on_db)
#     return produto_on_db, Response(status_code=status.HTTP_204_NO_CONTENT)


# router = APIRouter()