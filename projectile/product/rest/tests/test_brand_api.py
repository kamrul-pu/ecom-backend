from rest_framework import status

from common.base_test import BaseTest
from . import urlhelpers, payloads


class BrandApiTest(BaseTest):
    """Test case for brand api"""

    def setUp(self):
        super().setUp()

        # Define payload
        self.brand_payload = payloads.brand_create_payload()

    def test_create_brand(self):
        # Create brand and assert response
        response = self.client.post(
            urlhelpers.get_brand_list_create_url(), self.brand_payload
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert some response data
        self.assertEqual(response.data["name"], self.brand_payload["name"])
        self.assertEqual(response.data["origin"], self.brand_payload["origin"])
        self.assertEqual(
            response.data["description"], self.brand_payload["description"]
        )
        self.assertIn("image", response.data)

        return {"id": response.data["id"], "uid": response.data["uid"]}

    def test_get_brand_list(self):
        self.test_create_brand()

        # Get brand list data and assert response
        response = self.client.get(urlhelpers.get_brand_list_create_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert some response data
        checked_data = response.data["results"][0]

        self.assertEqual(checked_data["name"], self.brand_payload["name"])
        self.assertEqual(checked_data["origin"], self.brand_payload["origin"])
        self.assertEqual(checked_data["description"], self.brand_payload["description"])
        self.assertIn("image", checked_data)

    def test_get_brand_detail(self):
        uid = self.test_create_brand()["uid"]

        # Get brand detail data and assert response
        response = self.client.get(urlhelpers.get_brand_detail_update_url(uid))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert some response data
        self.assertEqual(response.data["name"], self.brand_payload["name"])
        self.assertEqual(response.data["origin"], self.brand_payload["origin"])
        self.assertEqual(
            response.data["description"], self.brand_payload["description"]
        )
        self.assertIn("image", response.data)

    def test_update_brand(self):
        uid = self.test_create_brand()["uid"]
        updated_brand_payload = payloads.brand_update_payload()

        # Update brand data and assert response
        response = self.client.patch(
            urlhelpers.get_brand_detail_update_url(uid), updated_brand_payload
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert some response data
        self.assertEqual(response.data["name"], updated_brand_payload["name"])
        self.assertEqual(response.data["origin"], updated_brand_payload["origin"])
        self.assertEqual(
            response.data["description"], updated_brand_payload["description"]
        )
