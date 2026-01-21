from sqlalchemy import Column, Integer, String, Enum, Float
from app.database.database import Base

class Bloco(Base):
    __tablename__ = "bloco"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, index=True)
    base = Column(Float, index=True)
    espessura = Column(Float, index=True)
    tamanho = Column(Float, index=True)
    grau = Column(Float, index=True)
    indicie = Column(Float, index=True)
    preco = Column(Float, index=True)