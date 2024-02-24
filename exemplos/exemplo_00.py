from typing import Dict

produto: Dict[str, str] = {
    "name":"Luciano",
    "quantidade":33,
    "price": 33.09
}

produto["name"] = "Fabio"
produto["name"] = 33

print(produto)