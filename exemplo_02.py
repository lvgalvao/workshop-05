from pydantic import BaseModel, ValidationError


class Produto(BaseModel):
    name: str
    quantity: int
    price: float
    is_stock: bool = True

produto_01 = Produto(name="Video Game",
                    quantity=30,
                    price= 40.50,
                    is_stock=True)

# Caso tenhamos acordado que o schema será salvo em Dict
print(produto_01.model_dump())

print(type(produto_01.model_dump()))

# Caso tenhamos acordado que o schema será salvo em Json
print(produto_01.model_dump_json(indent=2))

print(type(produto_01.model_dump_json(indent=2)))