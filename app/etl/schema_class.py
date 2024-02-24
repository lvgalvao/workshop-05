import pandera as pa
from pandera.typing import DataFrame, Series

email_regex = r"[^@]+@[^@]+\.[^@]+"

class ProdutoSchema(pa.SchemaModel):
    id_produto: Series[int] = pa.Field(ge=1, le=20)
    nome: Series[str]
    quantidade: Series[int] = pa.Field(ge=20, le=200)
    preco: Series[float] = pa.Field(ge=5.0, le=120.0)
    categoria: Series[str]

    class Config:
        coerce = True
        # strict = True