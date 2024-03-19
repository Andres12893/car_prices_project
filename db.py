import psycopg2
from dotenv import load_dotenv
import os
import logging

# Carga las variables de entorno desde el archivo .env
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

load_dotenv(verbose=True)

# Usa las variables de entorno cargadas
DB_HOST = os.environ["DB_HOST"]
DB_DATABASE = os.environ["DB_DATABASE"]
DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]

# Establecer la conexión a la base de datos PostgreSQL
try:
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_DATABASE,
        user=DB_USER,
        password=DB_PASSWORD
    )
except Exception as e:
    logger.warning(e)

# Crear un cursor para ejecutar consultas
cursor = conn.cursor()

# Consulta SQL para crear la tabla
create_table_query = """
CREATE TABLE car_prices (
    year INT,
    make VARCHAR(20),
    model VARCHAR(30),
    trim VARCHAR(50),
    body VARCHAR(30),
    transmission VARCHAR(20),
    vin VARCHAR(30),
    state VARCHAR(2),
    condition INT,
    odometer INT,
    color VARCHAR(10),
    interior VARCHAR(10),
    seller VARCHAR(100),
    mmr INT,
    sellingprice INT,
    saledate DATE
)
"""

# Ejecutar la consulta SQL para crear la tabla
cursor.execute(create_table_query)

# Confirmar la transacción
conn.commit()

# Cerrar el cursor y la conexión
cursor.close()
conn.close()