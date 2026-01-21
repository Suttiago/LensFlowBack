from enum import Enum

class TipoPessoa(str,Enum):
    ADMINISTRADOR = "ADMINISTRADOR"
    FUNCIONARIO = "FUNCIONARIO"
    CLIENTE = "CLIENTE"
    FORNECEDOR = "FORNECEDOR"