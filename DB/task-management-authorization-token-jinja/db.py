import sqlite3
from flask import g
from dotenv import load_dotenv
import os

import psycopg2

load_dotenv()
postgres_user = os.getenv('POSTGRES_USER')
postgres_password = os.getenv('POSTGRES_PASSWORD')

IS_POSTGRESQL= False


def init_postgresql(g):
    # Database connection parameters
    dbname = 'python_web'
    user = postgres_user
    password = postgres_password
    host = 'localhost'
    # Connect to the PostgreSQL database
    g.db = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

def close_postgresql(g):
    db = g.pop('db', None)

    if db is not None:
        cur = db.cursor()
        cur.close()
        db.close()

def init_sqlite(g):
    g.db = sqlite3.connect(
        "python_web.db",
        detect_types=sqlite3.PARSE_DECLTYPES
    )
    g.db.row_factory = sqlite3.Row

def close_sqlite(g):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def get_db():
    if 'db' not in g:
        if IS_POSTGRESQL:
            init_postgresql(g)
        else:
            init_sqlite(g)

    return g.db


def close_db(e=None):
    if IS_POSTGRESQL:
        close_postgresql(g)
    else:
        close_sqlite(g)

def init_app(app):
    get_db()
    app.teardown_appcontext(close_db)

