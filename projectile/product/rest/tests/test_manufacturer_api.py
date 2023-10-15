from rest_framework import status

from common.base_test import BaseTest
from . import urlhelpers, payloads


class ManufacturerApiTest(BaseTest):
    """Test case for manufacturer api"""

    def setUp(self):
        super().setUp()

        # Define payload
        self.manufacturer_payload = payloads.manufacturer_create_payload()

    def test_create_manufacturer(self):
        # Create manufacturer and assert response
        response = self.client.post(
            urlhelpers.get_manufacturer_list_create_url(), self.manufacturer_payload
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert some response data
        self.assertEqual(response.data["name"], self.manufacturer_payload["name"])
        self.assertEqual(response.data["origin"], self.manufacturer_payload["origin"])
        self.assertEqual(
            response.data["description"], self.manufacturer_payload["description"]
        )
        self.assertIn("logo", response.data)

        return response.data["uid"]

    def test_get_manufacturer_list(self):
        self.test_create_manufacturer()

        # Get manufacturer list data and assert response
        response = self.client.get(urlhelpers.get_manufacturer_list_create_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert some response data
        checked_data = response.data["results"][0]

        self.assertEqual(checked_data["name"], self.manufacturer_payload["name"])
        self.assertEqual(checked_data["origin"], self.manufacturer_payload["origin"])
        self.assertEqual(
            checked_data["description"], self.manufacturer_payload["description"]
        )
        self.assertIn("logo", checked_data)

    def test_get_manufacturer_detail(self):
        uid = self.test_create_manufacturer()

        # Get manufacturer detail data and assert response
        response = self.client.get(urlhelpers.get_manufacturer_detail_update_url(uid))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert some response data
        self.assertEqual(response.data["name"], self.manufacturer_payload["name"])
        self.assertEqual(response.data["origin"], self.manufacturer_payload["origin"])
        self.assertEqual(
            response.data["description"], self.manufacturer_payload["description"]
        )
        self.assertIn("logo", response.data)

    def test_update_manufacturer(self):
        uid = self.test_create_manufacturer()
        updated_manufacturer_payload = payloads.manufacturer_update_payload()

        # Update manufacturer data and assert response
        response = self.client.patch(
            urlhelpers.get_manufacturer_detail_update_url(uid),
            updated_manufacturer_payload,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert some response data
        self.assertEqual(response.data["name"], updated_manufacturer_payload["name"])
        self.assertEqual(
            response.data["origin"], updated_manufacturer_payload["origin"]
        )
        self.assertEqual(
            response.data["description"], updated_manufacturer_payload["description"]
        )
