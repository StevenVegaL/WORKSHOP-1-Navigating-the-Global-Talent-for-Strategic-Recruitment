import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
import json
import psycopg2


# Cargar el dataset
candidatos = pd.read_csv("C:/Users/JSLV3/Downloads/candidates.csv", delimiter=';')

# Renombrar las columnas para que coincidan con las de la tabla de base de datos
candidatos.columns = ['first_name', 'last_name', 'email', 'application_date', 'country', 'yoe', 'seniority', 'technology', 'code_challenge_score', 'technical_interview_score']


# Cargar la configuración de la base de datos desde un archivo JSON
with open('db_config.json', 'r') as file:
    db_config = json.load(file)

# Crear la cadena de conexión usando SQLAlchemy
engine = create_engine(f'postgresql+psycopg2://{db_config["user"]}:{db_config["password"]}@{db_config["host"]}:5432/{db_config["dbname"]}')

# Usar to_sql para cargar el DataFrame en la tabla deseada
try:
    candidatos.to_sql('candidatos', engine, if_exists='append', index=False)
    print("Todos los datos se han añadido correctamente a la base de datos.")
except Exception as e:
    print(f"Se ha producido un error al insertar los datos: {e}")