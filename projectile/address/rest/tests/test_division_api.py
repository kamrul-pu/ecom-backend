from rest_framework import status

from common.base_test import BaseTest
from . import urlhelpers, payloads


class DivisionApiTest(BaseTest):
    """Test case for division api"""

    def setUp(self):
        super().setUp()

        # Define payload
        self.division_payload = payloads.division_create_payload()

    def test_create_division(self):
        # Create division and assert response
        response = self.client.post(
            urlhelpers.get_division_list_create_url(), self.division_payload
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert some response data
        self.assertEqual(response.data["name"], self.division_payload["name"])
        self.assertIn("bengali_name", response.data)
        self.assertIn("latitude", response.data)

        return {"id": response.data["id"], "uid": response.data["uid"]}

    def test_get_division_list(self):
        self.test_create_division()

        # Get division list data and assert response
        response = self.client.get(urlhelpers.get_division_list_create_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert some response data
        checked_data = response.data["results"][0]

        self.assertEqual(checked_data["name"], self.division_payload["name"])
        self.assertIn("bengali_name", checked_data)
        self.assertIn("latitude", checked_data)

    def test_get_division_detail(self):
        uid = self.test_create_division()["uid"]

        # Get division detail data and assert response
        response = self.client.get(urlhelpers.get_division_detail_update_url(uid))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert some response data
        self.assertEqual(response.data["name"], self.division_payload["name"])
        self.assertIn("bengali_name", response.data)
        self.assertIn("latitude", response.data)

    def test_update_division(self):
        uid = self.test_create_division()["uid"]
        updated_division_payload = payloads.division_update_payload()

        # Update division data and assert response
        response = self.client.patch(
            urlhelpers.get_division_detail_update_url(uid), updated_division_payload
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert some response data
        self.assertEqual(response.data["name"], updated_division_payload["name"])
        self.assertIn("bengali_name", response.data)
        self.assertIn("latitude", response.data)
