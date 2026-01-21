from sqlalchemy.orm import Session
from app.models.Bloco import Bloco
from app.dto.BlocoDTO import BlocoCreateDTO, BlocoUpdateDTO

class BlocoRepository:

    def create(self, db: Session, bloco_dto: BlocoCreateDTO) -> Bloco:
        bloco = Bloco(
            tipo = bloco_dto.tipo,
            base = bloco_dto.base,
            espessura = bloco_dto.espessura,
            tamanho = bloco_dto.tamanho,
            grau = bloco_dto.grau,
            indicie = bloco_dto.indicie,
            preco = bloco_dto.preco
        )

        db.add(bloco)
        db.commit()
        db.refresh(bloco)
        return bloco
    
    def buscar_por_id(self, db:Session, Bloco_id:int)-> Bloco | None:
        return db.query(Bloco).filter(Bloco.id == Bloco_id).first()
    
    def listar_tudo(self, db:Session) ->  list[Bloco]:
        return db.query(Bloco).all()
    
    def editar(self, db:Session, bloco: Bloco, dto =BlocoUpdateDTO) -> Bloco:
        
        for field, value in dto.model_dump(exclude_unset=True).items():
            setattr(bloco, field, value)

        db.commit()
        db.refresh(bloco)
        return bloco 

    def excluir(self, db:Session, bloco: Bloco) -> None:
        db.delete(bloco)
        db.commit()