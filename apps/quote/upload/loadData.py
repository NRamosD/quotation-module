import csv
from decouple import config
import MySQLdb

mysql = MySQLdb.connect(host=config('SECRECT_HOST', default='localhost'),
                        user=config('SECRET_USER', default=''),
                        password=config('SECRET_PASS',default=''),
                        database="quote")

#with open('archivo.csv') as csv_file: