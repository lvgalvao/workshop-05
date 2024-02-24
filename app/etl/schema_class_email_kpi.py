import pandera as pa
from pandera.typing import Series

email_regex = r"[^@]+@[^@]+\.[^@]+"

class ProdutoSchemaEmail(pa.SchemaModel):
    id_produto: Series[int] = pa.Field(ge=1, le=20)
    nome: Series[str]
    quantidade: Series[int] = pa.Field(ge=20, le=200)
    preco: Series[float] = pa.Field(ge=5.0, le=120.0)
    categoria: Series[str]
    email: Series[str] = pa.Field(regex=email_regex)

    class Config:
        coerce = True
        strict = True

class ProdutoSchemaEmailKPI(ProdutoSchemaEmail):
    
    # Novas colunas KPIs
    valor_total_estoque: Series[float] = pa.Field(ge=0)  # O valor total em estoque deve ser >= 0
    categoria_normalizada: Series[str]  # Assume-se que a categoria será uma string, não precisa de check específico além de ser uma string
    disponibilidade: Series[bool]  # Disponibilidade é um booleano, então não precisa de check específico
