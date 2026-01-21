from sqlalchemy.orm import Session
from app.repository.PessoaRepository import PessoaRepository
from app.dto.PessoaDTO import PessoaCreateDTO, PessoaUpdateDTO
from app.models.Pessoa import Pessoa

class PessoaService:
    def __init__(self):
        self.repository = PessoaRepository()

    def criar_pessoa(self, db: Session, dto: PessoaCreateDTO) -> Pessoa:
        return self.repository.create(db,dto)
    
    def listar_todos (self, db: Session) -> Pessoa:
        return self.repository.listar_tudo(db)
    
    def buscar_por_id(self, db: Session, pessoa_id: int) -> Pessoa:
        return self.repository.buscar_por_id(db,pessoa_id)
        if not pessoa:
            raise ValueError("Pessoa não encontrada")
        return pessoa
    
    def editar_pessoa(self, db: Session, pessoa_id: int, dto: PessoaUpdateDTO) -> Pessoa:
        pessoa = self.buscar_por_id(db, pessoa_id)
        return self.repository.update(db, pessoa, dto)
    
    def excluir_pessoa(self, db: Session, pessoa_id: int):
        pessoa = self.buscar_por_id(db, pessoa_id)
        return self.repository.excluir(db, pessoa)