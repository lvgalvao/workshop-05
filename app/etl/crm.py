import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from pathlib import Path
import os

# Carrega variáveis de ambiente do arquivo .env

dotenv_path = Path.cwd() / 'env.env'
load_dotenv(dotenv_path=dotenv_path)

# Constrói a string de conexão usando as variáveis de ambiente
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')

# Cria o engine de conexão
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_engine(url=DATABASE_URL)
# Define sua consulta SQL
sql_query = "SELECT * FROM produtos_bronze LIMIT 10;"

# Usa o Pandas para executar a consulta e armazenar o resultado em um DataFrame
df = pd.read_sql(sql_query, engine)

# Mostra o DataFrame
print(df)
