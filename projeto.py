from datetime import date
from typing import Optional

from pydantic import BaseModel


class Cliente(BaseModel):
    nome: str
    sobrenome: str
    email: str
    telefone: Optional[str] = None
    data_de_cadastro: date
    categoria: str
    empresa: Optional[str] = None
    endereco: Optional[str] = None
    is_ativo: bool = True
    id_cliente: str

# Dados para teste de deserialização e serialização do modelo
data_cliente = {
    "nome": "João",
    "sobrenome": "Silva",
    "email": "joao.silva@example.com",
    "data_de_cadastro": "2023-02-01",
    "categoria": "Cliente",
    "id_cliente": "123456789"
}

cliente = Cliente(**data_cliente)

print(cliente)

data_cliente_esperado = {
    'nome': 'João',
    'sobrenome': 'Silva',
    'email': 'joao.silva@example.com',
    'telefone': None,
    'data_de_cadastro': date(2023, 2, 1),
    'categoria': 'Cliente',
    'empresa': None,
    'endereco': None,
    'is_ativo': True,
    'id_cliente': '123456789',
}

assert cliente.dict() == data_cliente_esperado