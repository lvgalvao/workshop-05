# Vamos criar um Pydantic Model
from pydantic import BaseModel, ValidationError

class Produto(BaseModel):
    """
    Tabela de Produto
    """
    name: str
    price: float
    quantity: int
    is_stock: bool = True

user_02 = {
    "name": "Cadeira",
    "price": 300.30,
    "quantity": 30,
    "is_stock": False
}

user_03 = {
    "name": "Cadeira",
    "price": 300.30,
}

user_02_class = Produto(**user_02)
print(user_02_class)

print(user_02_class.model_fields)

user_02_class.price = "30"
print(user_02_class)

# try:
#     user = Produto(name="Cadeira",
#                    price="3000.00",
#                    is_stock=True
#                    )
    
# except ValidationError as e:
#     print(e)