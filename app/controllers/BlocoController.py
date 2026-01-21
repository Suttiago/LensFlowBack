from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.service.BlocoService import BlocoService
from app.dto.BlocoDTO import BlocoCreateDTO, BlocoResponseDTO, BlocoUpdateDTO

router = APIRouter(prefix="/blocos",tags=["Blocos"])
service = BlocoService()

@router.post("/", response_model=BlocoResponseDTO, status_code=status.HTTP_201_CREATED)
def criar_bloco(dto:BlocoCreateDTO, db:Session = Depends(get_db)):
    return service.criar_bloco(db,dto)

@router.get("/listar", response_model=list[BlocoResponseDTO])
def listar_blocos(db: Session = Depends(get_db)):
    return service.listar_todos(db)

@router.get("/{bloco_id}", response_model=BlocoResponseDTO)
def buscar_bloco(bloco_id: int, db:Session = Depends(get_db)):
    try:
        return service.buscar_por_id(db, bloco_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
    
@router.put("/{bloco_id}",response_model=BlocoResponseDTO)
def editar_bloco(bloco_id: int, dto = BlocoUpdateDTO, db: Session = Depends(get_db)):
    try:
        return service.editar_bloco(db, bloco_id, dto)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.delete("/{bloco_id}", status_code=status.HTTP_204_NO_CONTENT)
def excluir_bloco(bloco_id: int, db:Session = Depends(get_db)):
    try:
        service.excluir_bloco(db, bloco_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))