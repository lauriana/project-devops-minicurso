import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

def connect_bd():
    try:
        conn_str = (
            f"DRIVER={{ODBC Driver 18 for SQL Server}};"
            f"SERVER={os.getenv('DB_HOST')};"
            f"UID={os.getenv('DB_USER')};"
            f"PWD={os.getenv('DB_PASSWORD')};"
            f"DATABASE={os.getenv('DB_NAME')};"
            "Encrypt=yes;"
            "TrustServerCertificate=no;"
            "Connection Timeout=30;"
        )
        conn = pyodbc.connect(conn_str)
        print("Conectado ao banco com sucesso!")
        return conn
    except pyodbc.Error as e:
        print(f"Erro ao conectar: {e}")
        return None


# Esse arquivo, em específico, contém uma função para tentativa de conexão ao banco de dados em nuvem da Azure.
# As credenciais do banco estão sendo inacessiveis, pois estamos utilizando dotenv para não expor.
# Mais explicações se encontram em README.md