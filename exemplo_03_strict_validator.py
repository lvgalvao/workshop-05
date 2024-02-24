from pydantic import BaseModel, ValidationError, field_validator


class CustomValidationModel(BaseModel):
    quantity: int   # Tipo normal, mas vamos validar estritamente

    @field_validator('quantity')
    def check_age_is_int(cls, value):
        if not isinstance(value, int):
            raise ValueError('Age must be an integer')
        return value
    
class Produto(BaseModel):
    name: str
    quantity: CustomValidationModel
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
                        quantity="30",
                        price= 40.50,
                        is_stock=True)
except ValidationError as ex:
    print(ex)

# Isso permite uma validação mais flexível e lógica customizada
    
