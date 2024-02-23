from pydantic import BaseModel, ValidationError

class Produto(BaseModel):
    name: str
    quantity: int
    price: float
    is_stock: bool = True

try:
    produto_01 = Produto(name="Video Game",
                    quantity=30,
                    price= 40.50,
                    is_stock=True)
except ValidationError as ex:
    print(ex)

try:
    produto_02 = Produto(name="Video Game",
                        quantity=30,
                        price= 40.50,
                        is_stock="true")
except ValidationError as ex:
    print(ex)

try:
    produto_03 = Produto(name="Video Game",
                        quantity=30,
                        price= 40.50,
                        is_stock="yes")
except ValidationError as ex:
    print(ex)

try:
    produto_04 = Produto(name="Video Game",
                        quantity=30,
                        price= 40.50,
                        is_stock="no")
except ValidationError as ex:
    print(ex)

try:
    produto_05 = Produto(name="Video Game",
                        quantity=30,
                        price= 40.50,
                        is_stock="f")
except ValidationError as ex:
    print(ex)

try:
    produto_06 = Produto(name="Video Game",
                        quantity=30,
                        price= 40.50,
                        is_stock=0)
except ValidationError as ex:
    print(ex)

try:
    produto_07 = Produto(name="Video Game",
                        quantity=30,
                        price= 40.50,
                        is_stock="1")
except ValidationError as ex:
    print(ex)

class Produto(BaseModel):
    name: str
    quantity: int
    price: float
    is_stock: bool = True
    email: str

new_product = {
    "name":"Video Game",
    "quantity": 3,
    "price": 30.0,
    "is_stock": False,
    "email": {
        "work": "lvgalvaofilho@gmail.com",
        "home": "contato@lvgalvaofilho.com",
    }
}

produto_01 = Produto(**new_product)