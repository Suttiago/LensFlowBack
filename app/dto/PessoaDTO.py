from pydantic import BaseModel, EmailStr
from app.Enums.TipoPessoaEnum import TipoPessoa
from typing import Optional


class PessoaCreateDTO(BaseModel):
    nome: str
    email: EmailStr
    cpf_cnpj:str
    cidade: str
    estado: str
    cep: int
    telefone: str
    tipo_pessoa: TipoPessoa 

class PessoaResponseDTO(BaseModel):
    id: int
    nome: str
    email: EmailStr
    cpf_cnpj:str
    cidade: str
    estado: str
    cep: int
    telefone: str
    tipo_pessoa: TipoPessoa

    class Config:
        orm_mode = True

class PessoaUpdateDTO(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    cpf_cnpj: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None
    cep: Optional[int] = None
    telefone: Optional[str] = None
    tipo_pessoa: Optional[TipoPessoa] = None