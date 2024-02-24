import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from pathlib import Path

import os

def load_settings():
    """Carrega as configurações a partir de variáveis de ambiente."""
    dotenv_path = Path.cwd() / 'env.env'
    load_dotenv(dotenv_path=dotenv_path)

    settings = {
        "db_host": os.getenv("POSTGRES_HOST"),
        "db_user": os.getenv("POSTGRES_USER"),
        "db_pass": os.getenv("POSTGRES_PASSWORD"),
        "db_name": os.getenv("POSTGRES_DB"),
        "db_port": os.getenv("POSTGRES_PORT"),
    }
    return settings

def extrair_do_sql(query:str) -> pd.DataFrame:
    # Carregar as configurações a partir de variáveis de ambiente
    settings = load_settings()

    # Criar a string de conexão com base nas configurações
    connection_string = f"postgresql://{settings['db_user']}:{settings['db_pass']}@{settings['db_host']}:{settings['db_port']}/{settings['db_name']}"

    # Criar engine de conexão
    engine = create_engine(connection_string)

    def extrair_do_sql(sql: str):
        """Executa a consulta SQL e retorna os dados como um DataFrame."""
        with engine.connect() as conn, conn.begin():
            df = pd.read_sql(sql, conn)
        return df

    # Exemplo de consulta SQL
    df = extrair_do_sql(query)
    return df

if __name__ == "__main__":
    query = "SELECT * FROM produtos_bronze LIMIT 10;"
    df_new = extrair_do_sql(query)
    print(df_new)