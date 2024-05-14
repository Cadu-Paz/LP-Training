from fastapi import  APIRouter, FastAPI, Depends, HTTPException, status, Response

from  database import engine,SessionLocal, BaseModel
from schema import PagamentoSchema
from sqlalchemy.orm import Session
from models import Pagamento 




BaseModel.metadata.create_all(bind=engine)
router = APIRouter(prefix='/pagamento')


def get_db():
    try:
        db = SessionLocal()
        #TODO 
        yield db
    finally:
        db.close()




@router.post("/add")
async def add_pagamento(request:PagamentoSchema, db: Session = Depends(get_db)):
    pagamento_on_db = Pagamento(id_pg=request.id_pg, valor=request.valor, cpf=request.cpf, produto=request.produto)
    db.add(pagamento_on_db)
    db.commit()
    db.refresh(pagamento_on_db)
    return pagamento_on_db

@router.get("/{produto}", description="Listar o produto pelo nome")
def get_pagamentos(produto,db: Session = Depends(get_db)):
    pagamento_on_db= db.query(Pagamento).filter(Pagamento.produto == produto).first()
    return pagamento_on_db

@router.get("/listar", description="Listar todos pagamentos")
def get_pagamentos_all(db: Session = Depends(get_db)):
    pagamentos= db.query(Pagamento).a
    return pagamentos

@router.delete("/{id_pg}", description="Deletar o usuario pelo id_pg")
def delete_pagamento(id: int, db: Session = Depends(get_db)):
    pagamento_on_db = db.query(Pagamento).filter(Pagamento.id_pg == id).first()
    if pagamento_on_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Sem pagamento com este id')
    db.delete(pagamento_on_db)
    db.commit()
    return f"Banco with id {id} deletado.", Response(status_code=status.HTTP_200_OK)



