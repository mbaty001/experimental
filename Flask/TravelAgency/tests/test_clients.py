import pytest
from unittest.mock import patch

class TestListClients():

    def test_list_clients(self, test_app_client, test_clients, test_clients_json):

        with patch("views.db.list_clients", return_value=test_clients):
            resp = test_app_client.get("/api/clients")

            assert resp.status_code == 200
            assert resp.get_json() == test_clients_json

    def test_list_clients_empty(self, test_app_client):
        with patch("views.db.list_clients", return_value=[]):
            resp = test_app_client.get("/api/clients")

            assert resp.status_code == 200
            assert resp.get_json() == []

    def test_list_client_db_error(self, test_app_client):
        with patch("views.db.list_clients", side_effect=Exception("DB error")):
            resp = test_app_client.get("/api/clients")

            assert resp.status_code == 500
            assert resp.get_json() == {"message": "Internal server error."}


class TestGetClient():
    def test_get_client(self, test_app_client, test_clients, test_clients_json):
        with patch("views.db.get_client", return_value=test_clients[0]):
            resp = test_app_client.get("/api/clients/1")

            assert resp.status_code == 200
            assert resp.get_json() == test_clients_json[0]

    def test_get_client_not_found(self, test_app_client):
        with patch("views.db.get_client", return_value=None):
            resp = test_app_client.get("/api/clients/999")

            assert resp.status_code == 404
            assert resp.get_json() == {"message": "Client not found."}

    def test_get_client_db_error(self, test_app_client):
        with patch("views.db.get_client", side_effect=Exception("DB error")):
            resp = test_app_client.get("/api/clients/1")

            assert resp.status_code == 500
            assert resp.get_json() == {"message": "Internal server error."}

class TestCreateClient():

    def test_create_client_success(self, test_app_client, test_clients, test_clients_json):
        with patch("views.db.create_client", return_value=test_clients[0]):
            resp = test_app_client.post("/api/clients", json=test_clients_json[0])

            assert resp.status_code == 201
            assert resp.get_json() == test_clients_json[0]


    def test_create_client_missing_name(self, test_app_client):
        resp = test_app_client.post("/api/clients", json={"email": "no_name@example.com"})

        assert resp.status_code == 400
        assert resp.get_json() == {"message": "Name and email are required."}

    def test_create_client_db_error(self, test_app_client, test_clients_json):
        with patch("views.db.create_client", side_effect=Exception("DB error")):
            resp = test_app_client.post("/api/clients", json=test_clients_json[0])

            assert resp.status_code == 500
            assert resp.get_json() == {"message": "Internal server error."}

class TestUpdateClient():

    def test_update_client_success(self, test_app_client, test_clients, test_clients_json):
        new_client = test_clients[1]
        with patch("views.db.update_client", return_value=new_client):
            resp = test_app_client.patch(f"/api/clients/{new_client.id}", json=test_clients_json[1])

            assert resp.status_code == 200
            assert resp.get_json() == test_clients_json[1]

    def test_update_client_no_fields(self, test_app_client, test_clients):
        new_client = test_clients[1]
        with patch("views.db.update_client", return_value=new_client):
            resp = test_app_client.patch(f"/api/clients/{new_client.id}", json={})

            assert resp.status_code == 400
            assert resp.get_json() == {"message": "No fields provided to update."}

    def test_update_client_not_found(self, test_app_client, test_clients, test_clients_json):
        new_client = test_clients[1]
        with patch("views.db.update_client", return_value=None):
            resp = test_app_client.patch(f"/api/clients/{new_client.id}", json=test_clients_json[1])

            assert resp.status_code == 404
            assert resp.get_json() == {"message": "Client not found."}

    def test_update_client_db_error(self, test_app_client, test_clients, test_clients_json):
        new_client = test_clients[1]
        with patch("views.db.update_client", side_effect=Exception("DB error")):
            resp = test_app_client.patch(f"/api/clients/{new_client.id}", json=test_clients_json[1])

            assert resp.status_code == 500
            assert resp.get_json() == {"message": "Internal server error."}

class TestDeleteClient():
    def test_delete_client_success(self, test_app_client, test_clients):

        client_to_delete = test_clients[0]
        with patch("views.db.delete_client", return_value=client_to_delete):
            resp = test_app_client.delete(f"/api/clients/{client_to_delete.id}")

            assert resp.status_code == 200
            assert resp.get_json() == {"message": f"Client deleted successfully. Id: {client_to_delete.id}"}

    def test_delete_client_not_found(self, test_app_client, test_clients):

        client_to_delete = test_clients[0]
        with patch("views.db.delete_client", return_value=None):
            resp = test_app_client.delete(f"/api/clients/{client_to_delete.id}")

            assert resp.status_code == 404
            assert resp.get_json() == {"message": f"Client not found. Id: {client_to_delete.id}"}

    def test_delete_client_db_error(self, test_app_client, test_clients):

        client_to_delete = test_clients[0]
        with patch("views.db.delete_client", side_effect=Exception("DB error")):
            resp = test_app_client.delete(f"/api/clients/{client_to_delete.id}")

            assert resp.status_code == 500
            assert resp.get_json() == {"message": f"Internal server error."}