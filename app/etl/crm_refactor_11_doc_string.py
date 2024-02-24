import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from pathlib import Path
import pandera as pa
import duckdb

from schema_class_email_kpi import ProdutoSchemaEmail, ProdutoSchemaEmailKPI


def load_settings() -> dict:
    """
    Carrega as configurações a partir de variáveis de ambiente.

    Este método lê o arquivo `.env` localizado no diretório atual para configurar
    a conexão com o banco de dados.

    Returns:
        Um dicionário contendo as configurações do banco de dados.
    """
    dotenv_path = Path.cwd() / 'env.env'
    load_dotenv(dotenv_path=dotenv_path)

    return {
        "db_host": os.getenv("POSTGRES_HOST"),
        "db_user": os.getenv("POSTGRES_USER"),
        "db_pass": os.getenv("POSTGRES_PASSWORD"),
        "db_name": os.getenv("POSTGRES_DB"),
        "db_port": os.getenv("POSTGRES_PORT"),
    }


@pa.check_output(ProdutoSchemaEmail, lazy=True)
def extrair_do_sql(query: str) -> pd.DataFrame:
    """
    Extrai dados do banco de dados SQL usando a consulta fornecida.

    Args:
        query: A consulta SQL para extrair dados.

    Returns:
        Um DataFrame do Pandas contendo os dados extraídos.
    """
    settings = load_settings()
    connection_string = f"postgresql://{settings['db_user']}:{settings['db_pass']}@{settings['db_host']}:{settings['db_port']}/{settings['db_name']}"
    engine = create_engine(connection_string)

    with engine.connect() as conn, conn.begin():
        df = pd.read_sql(query, conn)

    return df


@pa.check_input(ProdutoSchemaEmail, lazy=True)
@pa.check_output(ProdutoSchemaEmailKPI, lazy=True)
def transformar(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforma os dados do DataFrame aplicando cálculos e normalizações.

    Args:
        df: DataFrame do Pandas contendo os dados originais.

    Returns:
        DataFrame do Pandas após a aplicação das transformações.
    """
    df['valor_total_estoque'] = df['quantidade'] * df['preco']
    df['categoria_normalizada'] = df['categoria'].str.upper()
    df['disponibilidade'] = df['quantidade'] > 0

    return df


@pa.check_input(ProdutoSchemaEmailKPI, lazy=True)
def load_to_duckdb(df: pd.DataFrame, table_name: str, db_file: str = 'my_duckdb.db'):
    """
    Carrega o DataFrame no DuckDB, criando ou substituindo a tabela especificada.

    Args:
        df: DataFrame do Pandas para ser carregado no DuckDB.
        table_name: Nome da tabela no DuckDB onde os dados serão inseridos.
        db_file: Caminho para o arquivo DuckDB. Se não existir, será criado.
    """
    con = duckdb.connect(database=db_file, read_only=False)
    con.register('df_temp', df)
    con.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM df_temp")
    con.close()


if __name__ == "__main__":
    query = "SELECT * FROM produtos_bronze_email;"
    df_new = extrair_do_sql(query)
    df_calculado = transformar(df_new)
    load_to_duckdb(df_calculado, table_name="produto_bronze_kpi")
    print(df_calculado)
