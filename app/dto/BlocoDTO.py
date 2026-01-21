from pydantic import BaseModel, EmailStr
from app.Enums.TipoPessoaEnum import TipoPessoa
from typing import Optional


class BlocoCreateDTO(BaseModel):
    tipo: str
    base: float
    espessura:float
    tamanho: float
    grau: float
    indicie: float
    preco: float


class BlocoResponseDTO(BaseModel):
    id: int
    tipo: str
    base: float
    espessura:float
    tamanho: float
    grau: float
    indicie: float
    preco: float

    class Config:
        orm_mode = True

class BlocoUpdateDTO(BaseModel):
    tipo: Optional[str] = None
    base: Optional[float] = None
    espessura: Optional[float] = None
    tamanho: Optional[float] = None
    grau: Optional[float] = None
    indicie: Optional[float] = None
    preco: Optional[float] = None