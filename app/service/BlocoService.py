from sqlalchemy.orm import Session
from app.repository.BlocoRepository import BlocoRepository
from app.dto.BlocoDTO import BlocoCreateDTO, BlocoUpdateDTO
from app.models.Bloco import Bloco

class BlocoService:
    def __init__(self):
        self.repository = BlocoRepository()

    def criar_bloco(self, db: Session, dto: BlocoCreateDTO) -> Bloco:
        return self.repository.create(db,dto)
    
    def listar_todos (self, db: Session) -> Bloco:
        return self.repository.listar_tudo(db)
    
    def buscar_por_id(self, db: Session, bloco_id: int) -> Bloco:
        return self.repository.buscar_por_id(db,bloco_id)
        if not bloco:
            raise ValueError("Bloco não encontrado")
        return bloco
    
    def editar_bloco(self, db: Session, bloco_id: int, dto: BlocoUpdateDTO) -> Bloco:
        bloco = self.buscar_por_id(db, bloco_id)
        return self.repository.update(db, bloco, dto)
    
    def excluir_bloco(self, db: Session, bloco_id: int):
        bloco = self.buscar_por_id(db, bloco_id)
        return self.repository.excluir(db, bloco)