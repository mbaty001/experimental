import crud_sqlite
import crud_postgresql
from db import IS_POSTGRESQL

def is_username_occupied(conn, username):
    if IS_POSTGRESQL:
        user = crud_postgresql.select_user_by_username(conn, username)
    else:
        user = crud_sqlite.select_user_by_username(conn, username)
    return bool(user)

def insert_user(conn, user_data):
    if IS_POSTGRESQL:
        return crud_postgresql.insert_user(conn, user_data)
    else:
        return crud_sqlite.insert_user(conn, user_data)

def select_user_by_user_id(conn, user_id):
    if IS_POSTGRESQL:
        return crud_postgresql.select_user_by_user_id(conn, user_id)
    else:
        return crud_sqlite.select_user_by_user_id(conn, user_id)

def select_user_by_username(conn, username):
    if IS_POSTGRESQL:
        return crud_postgresql.select_user_by_username(conn, username)
    else:
        return crud_sqlite.select_user_by_username(conn, username)

def select_user_by_username_password(conn, username, password):
    if IS_POSTGRESQL:
        return crud_postgresql.select_user_by_username_password(conn, username, password)
    else:
        return crud_sqlite.select_user_by_username_password(conn, username, password)

def insert_task(conn, task_data):
    if IS_POSTGRESQL:
        return crud_postgresql.insert_task(conn, task_data)
    else:
        return crud_sqlite.insert_task(conn, task_data)

def get_completed_tasks(conn, user_id, is_completed):
    if IS_POSTGRESQL:
        return crud_postgresql.get_completed_tasks(conn, user_id, is_completed)
    else:
        return crud_sqlite.get_completed_tasks(conn, user_id, is_completed)

def get_user_tasks(conn, user_id):
    if IS_POSTGRESQL:
        return crud_postgresql.get_user_tasks(conn, user_id)
    else:
        return crud_sqlite.get_user_tasks(conn, user_id)

def get_user_task_by_id(conn, user_id, task_id):
    if IS_POSTGRESQL:
        return crud_postgresql.get_user_task_by_id(conn, user_id, task_id)
    else:
        return crud_sqlite.get_user_task_by_id(conn, user_id, task_id)

def update_task(conn, task_id, title, is_completed):
    if IS_POSTGRESQL:
        return crud_postgresql.update_task(conn, task_id, title, is_completed)
    else:
        return crud_sqlite.update_task(conn, task_id, title, is_completed)

def delete_task(conn, task_id):
    if IS_POSTGRESQL:
        return crud_postgresql.delete_task(conn, task_id)
    else:
        return crud_sqlite.delete_task(conn, task_id)

