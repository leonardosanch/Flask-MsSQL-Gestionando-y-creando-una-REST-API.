import os
from datetime import timedelta
SECRET_KEY = os.urandom(32)
DEBUG = True

#Credenciales SQL
server = r"DESKTOP-9MTQ24N\SQLEXPRESS"
database = "agenda_telefonica_desde_flask"
driver = "ODBC Driver 17 for SQL Server"

SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc://@{server}/{database}?driver={driver}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

## JWT
JWT_SECRET_KEY = os.urandom(32)
JWT_COOKIE_SECURE= False #en ambiente de produccion debe ser True
JWT_TOKEN_LOCATION = ['headers','json','query_string']
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(hours=30)