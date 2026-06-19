from flask import Blueprint, request, redirect, session, url_for, render_template, make_response
import db

bp = Blueprint("clients", __name__, template_folder="templates/clients") 

# Create a client (POST /api/clients)
@bp.post("/api/clients")
def create_client_post():
    try:
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        address = data.get("address")
        if not name or not email:
            return make_response({"message": "Name and email are required."}, 400)
        new_client = db.create_client(name, email, phone, address)
        return make_response({"id": new_client.id, "name": new_client.name, "email": new_client.email, "phone": new_client.phone, "address": new_client.address}, 201)
    except Exception as e:
        return make_response({"message": "Internal server error."}, 500)

# List all clients (GET /api/clients)
@bp.get("/api/clients")
def list_clients():
    try:
        clients = db.list_clients()
        return make_response([{"id": client.id, "name": client.name, "email": client.email, "phone": client.phone, "address": client.address} for client in clients], 200)
    except Exception as e:
        return make_response({"message": "Internal server error."}, 500)

# Get a single client (GET /api/clients/)
@bp.get("/api/clients/<int:client_id>")
def get_client(client_id):
    try:
        client = db.get_client(client_id)
        if not client:
            return make_response({"message": "Client not found."}, 404)
        return make_response({"id": client.id, "name": client.name, "email": client.email, "phone": client.phone, "address": client.address}, 200)
    except Exception as e:
        return make_response({"message": "Internal server error."}, 500)
    
# Update a client (PATCH /api/clients/)
@bp.patch("/api/clients/<int:client_id>")
def patch_client(client_id):
    try:
        data = request.get_json() or {}
        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        address = data.get("address")

        if name is None and email is None and phone is None and address is None:
            return make_response({"message": "No fields provided to update."}, 400)

        updated = db.update_client(client_id, name=name, email=email, phone=phone, address=address)
        if not updated:
            return make_response({"message": "Client not found."}, 404)

        return make_response({"id": updated.id, "name": updated.name, "email": updated.email, "phone": updated.phone, "address": updated.address}, 200)
    except Exception as e:
        return make_response({"message": "Internal server error."}, 500)
    
# Delete a client (DELETE /api/clients/)
@bp.delete("/api/clients/<int:client_id>")
def delete_client(client_id):
    try:
        deleted = db.delete_client(client_id)
        if not deleted:
            return make_response({"message": f"Client not found. Id: {client_id}"}, 404)
        
        return make_response({"message": f"Client deleted successfully. Id: {client_id}"}, 200)
    except Exception:
        return make_response({"message": "Internal server error."}, 500)