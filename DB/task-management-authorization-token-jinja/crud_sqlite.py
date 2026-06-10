def insert_user(conn, user_data):
    cur = conn.cursor()
    cur.execute('INSERT INTO users (username, password) VALUES (?, ?)', user_data)
    conn.commit()

def select_user_by_user_id(conn, user_id):
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE user_id=?', (user_id,))
    user = cur.fetchone()
    return user

def select_user_by_username(conn, username):
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE username=?', (username,))
    user = cur.fetchone()
    return user

def select_user_by_username_password(conn, username, password):
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE username=? AND password=?', (username,password))
    user = cur.fetchone()
    return user

def insert_task(conn, task_data):
    cur = conn.cursor()
    cur.execute('INSERT INTO tasks (title, created_at, is_completed, user_id) VALUES (?, ?, ?, ?)', task_data)
    conn.commit()
    return cur.lastrowid

def get_completed_tasks(conn, user_id, is_completed):
    cur = conn.cursor()
    cur.execute('SELECT task_id, title, datetime(created_at) created_at, is_completed, user_id FROM tasks WHERE user_id=? AND is_completed=? ORDER BY created_at, title', (user_id, is_completed))
    tasks = cur.fetchall()
    return tasks

def get_user_tasks(conn, user_id):
    cur = conn.cursor()
    cur.execute("SELECT task_id, title, datetime(created_at) created_at, is_completed, user_id FROM tasks  WHERE user_id = ? ORDER BY created_at, title", (user_id,))
    tasks = cur.fetchall()
    return tasks

def get_user_task_by_id(conn, user_id, task_id):
    cur = conn.cursor()
    cur.execute("SELECT task_id, title, datetime(created_at) created_at, is_completed, user_id FROM tasks WHERE user_id =? AND task_id = ?", (user_id, task_id))
    task = cur.fetchone()
    return task

def update_task(conn, task_id, title, is_completed):
    cur = conn.cursor()
    cur.execute('UPDATE tasks SET title=?, is_completed=? WHERE task_id=?', (title, is_completed, task_id))
    conn.commit()

def delete_task(conn, task_id):
    cur = conn.cursor()
    cur.execute('DELETE FROM tasks WHERE task_id=?', (task_id,))
    conn.commit()

