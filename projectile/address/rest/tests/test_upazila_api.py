from rest_framework import status

from common.base_test import BaseTest
from . import urlhelpers, payloads


class UpazilaApiTest(BaseTest):
    """Test case for upazila api"""

    def setUp(self):
        super().setUp()

        # Define payload
        self.upazila_payload = payloads.upazila_create_payload()

    def test_create_upazila(self):
        # Create upazila and assert response
        response = self.client.post(
            urlhelpers.get_upazila_list_create_url(), self.upazila_payload
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert some response data
        self.assertEqual(response.data["name"], self.upazila_payload["name"])
        self.assertEqual(response.data["division"], self.upazila_payload["division"])
        self.assertEqual(response.data["district"], self.upazila_payload["district"])
        self.assertIn("latitude", response.data)

        return {"id": response.data["id"], "uid": response.data["uid"]}

    def test_get_upazila_list(self):
        self.test_create_upazila()

        # Get upazila list data and assert response
        response = self.client.get(urlhelpers.get_upazila_list_create_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert some response data
        checked_data = response.data["results"][0]

        self.assertEqual(checked_data["name"], self.upazila_payload["name"])
        self.assertEqual(checked_data["division"], self.upazila_payload["division"])
        self.assertEqual(checked_data["division"], self.upazila_payload["division"])
        self.assertIn("latitude", checked_data)

    def test_get_upazila_detail(self):
        uid = self.test_create_upazila()["uid"]

        # Get upazila detail data and assert response
        response = self.client.get(urlhelpers.get_upazila_detail_update_url(uid))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert some response data
        self.assertEqual(response.data["name"], self.upazila_payload["name"])
        self.assertEqual(response.data["division"], self.upazila_payload["division"])
        self.assertEqual(response.data["district"], self.upazila_payload["district"])
        self.assertIn("latitude", response.data)

    def test_update_upazila(self):
        uid = self.test_create_upazila()["uid"]
        updated_upazila_payload = payloads.upazila_update_payload()

        # Update upazila data and assert response
        response = self.client.patch(
            urlhelpers.get_upazila_detail_update_url(uid), updated_upazila_payload
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert some response data
        self.assertEqual(response.data["name"], updated_upazila_payload["name"])
        self.assertEqual(response.data["district"], updated_upazila_payload["district"])
        self.assertIn("latitude", response.data)
