from flask import Blueprint, make_response, request
from hashlib import sha1

from db import users

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.post("/login")
def login():
    return make_response({"message": "Not implemented"}, 501)

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
    
    users[username] = sha1(password.encode()).hexdigest()

    return make_response({"message": "User created successfully"}, status_code)