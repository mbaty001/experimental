import psycopg2
from dotenv import load_dotenv  
import os

load_dotenv()

conn_obj = psycopg2.connect(
    host='localhost',
    dbname='python_web',
    user=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD')
)
print("Connected to PostgreSQL database successfully!")

conn_obj.close()

conn_obj = psycopg2.connect(
    f"host=localhost dbname=python_web user={os.getenv('POSTGRES_USER')} password={os.getenv('POSTGRES_PASSWORD')}"
)
print("Connected to PostgreSQL database successfully!")

conn_obj.close()