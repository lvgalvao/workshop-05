import pandas as pd

# pega os dados do ERP

import sqlalchemy as sal
from sqlalchemy import create_engine
db_name = "database.sqlite"
table_name = "Player_Attributes"
engine = sal.create_engine("sqlite:///%s" % db_name)
df = pd.read_sql_query("SELECT * from Player", engine

# processa os dados do ERP

# salva os dados do ERP em duckdb