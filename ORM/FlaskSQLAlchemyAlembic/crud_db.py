from sqlalchemy import select, update, delete

from app_init import db
from models import User, Task


def is_username_occupied(username):
    return bool(select_user_by_username(username))


def insert_user(user_data):
    username, password = user_data
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()


def select_user_by_user_id(user_id):
    stmt = select(User).where(User.user_id == user_id)
    return db.session.execute(stmt).scalar_one_or_none()


def select_user_by_username(username):
    stmt = select(User).where(User.username == username)
    return db.session.execute(stmt).scalar_one_or_none()


def select_user_by_username_password(username, password):
    stmt = select(User).where(User.username == username, User.password == password)
    return db.session.execute(stmt).scalar_one_or_none()


def insert_task(task_data):
    title, current_time, is_completed, user_id, description = task_data
    db.session.add(
        Task(
            title=title,
            created_at=current_time,
            is_completed=is_completed,
            user_id=user_id,
            description=description,
        )
    )
    db.session.commit()


def get_completed_tasks(user_id, is_completed):
    stmt = select(Task).where(Task.user_id == user_id, Task.is_completed == is_completed)
    return db.session.execute(stmt).scalars().all()


def get_user_task_by_id(user_id, task_id):
    stmt = select(Task).where( Task.user_id == user_id, Task.task_id == task_id)
    return db.session.execute(stmt).scalar_one_or_none()


def update_task(task_id, title, is_completed):
    stmt = update(Task).where(Task.task_id == task_id).values(title=title, is_completed=is_completed)
    db.session.execute(stmt)
    db.session.commit()


def delete_task(task_id):
    stmt = delete(Task).where(Task.task_id == task_id)
    db.session.execute(stmt)
    db.session.commit()

