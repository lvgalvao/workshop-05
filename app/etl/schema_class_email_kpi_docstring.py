import pandera as pa
from pandera.typing import Series

email_regex = r"[^@]+@[^@]+\.[^@]+"

class ProdutoSchemaEmail(pa.SchemaModel):
    """
    Define o esquema para a validação de dados de produtos com Pandera.
    
    Este esquema inclui campos básicos para produtos, incluindo um campo de e-mail
    validado por uma expressão regular.

    Attributes:
        id_produto (Series[int]): Identificador do produto, deve estar entre 1 e 20.
        nome (Series[str]): Nome do produto.
        quantidade (Series[int]): Quantidade disponível do produto, deve estar entre 20 e 200.
        preco (Series[float]): Preço do produto, deve estar entre 5.0 e 120.0.
        categoria (Series[str]): Categoria do produto.
        email (Series[str]): E-mail associado ao produto, deve seguir o formato padrão de e-mails.
    """
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
    """
    Estende o esquema ProdutoSchemaEmail para incluir KPIs (Indicadores-chave de Desempenho).

    Além dos campos definidos em ProdutoSchemaEmail, este esquema adiciona campos para
    valor total em estoque, categoria normalizada e disponibilidade.

    Attributes:
        valor_total_estoque (Series[float]): Valor total em estoque do produto, deve ser >= 0.
        categoria_normalizada (Series[str]): Categoria do produto em formato normalizado.
        disponibilidade (Series[bool]): Indica se o produto está disponível.
    """
    
    valor_total_estoque: Series[float] = pa.Field(ge=0)  # O valor total em estoque deve ser >= 0
    categoria_normalizada: Series[str]  # Assume-se que a categoria será uma string, não precisa de check específico além de ser uma string
    disponibilidade: Series[bool]  # Disponibilidade é um booleano, então não precisa de check específico
