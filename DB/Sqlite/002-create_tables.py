import sqlite3

conn = sqlite3.connect('python_web.db')

cur = conn.cursor()

create_users_table = open('users.sql').read()
create_tasks_table = open('tasks.sql').read()

try:
    cur.execute(create_users_table)
    cur.execute(create_tasks_table)
    conn.commit()
    print("Tables created successfully!")
except sqlite3.Error as e:
    print(f"Error occurred: {e}")
finally:
    cur.close()
    conn.close()