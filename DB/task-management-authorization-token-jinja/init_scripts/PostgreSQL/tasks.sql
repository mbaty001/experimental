CREATE TABLE tasks (
    task_id SERIAL PRIMARY KEY,
    title TEXT,
    created_at TIMESTAMP,
    is_completed BOOL, 
    user_id SERIAL,
    FOREIGN KEY(user_id) REFERENCES users(user_id)  -- to define a relationship with the users table
);

