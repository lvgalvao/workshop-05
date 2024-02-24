from pydantic import BaseModel, ValidationError
from pydantic.types import StrictBool, StrictFloat, StrictInt, StrictStr


class Produto(BaseModel):
    name: StrictStr
    quantity: StrictInt
    price: StrictFloat
    is_stock: StrictBool = True

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