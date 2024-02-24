import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from pathlib import Path
import os

from schema_class_email_kpi import ProdutoSchemaEmail, ProdutoSchemaEmailKPI

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

@pa.check_output(ProdutoSchemaEmail, lazy=True)
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


@pa.check_input(ProdutoSchemaEmail, lazy=True)
@pa.check_output(ProdutoSchemaEmailKPI, lazy=True)
def transformar(df: pd.DataFrame) -> pd.DataFrame:
    # Calcular valor_total_estoque
    df['valor_total_estoque'] = df['quantidade'] * df['preco']
    
    # Normalizar categoria para maiúsculas
    df['categoria_normalizada'] = df['categoria'].str.upper()
    
    # Determinar disponibilidade (True se quantidade > 0)
    df['disponibilidade'] = df['quantidade'] > 0
    
    return df

import duckdb
import pandas as pd

@pa.check_input(ProdutoSchemaEmailKPI, lazy=True)
def load_to_duckdb(df: pd.DataFrame, table_name: str, db_file: str = 'my_duckdb.db'):

    # Conectar ao DuckDB. Se o arquivo não existir, ele será criado.
    con = duckdb.connect(database=db_file, read_only=False)
    
    # Registrar o DataFrame como uma tabela temporária
    con.register('df_temp', df)
    
    # Utilizar SQL para inserir os dados da tabela temporária em uma tabela permanente
    # Se a tabela já existir, substitui.
    con.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM df_temp")
    
    # Fechar a conexão
    con.close()

if __name__ == "__main__":
    query = "SELECT * FROM produtos_bronze_email;"
    df_new = extrair_do_sql(query)
    df_calculado = transformar(df_new)
    load_to_duckdb(df_calculado, table_name="produto_bronze_kpi")
    print(df_calculado)