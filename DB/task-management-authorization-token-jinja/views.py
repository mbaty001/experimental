from datetime import datetime
from functools import wraps

from flask import Blueprint, make_response, request, session, redirect, url_for, render_template
import jwt

from crud_db import (insert_task,
                         get_user_task_by_id,
                         get_completed_tasks,
                         update_task,
                         delete_task,
                         get_user_tasks, select_user_by_user_id)
from db import get_db
from app_init import app


# https://flask.palletsprojects.com/en/2.3.x/tutorial/views/
bp = Blueprint("tasks", __name__, template_folder="templates/tasks")

def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = session.get("token")

        if not token:
            return redirect(url_for("auth.login"))

        try:
            payload = jwt.decode(token, app.secret_key, "HS256")

            username = payload["username"]
            user_id = payload["user_id"]

            conn = get_db()
            user = select_user_by_user_id(conn, user_id)
            if not user:
                return redirect(url_for("auth.login"))

            session["username"] = username
            session["user_id"] = user['user_id']

        except jwt.exceptions.DecodeError:

            return redirect(url_for("auth.login"))

        return func(user['user_id'], *args, **kwargs)

    return wrapper


@bp.get("/")
@auth_required
def list_tasks(user_id):
    completed_flag = request.args.get("completed", "false").lower()  # fetch the query parameter
    # check that query parameter has valid value
    if completed_flag.lower() not in ("true", "false"):
       # say to a user that the request is invalid
        return make_response(
            {"message": "Wrong value for `completed`. Expected `true` or `false`."},
            400,
        )

    flag_mapping = {"true": True, "false": False}[completed_flag]
    conn = get_db()
    if flag_mapping:
        # filter only completed tasks
        tasks = get_completed_tasks(conn, session["user_id"], flag_mapping)
    else:
        # return all user tasks if query parameter was not provided
        tasks = get_user_tasks(conn, session["user_id"])

    return render_template("dashboard.html", is_completed=flag_mapping, tasks=tasks)


@bp.get("/new_task")
@auth_required
def get_create_task_page(user_id):
    return render_template("new_task.html")


@bp.post("/new_task")
@auth_required
def create_task(user_id):
    conn = get_db()
    task_info = (
        request.form.get("title", "Missed title"),  # get `title` from the request body
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # get current time
        False,  # by default a new task is not completed
        user_id,  # save who requested to create task
    )

    insert_task(conn, task_info)  # save the task in the storage

    return redirect(url_for("tasks.list_tasks"))


@bp.get("/complete/<task_id>")
@auth_required
def mark_completed(user_id, task_id):
    conn = get_db()
    # filter user tasks and find task by the provided ID from the path
    task = get_user_task_by_id(conn, user_id, task_id)
 
    if not task:
        # say to a user that the task with provided ID doesn't exist
        return make_response({"message": "Task not found"}, 404)

    update_task(conn, task_id, task['title'], True) # mark the task as completed
    return redirect(url_for("tasks.list_tasks"))


@bp.get("/delete/<task_id>")
@auth_required
def delete(user_id, task_id):
    # filter user tasks
    conn = get_db()
    task = get_user_task_by_id(conn, user_id, task_id)

    if not task:  # check that user try to delete own task
        # say to a user that the task with provided ID doesn't exist
        return make_response({"message": "Task not found"}, 404)

    delete_task(conn,task_id)  # delete task by the provided ID from the path

    return redirect(url_for("tasks.list_tasks"))

