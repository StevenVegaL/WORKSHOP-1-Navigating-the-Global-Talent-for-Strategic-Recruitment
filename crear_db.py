# Importar las bibliotecas necesarias

import json
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT



# Cargar la configuración de la base de datos desde el archivo JSON
with open('db_config.json', 'r') as file:
    db_config = json.load(file)

# Conectar al servidor de PostgreSQL sin especificar una base de datos
conn = psycopg2.connect(
    host=db_config['host'],
    user=db_config['user'],
    password=db_config['password']
)

# Configurar la conexión para usar el modo de autocommit
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Crear un cursor para ejecutar comandos SQL
cur = conn.cursor()

# Crear la base de datos 'workshop1st'
try:
    cur.execute("CREATE DATABASE candidatos")
    print("Base de datos 'candidatos' creada con éxito.")
except psycopg2.Error as e:
    print(f"Error al crear la base de datos: {e}")

# Cerrar la conexión y el cursor
cur.close()
conn.close()