from hashlib import sha1

import jwt

from flask import Blueprint, redirect, render_template, request, session, url_for

from crud_db import insert_user, is_username_occupied, select_user_by_username_password
from app_init import app

bp = Blueprint("auth", __name__, url_prefix="/auth",template_folder="templates/auth")


@bp.get("/sign_up")
def get_sign_up_page():
    message = session.get("message")

    session.clear()

    return render_template("sign_up.html", message=message)

@bp.post("/sign_up")
def sign_up():
    username = request.form.get("username")
    password = request.form.get("password")
    error = None
    # we don’t need to return anything in case the sign-up finishes successfully.
    status_code = 204
    if not username:
        # say to a user that the request is invalid - missed username
        error, status_code = "Username is required.", 400
    elif not password:
        # say to a user that the request is invalid - missed password
        error, status_code = "Password is required.", 400
    elif is_username_occupied(username):
        # say that the provided username leads to a conflict in the system
        error, status_code = "Username already exists.", 409

    if error:
        session["message"] = {"content": error, "is_error": True}

        return redirect(url_for(".sign_up"))

    insert_user((username, sha1(password.encode()).hexdigest()))
    session["message"] = {"content": "User was successfully created.", "is_error": False}

    return redirect(url_for(".login"))


@bp.get("/login")
def get_login_page():
    message = session.get("message")

    session.clear()

    return render_template("login.html", message=message)


@bp.post("/login")
def login():
    username = request.form.get("username")

    password = request.form.get("password")

    error = None

    user = select_user_by_username_password(username, sha1(password.encode()).hexdigest())

    if not username:
        error = "Username is required."

    elif not password:
        error = "Password is required."

    elif not user:
        error = "Username or password invalid."

    if error:
        session["message"] = {"content": error, "is_error": True}

        return redirect(url_for(".login"))

    token = jwt.encode({"username": username, "user_id": user.user_id}, app.secret_key)

    session["token"] = token

    return redirect(url_for("tasks.list_tasks"))


@bp.post("/logout")
def logout():
    session.clear()

    return redirect(url_for("auth.login"))

