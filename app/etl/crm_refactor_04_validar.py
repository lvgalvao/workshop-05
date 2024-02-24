import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from pathlib import Path
import os

from schema import schema_crm

import pandera as pa

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

@pa.check_output(schema_crm, lazy=True)
def extrair_do_sql(query:str) -> pd.DataFrame:
    # Carregar as configurações a partir de variáveis de ambiente
    settings = load_settings()

    # Criar a string de conexão com base nas configurações
    connection_string = f"postgresql://{settings['db_user']}:{settings['db_pass']}@{settings['db_host']}:{settings['db_port']}/{settings['db_name']}"

    # Criar engine de conexão
    engine = create_engine(connection_string)

    with engine.connect() as conn, conn.begin():
            df = pd.read_sql(query, conn)

    # try:
    #     schema_crm.validate(df, lazy=True)
    # except pa.errors.SchemaError as err:
    #     print(err)
    #     exit()

    return df

if __name__ == "__main__":
    query = "SELECT * FROM produtos_bronze;"
    df_new = extrair_do_sql(query)

    print(df_new)