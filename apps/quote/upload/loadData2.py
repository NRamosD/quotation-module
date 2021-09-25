from sqlalchemy import create_engine
import pandas as pd
from decouple import config
import MySQLdb

db = "quote"
table = "category"
path = "/home/nix/Documentos/prueba.xlsx"
#dialect+driver://username:password@host:port/database
url = f"mysql+mysqlconnector://{config('SECRET_USER', default='')}:{config('SECRET_PASS',default='')}@{config('SECRECT_HOST', default='localhost')}:3306/"

engine = create_engine(url + db, echo=False)

df = pd.read_excel(path)

print("okas")

df.to_sql(name = table, con = engine, if_exists='append', index=False)
