import pytest
from unittest.mock import patch
from sqlalchemy import DateTime

class TestItineraries():

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
            resp = test_app_client.post("/api/itineraries", json=test_itineraries_json[0])

            assert resp.status_code == 201
            self.compare_response_with_json(resp.get_json(), test_itineraries_json[0])

    def test_client_does_not_exist(self, test_app_client, test_itineraries_json):
        test_itinerary = test_itineraries_json[2]
        with patch("views.db.create_itinerary", side_effect=ValueError(f"Client not found. Id: {test_itinerary["client_id"]}")):
            resp = test_app_client.post("/api/itineraries", json=test_itinerary)

            assert resp.status_code == 404
            assert resp.get_json() == {"message": f"Client not found. Id: {test_itinerary["client_id"]}"}

    def test_missing_data(self, test_app_client, test_itineraries, test_itineraries_json):
        test_itinerary = test_itineraries[0]
        test_itinerary_json = test_itineraries_json[0]
        test_itinerary_json.pop("destination")

        with patch("views.db.create_itinerary", return_value=test_itinerary):
            resp = test_app_client.post("/api/itineraries", json=test_itinerary_json)

            assert resp.status_code == 400
            assert resp.get_json() == {"message": "Destination, start_date and end_date are required."}

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
