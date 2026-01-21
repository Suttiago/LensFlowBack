from sqlalchemy.orm import Session
from app.models.Pessoa import Pessoa
from app.dto.PessoaDTO import PessoaCreateDTO, PessoaUpdateDTO

class PessoaRepository:

    def create(self, db: Session, pessoa_dto: PessoaCreateDTO) -> Pessoa:
        pessoa = Pessoa(
            nome=pessoa_dto.nome,
            email=pessoa_dto.email,
            cpf_cnpj=pessoa_dto.cpf_cnpj,
            cidade=pessoa_dto.cidade,
            estado=pessoa_dto.estado,
            cep=pessoa_dto.cep,
            telefone=pessoa_dto.telefone,
            tipo_pessoa=pessoa_dto.tipo_pessoa
        )

        db.add(pessoa)
        db.commit()
        db.refresh(pessoa)
        return pessoa
    
    def buscar_por_id(self, db:Session, pessoa_id:int)-> Pessoa | None:
        return db.query(Pessoa).filter(Pessoa.id == pessoa_id).first()
    
    def listar_tudo(self, db:Session) ->  list[Pessoa]:
        return db.query(Pessoa).all()
    
    def editar(self, db:Session, pessoa: Pessoa, dto =PessoaUpdateDTO) -> Pessoa:
        
        for field, value in dto.model_dump(exclude_unset=True).items():
            setattr(pessoa, field, value)

        db.commit()
        db.refresh(pessoa)
        return pessoa 

    def excluir(self, db:Session, pessoa: Pessoa) -> None:
        db.delete(pessoa)
        db.commit()