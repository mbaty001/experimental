from smtplib import SMTPAuthenticationError
from unittest.mock import patch

import pytest
from sqlalchemy import DateTime


class TestItineraries:

    def compare_response_with_json(self, response_json, json_to_compare):

        assert response_json.get("id") == json_to_compare["id"]
        assert response_json.get("destination") == json_to_compare["destination"]
        assert response_json.get("start_date") == json_to_compare["start_date"]
        assert response_json.get("end_date") == json_to_compare["end_date"]
        if json_to_compare.get("activities"):
            assert response_json.get("activities") == json_to_compare["activities"]


class TestCreateItineraries(TestItineraries):

    def test_sunny_path(self, test_app_client, test_itineraries, test_itineraries_json):
        with patch("views.db.create_itinerary", return_value=test_itineraries[0]):
            resp = test_app_client.post(
                "/api/itineraries", json=test_itineraries_json[0]
            )

            assert resp.status_code == 201
            self.compare_response_with_json(resp.get_json(), test_itineraries_json[0])

    def test_client_does_not_exist(self, test_app_client, test_itineraries_json):
        test_itinerary = test_itineraries_json[2]
        with patch(
            "views.db.create_itinerary",
            side_effect=ValueError(
                f"Client not found. Id: {test_itinerary["client_id"]}"
            ),
        ):
            resp = test_app_client.post("/api/itineraries", json=test_itinerary)

            assert resp.status_code == 404
            assert resp.get_json() == {
                "message": f"Client not found. Id: {test_itinerary["client_id"]}"
            }

    def test_missing_data(
        self, test_app_client, test_itineraries, test_itineraries_json
    ):
        test_itinerary = test_itineraries[0]
        test_itinerary_json = test_itineraries_json[0]
        test_itinerary_json.pop("destination")

        with patch("views.db.create_itinerary", return_value=test_itinerary):
            resp = test_app_client.post("/api/itineraries", json=test_itinerary_json)

            assert resp.status_code == 400
            assert resp.get_json() == {
                "message": "Destination, start_date and end_date are required."
            }

    def test_internal_error(self, test_app_client, test_itineraries_json):
        test_itinerary = test_itineraries_json[2]
        with patch("views.db.create_itinerary", side_effect=Exception("DB error")):
            resp = test_app_client.post("/api/itineraries", json=test_itinerary)

            assert resp.status_code == 500
            assert resp.get_json() == {"message": "Internal server error."}


class TestListItineraries(TestItineraries):

    def test_sunny_path(self, test_app_client, test_itineraries, test_itineraries_json):

        with patch("views.db.list_itineraries", return_value=test_itineraries):
            resp = test_app_client.get("/api/itineraries")

            assert resp.status_code == 200
            for i, response in enumerate(resp.get_json()):
                self.compare_response_with_json(response, test_itineraries_json[i])

    def test_list_itineraries_empty(self, test_app_client):
        with patch("views.db.list_itineraries", return_value=[]):
            resp = test_app_client.get("/api/itineraries")

            assert resp.status_code == 200
            assert resp.get_json() == []

    def test_list_itineraries_db_error(self, test_app_client):
        with patch("views.db.list_itineraries", side_effect=Exception("DB error")):
            resp = test_app_client.get("/api/itineraries")

            assert resp.status_code == 500
            assert resp.get_json() == {"message": "Internal server error."}


class TestGetItineraries(TestItineraries):

    def test_sunny_path(self, test_app_client, test_itineraries, test_itineraries_json):

        test_itinerary = test_itineraries[0]
        test_itinerary_json = test_itineraries_json[0]

        with patch("views.db.get_itinerary", return_value=test_itinerary):
            resp = test_app_client.get("/api/itineraries/101")
            assert resp.status_code == 200
            self.compare_response_with_json(resp.get_json(), test_itinerary_json)

    def test_get_itinerary_does_not_exits(self, test_app_client):

        not_found = 101
        with patch("views.db.get_itinerary", return_value=None):
            resp = test_app_client.get(f"/api/itineraries/{not_found}")
            assert resp.status_code == 404
            assert resp.get_json() == {
                "message": f"Itinerary not found. Id: {not_found}"
            }

    def test_get_itineraries_db_error(self, test_app_client):
        with patch("views.db.get_itinerary", side_effect=Exception("DB error")):
            resp = test_app_client.get("/api/itineraries/101")

            assert resp.status_code == 500
            assert resp.get_json() == {"message": "Internal server error."}


class TestUpdateIternaries(TestItineraries):

    def test_sunny_path(self, test_app_client, test_itineraries, test_itineraries_json):
        new_itinerary = test_itineraries[0]
        with patch("views.db.update_itinerary", return_value=new_itinerary):
            resp = test_app_client.patch(
                f"/api/itineraries/{new_itinerary.id}", json=test_itineraries_json[0]
            )

            assert resp.status_code == 200
            self.compare_response_with_json(resp.get_json(), test_itineraries_json[0])

    def test_itineraries_no_fields(self, test_app_client, test_itineraries):
        new_itinerary = test_itineraries[1]
        with patch("views.db.update_itinerary", return_value=new_itinerary):
            resp = test_app_client.patch(
                f"/api/itineraries/{new_itinerary.id}", json={}
            )

            assert resp.status_code == 400
            assert resp.get_json() == {"message": "No fields provided to update."}

    def test_itinerary_not_found(
        self, test_app_client, test_itineraries, test_itineraries_json
    ):
        new_itinerary = test_itineraries[1]
        with patch("views.db.update_itinerary", return_value=None):
            resp = test_app_client.patch(
                f"/api/itineraries/{new_itinerary.id}", json=test_itineraries_json[1]
            )

            assert resp.status_code == 404
            assert resp.get_json() == {
                "message": f"Itinerary not found. Id: {new_itinerary.id}"
            }

    def test_db_error(self, test_app_client, test_itineraries, test_itineraries_json):
        new_itinerary = test_itineraries[1]
        with patch("views.db.update_itinerary", side_effect=Exception("DB error")):
            resp = test_app_client.patch(
                f"/api/itineraries/{new_itinerary.id}", json=test_itineraries_json[1]
            )

            assert resp.status_code == 500
            assert resp.get_json() == {"message": "Internal server error."}


class TestDeleteItinerary:
    def test_sunny_path(self, test_app_client, test_itineraries):

        itinerary_to_delete = test_itineraries[0]
        with patch("views.db.delete_itinerary", return_value=itinerary_to_delete):
            resp = test_app_client.delete(f"/api/itineraries/{itinerary_to_delete.id}")

            assert resp.status_code == 200
            assert resp.get_json() == {
                "message": f"Itinerary deleted successfully. Id: {itinerary_to_delete.id}"
            }

    def test_itinerary_not_found(self, test_app_client, test_itineraries):

        itinerary_to_delete = test_itineraries[0]
        with patch("views.db.delete_itinerary", return_value=None):
            resp = test_app_client.delete(f"/api/itineraries/{itinerary_to_delete.id}")

            assert resp.status_code == 404
            assert resp.get_json() == {
                "message": f"Itinerary not found. Id: {itinerary_to_delete.id}"
            }

    def test_db_error(self, test_app_client, test_itineraries):

        itinerary_to_delete = test_itineraries[0]
        with patch("views.db.delete_itinerary", side_effect=Exception("DB error")):
            resp = test_app_client.delete(f"/api/itineraries/{itinerary_to_delete.id}")

            assert resp.status_code == 500
            assert resp.get_json() == {"message": f"Internal server error."}


class TestItinerariesEmail(TestItineraries):

    # @bp.post("/api/itineraries/send_email")
    # def itinerary_send_email():
    #     try:
    #         data = request.get_json()
    #         receipient = data.get("receipient")
    #         if not receipient:
    #             return make_response({"message": "Receipient cannot be empty."}, 400)
    #         resp = email_handler.send(receipient=receipient)
    #         if resp:
    #             return make_response({"message": "Email sent successfully"}, 200)
    #         return make_response({"message": "Email sent failed."}, 400)
    #     except SMTPAuthenticationError as err:
    #         return make_response({"message": "Email sent failed. Authorization error"}, 403)
    #     except Exception as err:
    #         return make_response({"message": "Email sent failed. Internal error"}, 500)

    def test_sunny_path(self, test_app_client):

        with patch("views.email_handler.send", return_value=True):
            resp = test_app_client.post(
                "/api/itineraries/send_email", json={"receipient": "test@kuku.com"}
            )

            assert resp.status_code == 200
            assert resp.get_json() == {"message": "Email sent successfully."}

    def test_empty_receipient(self, test_app_client):

        resp = test_app_client.post("/api/itineraries/send_email", json={})

        assert resp.status_code == 400
        assert resp.get_json() == {"message": "Receipient cannot be empty."}

    def test_failed_path(self, test_app_client):

        with patch("views.email_handler.send", return_value=False):
            resp = test_app_client.post(
                "/api/itineraries/send_email", json={"receipient": "test@kuku.com"}
            )

            assert resp.status_code == 400
            assert resp.get_json() == {"message": "Email delivery failed."}

    def test_failed_authorization(self, test_app_client):

        with patch(
            "views.email_handler.send",
            side_effect=SMTPAuthenticationError(403, "Authorization error"),
        ):
            resp = test_app_client.post(
                "/api/itineraries/send_email", json={"receipient": "test@kuku.com"}
            )

            assert resp.status_code == 403
            assert resp.get_json() == {
                "message": "Email delivery failed. Authorization error."
            }

    def test_failed_internal(self, test_app_client):

        with patch("views.email_handler.send", side_effect=Exception("Internal error")):
            resp = test_app_client.post(
                "/api/itineraries/send_email", json={"receipient": "test@kuku.com"}
            )

            assert resp.status_code == 500
            assert resp.get_json() == {
                "message": "Email delivery failed. Internal error."
            }
