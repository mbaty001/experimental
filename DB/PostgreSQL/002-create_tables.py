import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv('POSTGRES_USER')
password = os.getenv('POSTGRES_PASSWORD')

create_users_table = open('users.sql').read()
create_tasks_table = open('tasks.sql').read()

try:
    conn = psycopg2.connect(
        host='localhost',
        dbname='python_web',
        user=user,
        password=password
    )
    cur = conn.cursor()

    cur.execute(create_users_table)
    cur.execute(create_tasks_table)
    conn.commit()
    print("Tables created successfully!")
except psycopg2.Error as e:
    print(f"Error occurred: {e}")
    conn.rollback()
finally:
    if conn:
        conn.close()
    if cur:
        cur.close()