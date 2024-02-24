from app.etl.crm_refactor_01 import extrair_do_sql
import pandas as pd
from pandas.testing import assert_frame_equal

def test_extrair_do_sql():
    query = "SELECT * FROM produtos_bronze LIMIT 10;"
    df_new = extrair_do_sql(query)
    
    dados_esperados = {
        "id_produto": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "nome": ["Produto A", "Produto B", "Produto C", "Produto D", "Produto E", 
                 "Produto F", "Produto G", "Produto H", "Produto I", "Produto J"],
        "quantidade": [100, 150, 200, 50, 120, 80, 60, 30, 90, 20],
        "preço": [10.0, 20.0, 15.0, 5.0, 22.0, 45.0, 120.0, 85.0, 55.0, 100.0],
        "categoria": ["eletronicos", "mobilia", "informatica", "decoracao", "eletronicos", 
                      "mobilia", "informatica", "decoracao", "eletronicos", "mobilia"]
    }

    # Converter os dados esperados em um DataFrame
    df_esperado = pd.DataFrame(dados_esperados)

    # Usar assert_frame_equal para comparar os DataFrames
    assert_frame_equal(df_new, df_esperado)