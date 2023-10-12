from rest_framework import status

from common.base_test import BaseTest
from . import urlhelpers, payloads


class CategoryApiTest(BaseTest):
    """Test case for category api"""

    def setUp(self):
        super().setUp()

        # Define payload
        self.category_payload = payloads.category_create_payload()

    def test_create_category(self):
        # Create category and assert response
        response = self.client.post(
            urlhelpers.get_category_list_create_url(), self.category_payload
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert some response data
        self.assertEqual(response.data["name"], self.category_payload["name"])
        self.assertEqual(
            response.data["description"], self.category_payload["description"]
        )
        self.assertIn("image", response.data)

        return response.data["uid"]

    def test_get_category_list(self):
        self.test_create_category()

        # Get category list data and assert response
        response = self.client.get(urlhelpers.get_category_list_create_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert some response data
        checked_data = response.data["results"][0]

        self.assertEqual(checked_data["name"], self.category_payload["name"])
        self.assertEqual(
            checked_data["description"], self.category_payload["description"]
        )
        self.assertIn("image", checked_data)

    def test_get_category_detail(self):
        uid = self.test_create_category()

        # Get category detail data and assert response
        response = self.client.get(urlhelpers.get_category_detail_update_url(uid))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert some response data
        self.assertEqual(response.data["name"], self.category_payload["name"])
        self.assertEqual(
            response.data["description"], self.category_payload["description"]
        )
        self.assertIn("image", response.data)

    def test_update_category(self):
        uid = self.test_create_category()
        updated_category_payload = payloads.category_update_payload()

        # Update category data and assert response
        response = self.client.patch(
            urlhelpers.get_category_detail_update_url(uid), updated_category_payload
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert some response data
        self.assertEqual(response.data["name"], updated_category_payload["name"])
        self.assertEqual(
            response.data["description"], updated_category_payload["description"]
        )
        self.assertIn("image", response.data)
