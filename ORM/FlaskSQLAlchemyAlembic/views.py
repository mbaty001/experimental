from datetime import datetime
from functools import wraps

import jwt
from flask import Blueprint, make_response, request, session, redirect, url_for, render_template

from app_init import app
from crud_db import (
    insert_task,
    get_user_task_by_id,
    get_completed_tasks,
    update_task,
    delete_task,
    select_user_by_user_id,
)

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
            user = select_user_by_user_id(user_id)

            if not user:
                return redirect(url_for("auth.login"))

            session["username"] = username
            session["user_id"] = user.user_id

        except jwt.exceptions.DecodeError:

            return redirect(url_for("auth.login"))

        return func(user, *args, **kwargs)

    return wrapper


@bp.get("/")
@auth_required
def list_tasks(user):
    completed_flag = request.args.get("completed", "false").lower()  # fetch the query parameter
    # check that query parameter has valid value
    if completed_flag.lower() not in ("true", "false"):
       # say to a user that the request is invalid
        return make_response(
            {"message": "Wrong value for `completed`. Expected `true` or `false`."},
            400,
        )

    flag_mapping = {"true": True, "false": False}[completed_flag]

    if flag_mapping:
        # filter only not completed tasks
        tasks = get_completed_tasks(user.user_id, flag_mapping)
    else:
        # return all user tasks if query parameter was not provided
        tasks = user.tasks

    return render_template(
        "dashboard.html",
        is_completed=flag_mapping,
        tasks=[t.__dict__ for t in tasks],
    )


@bp.get("/new_task")
@auth_required
def get_create_task_page(user):
    return render_template("new_task.html")


@bp.post("/new_task")
@auth_required
def create_task(user):
    task_info = (
        request.form.get("title", "Missed title"),  # get `title` from the request body
        datetime.now(),  # get current time
        False,  # by default a new task is not completed
        user.user_id,
        request.form.get("description"),
    )

    insert_task(task_info)  # save the task in the storage

    return redirect(url_for("tasks.list_tasks"))


@bp.get("/complete/<task_id>")
@auth_required
def mark_completed(user, task_id):
    # filter user tasks and find task by the provided ID from the path
    task = get_user_task_by_id(user.user_id, task_id)

    if not task:
        # say to a user that the task with provided ID doesn't exist
        return make_response({"message": "Task not found"}, 404)

    update_task(task_id, task.title, True) # mark the task as completed

    return redirect(url_for("tasks.list_tasks"))


@bp.get("/delete/<task_id>")
@auth_required
def delete(user, task_id):
    # filter user tasks
    task = get_user_task_by_id(user.user_id, task_id)

    if not task:  # check that user try to delete own task
        # say to a user that the task with provided ID doesn't exist
        return make_response({"message": "Task not found"}, 404)

    delete_task(task_id)  # delete task by the provided ID from the path

    return redirect(url_for("tasks.list_tasks"))

