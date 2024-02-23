from pydantic import BaseModel
from typing import Optional, Union

# O campo só é optional caso tenha o valor default

class Produto(BaseModel):
    id: int  # Campo obrigatório
    nome: str | None # Campo pode ser None
    descricao: Union[str, None] # Campo pode ser None
    preco: float  # Campo obrigatório
    estoque: int = 0  # Campo opcional com valor padrão
    categoria: Optional[str]  # Campo pode ser None

# Instância válida: todos os campos obrigatórios estão presentes
produto_01 = Produto(id=1, nome="Teclado Mecânico", preco=200.0)

# Instância válida: inclui dados opcionais
produto_02 = Produto(id=2, nome="Mouse Gamer", descricao="Mouse com DPI ajustável", preco=150.0, estoque=10, categoria="Periféricos")

# Tentativa de instância sem todos os campos obrigatórios resultará em erro
# produto_03 = Produto(nome="Monitor")