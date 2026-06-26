from smtplib import SMTPAuthenticationError

from flask import (
    Blueprint,
    make_response,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

import db
import email_handler

bp_clients = Blueprint("clients", __name__, template_folder="templates/clients")
bp_itineraries = Blueprint("itineraries", __name__, template_folder="templates/itineraries")


# Create a client (POST /api/clients)
@bp_clients.post("/api/clients")
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
        return make_response(
            {
                "id": new_client.id,
                "name": new_client.name,
                "email": new_client.email,
                "phone": new_client.phone,
                "address": new_client.address,
            },
            201,
        )
    except Exception as e:
        return make_response({"message": "Internal server error."}, 500)


# List all clients (GET /api/clients)
@bp_clients.get("/api/clients")
def list_clients():
    try:
        clients = db.list_clients()
        return make_response(
            [
                {
                    "id": client.id,
                    "name": client.name,
                    "email": client.email,
                    "phone": client.phone,
                    "address": client.address,
                }
                for client in clients
            ],
            200,
        )
    except Exception as e:
        return make_response({"message": "Internal server error."}, 500)


# Get a single client (GET /api/clients/)
@bp_clients.get("/api/clients/<int:client_id>")
def get_client(client_id):
    try:
        client = db.get_client(client_id)
        if not client:
            return make_response({"message": "Client not found."}, 404)
        return make_response(
            {
                "id": client.id,
                "name": client.name,
                "email": client.email,
                "phone": client.phone,
                "address": client.address,
            },
            200,
        )
    except Exception as e:
        return make_response({"message": "Internal server error."}, 500)


# Update a client (PATCH /api/clients/)
@bp_clients.patch("/api/clients/<int:client_id>")
def patch_client(client_id):
    try:
        data = request.get_json() or {}
        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        address = data.get("address")

        if name is None and email is None and phone is None and address is None:
            return make_response({"message": "No fields provided to update."}, 400)

        updated = db.update_client(
            client_id, name=name, email=email, phone=phone, address=address
        )
        if not updated:
            return make_response({"message": "Client not found."}, 404)

        return make_response(
            {
                "id": updated.id,
                "name": updated.name,
                "email": updated.email,
                "phone": updated.phone,
                "address": updated.address,
            },
            200,
        )
    except Exception as e:
        return make_response({"message": "Internal server error."}, 500)


# Delete a client (DELETE /api/clients/)
@bp_clients.delete("/api/clients/<int:client_id>")
def delete_client(client_id):
    try:
        deleted = db.delete_client(client_id)
        if not deleted:
            return make_response({"message": f"Client not found. Id: {client_id}"}, 404)

        return make_response(
            {"message": f"Client deleted successfully. Id: {client_id}"}, 200
        )
    except Exception:
        return make_response({"message": "Internal server error."}, 500)

# Root redirect (GET /)
@bp_clients.get("/")
def index_redirect():
    # Automatically redirects anyone accessing the base domain to the list page
    return redirect(url_for("clients.list_clients_page"))

# Front end List Clients (GET /clients)
@bp_clients.get("/clients")
def list_clients_page():
    # Renders the static/skeleton template from your templates folder.
    # No database query is made here; the browser will fetch the data.
    return render_template("clients.html")

# Front end Add Client Form (GET /clients/add)
@bp_clients.get("/clients/add")
def add_client_page():
    # Renders the template containing the form to add a new client.
    return render_template("add_client.html")

# Create an itinerary (POST /api/itineraries)
@bp_itineraries.post("/api/itineraries")
def create_itineraries():
    try:
        data = request.get_json()

        client_id = data.get("client_id")
        destination = data.get("destination")
        start_date = data.get("start_date")
        end_date = data.get("end_date")
        activities = data.get("activities")

        if not destination or not start_date or not end_date:
            return make_response(
                {"message": "Destination, start_date and end_date are required."}, 400
            )

        new_itinerary = db.create_itinerary(
            client_id=client_id,
            destination=destination,
            start_date=start_date,
            end_date=end_date,
            activities=activities,
        )
        return make_response(
            {
                "id": new_itinerary.id,
                "destination": new_itinerary.destination,
                "start_date": new_itinerary.start_date,
                "end_date": new_itinerary.end_date,
                "activities": new_itinerary.activities,
            },
            201,
        )
    except ValueError as e:
        return make_response({"message": str(e)}, 404)
    except Exception as e:
        return make_response({"message": "Internal server error."}, 500)


# List all itineraries (GET /api/itineraries)
@bp_itineraries.get("/api/itineraries")
def get_all_itineraries():
    try:
        itineraries = db.list_itineraries()
        return make_response(
            [
                {
                    "id": itinerary.id,
                    "client_id": itinerary.client_id,
                    "destination": itinerary.destination,
                    "start_date": itinerary.start_date,
                    "end_date": itinerary.end_date,
                    "activities": itinerary.activities,
                    "created_at": itinerary.created_at,
                    "updated_at": itinerary.updated_at,
                }
                for itinerary in itineraries
            ],
            200,
        )
    except Exception as e:
        return make_response({"message": "Internal server error."}, 500)


# Get a single itinerary (GET /api/itineraries/)
@bp_itineraries.get("/api/itineraries/<int:itinerary_id>")
def get_itinerary(itinerary_id: int):
    try:
        itinerary = db.get_itinerary(itinerary_id)
        if not itinerary:
            return make_response(
                {"message": f"Itinerary not found. Id: {itinerary_id}"}, 404
            )
        return make_response(
            {
                "id": itinerary.id,
                "client_id": itinerary.client_id,
                "destination": itinerary.destination,
                "start_date": itinerary.start_date,
                "end_date": itinerary.end_date,
                "activities": itinerary.activities,
                "created_at": itinerary.created_at,
                "updated_at": itinerary.updated_at,
            },
            200,
        )
    except Exception as e:
        return make_response({"message": "Internal server error."}, 500)


# Update an itinerary (PATCH /api/itineraries/)
@bp_itineraries.patch("/api/itineraries/<int:itinerary_id>")
def update_itinerary(itinerary_id):
    try:
        data = request.get_json()

        destination = data.get("destination")
        start_date = data.get("start_date")
        end_date = data.get("end_date")
        activities = data.get("activities")

        if (
            destination is None
            and start_date is None
            and end_date is None
            and activities is None
        ):
            return make_response({"message": "No fields provided to update."}, 400)

        updated = db.update_itinerary(
            itinerary_id,
            destination=destination,
            start_date=start_date,
            end_date=end_date,
            activities=activities,
        )
        if not updated:
            return make_response(
                {"message": f"Itinerary not found. Id: {itinerary_id}"}, 404
            )

        return make_response(
            {
                "id": updated.id,
                "client_id": updated.client_id,
                "destination": updated.destination,
                "start_date": updated.start_date,
                "end_date": updated.end_date,
                "activities": updated.activities,
                "created_at": updated.created_at,
                "updated_at": updated.updated_at,
            },
            200,
        )
    except Exception as e:
        return make_response({"message": "Internal server error."}, 500)


# Delete an itinerary (DELETE /api/itineraries/)
@bp_itineraries.delete("/api/itineraries/<int:itinerary_id>")
def delete_itinerary(itinerary_id):
    try:
        deleted = db.delete_itinerary(itinerary_id)
        if not deleted:
            return make_response(
                {"message": f"Itinerary not found. Id: {itinerary_id}"}, 404
            )

        return make_response(
            {"message": f"Itinerary deleted successfully. Id: {itinerary_id}"}, 200
        )
    except Exception:
        return make_response({"message": "Internal server error."}, 500)


# Send itinerary details via email (POST /api/itineraries/<id>/send_email).
@bp_itineraries.post("/api/itineraries/<int:itinerary_id>/send_email")
def itinerary_send_email(itinerary_id):
    try:
        # 1. Fetch the itinerary to find the associated client_id
        itinerary = db.get_itinerary(itinerary_id)
        if not itinerary:
            return make_response({"message": f"Itinerary not found. Id: {itinerary_id}"}, 404)

        # 2. Fetch the client using the itinerary's client_id
        client = db.get_client(itinerary.client_id)
        if not client or not client.email:
            return make_response({"message": "Client or client email address not found."}, 404)

        # 3. Trigger email using the retrieved email address
        resp = email_handler.send(receipient=client.email)
        
        if resp:
            return make_response({"message": f"Email successfully dispatched to {client.email}."}, 200)
        return make_response({"message": "Email delivery failed."}, 400)
    except SMTPAuthenticationError as err:
        return make_response(
            {"message": "Email delivery failed. Authorization error."}, 403
        )
    except Exception as err:
        return make_response({"message": "Email delivery failed. Internal error."}, 500)
        
# Front end List Itineraries (GET /itineraries)
@bp_itineraries.get("/itineraries")
def list_itineraries_page():
    # Renders the main static list view for itinerary databases.
    return render_template("itineraries.html")

# Front end Add Itinerary (GET /itineraries/add)
@bp_itineraries.get("/itineraries/add")
def add_itinerary_page():
    # Renders the static form to schedule client events.
    return render_template("add_itineraries.html")
