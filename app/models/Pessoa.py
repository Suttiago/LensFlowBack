from sqlalchemy import Column, Integer, String, Enum
from app.database.database import Base
from app.Enums.TipoPessoaEnum import TipoPessoa

class Pessoa(Base):
    __tablename__ = "pessoa"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    cpf_cnpj = Column(String, unique=True, index=True)
    cidade = Column(String, index=True)
    estado = Column(String, index=True)
    cep = Column(Integer, index=True)
    telefone = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    tipo_pessoa = Column(Enum(TipoPessoa, name="tipo_pessoa"),nullable=False)
