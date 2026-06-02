from flask import Blueprint, make_response, request, Response, session, render_template, url_for
from hashlib import sha1
import jwt

from app import app
from db import users

bp = Blueprint("auth", __name__, url_prefix="/auth", template_folder="templates/auth")


@bp.post("/login")
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    error = None

    status_code = 200

    if not username:
        error, status_code = "Username is required", 400
    elif not password:
        error, status_code = "Password is required", 400
    elif username not in users or users[username] != sha1(password.encode()).hexdigest():
        error, status_code = "Unauthorized", 401

    if error:
        return make_response({"message": error}, status_code)
    
    token = jwt.encode({"username": username}, app.secret_key)

    return make_response({"message": "Login successful", "token": token}, status_code)

@bp.get("/sign_up")
def get_sign_up_page():
    message = session.get("message")
    session.clear()
    return render_template("sign_up.html", message=message)

@bp.post("/sign_up")
def sign_up():
    username = request.json.get("username")
    password = request.json.get("password")
    error = None

    status_code = 204

    if not username:
        error, status_code = "Username is required", 400
    elif not password:
        error, status_code = "Password is required", 400
    elif username in users:
        error, status_code = "Username is already taken", 400

    if error:
        return make_response({"message": error}, status_code)
        session["message"] = {"content": error, "is_error": True}
        return redirect(url_for(""))
    
    users[username] = sha1(password.encode()).hexdigest()

    return make_response({"message": "User created successfully"}, status_code)