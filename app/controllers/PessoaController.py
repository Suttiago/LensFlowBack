from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.service.PessoaService import PessoaService
from app.dto.PessoaDTO import PessoaCreateDTO, PessoaResponseDTO, PessoaUpdateDTO

router = APIRouter(prefix="/pessoas",tags=["Pessoas"])
service = PessoaService()

@router.post("/", response_model=PessoaResponseDTO, status_code=status.HTTP_201_CREATED)
def criar_pessoa(dto:PessoaCreateDTO, db:Session = Depends(get_db)):
    return service.criar_pessoa(db,dto)

@router.get("/listar", response_model=list[PessoaResponseDTO])
def listar_pessoas(db: Session = Depends(get_db)):
    return service.listar_todos(db)

@router.get("/{pessoa_id}", response_model=PessoaResponseDTO)
def buscar_pessoa(pessoa_id: int, db:Session = Depends(get_db)):
    try:
        return service.buscar_por_id(db, pessoa_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
    
@router.put("/{pessoa_id}",response_model=PessoaResponseDTO)
def editar_pessoa(pessoa_id: int, dto = PessoaUpdateDTO, db: Session = Depends(get_db)):
    try:
        return service.editar_pessoa(db, pessoa_id, dto)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.delete("/{pessoa_id}", status_code=status.HTTP_204_NO_CONTENT)
def excluir_pessoa(pessoa_id: int, db:Session = Depends(get_db)):
    try:
        service.excluir_pessoa(db, pessoa_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))