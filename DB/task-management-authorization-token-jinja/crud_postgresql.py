import psycopg2.extras

def cursor(conn):
    return conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

def insert_user(conn, user_data):
    cur = cursor(conn)
    cur.execute('INSERT INTO users (username, password) VALUES (%s, %s)', user_data)
    conn.commit()

def select_user_by_user_id(conn, user_id):
    cur = cursor(conn)
    cur.execute('SELECT * FROM users WHERE user_id=%s', (user_id,))
    user = cur.fetchone()
    return user

def select_user_by_username(conn, username):
    cur = cursor(conn)
    cur.execute('SELECT * FROM users WHERE username=%s', (username,))
    user = cur.fetchone()
    return user

def select_user_by_username_password(conn, username, password):
    cur = cursor(conn)
    cur.execute('SELECT * FROM users WHERE username=%s AND password=%s', (username,password))
    user = cur.fetchone()
    return dict(user)

def insert_task(conn, task_data):
    cur = cursor(conn)
    cur.execute('INSERT INTO tasks (title, created_at, is_completed, user_id) VALUES (%s, %s, %s, %s)', task_data)
    conn.commit()
    return cur.lastrowid

def get_completed_tasks(conn, user_id, is_completed):
    cur = cursor(conn)
    cur.execute('SELECT task_id, title, created_at, is_completed, user_id FROM tasks WHERE user_id=%s AND is_completed=%s ORDER BY created_at, title', (user_id,is_completed,))
    tasks = cur.fetchall()
    return tasks

def get_user_tasks(conn, user_id):
    cur = cursor(conn)
    cur.execute("SELECT task_id, title, created_at, is_completed, user_id FROM tasks  WHERE user_id = %s ORDER BY  created_at, title", (user_id,))
    tasks = cur.fetchall()
    return tasks

def get_user_task_by_id(conn, user_id, task_id):
    cur = cursor(conn)
    cur.execute("SELECT task_id, title, created_at, is_completed, user_id FROM tasks WHERE user_id =%s AND task_id = %s", (user_id, task_id))
    task = cur.fetchone()
    return task

def update_task(conn, task_id, title, is_completed):
    cur = cursor(conn)
    cur.execute('UPDATE tasks SET title=%s, is_completed=%s WHERE task_id=%s', (title, is_completed, task_id))
    conn.commit()

def delete_task(conn, task_id):
    cur = cursor(conn)
    cur.execute('DELETE FROM tasks WHERE task_id=%s', (task_id,))
    conn.commit()

