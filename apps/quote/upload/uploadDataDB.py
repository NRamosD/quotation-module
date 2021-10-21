from sqlalchemy import create_engine
import pandas as pd
from decouple import config
import os
#import MySQLdb
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def uploadDocumentXlsx(documentName):    
    documentLocation = os.path.join(os.path.dirname(BASE_DIR), "Documentos")
    db = "quote"
    table = "category"
    path = f"{documentLocation}/{documentName}"
    #dialect+driver://username:password@host:port/database
    #url = f"mysql+mysqlconnector://{config('SECRET_USER', default='')}:{config('SECRET_PASS',default='')}@{config('SECRECT_HOST', default='localhost')}:3306/"
    #local
    url = f"mysql+mysqlconnector://root:@localhost:3306/"
    engine = create_engine(url + db, echo=False)

    df = pd.read_excel(path)

    print("okas")

    df.to_sql(name = table, con = engine, if_exists='append', index=False)
    #pagina para configuración ssl https://docs.microsoft.com/en-us/azure/mysql/howto-configure-ssl

""" 
CÓDIGO DE EJEMPLO DEL SSL

try:
    conn = mysql.connector.connect(user='myadmin@mydemoserver',
                                   password='yourpassword',
                                   database='quickstartdb',
                                   host='mydemoserver.mysql.database.azure.com',
                                   ssl_ca='/var/www/html/BaltimoreCyberTrustRoot.crt.pem')
except mysql.connector.Error as err:
    print(err)


 """



""" connection = create_engine(
    'mysql://{user}:{password}@{host}/{database}',
    connect_args={'ssl': {'ssl-mode': 'preferred'}}
) """
