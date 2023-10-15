from rest_framework import status

from common.base_test import BaseTest

from . import urlhelpers, payloads


class ProductApiTest(BaseTest):
    """Test case for product api"""

    def setUp(self):
        super().setUp()

        # Define payload
        self.product_payload = payloads.product_create_payload()

    def test_create_product(self):
        # Create product and assert response
        response = self.client.post(
            urlhelpers.get_product_list_create_url(), self.product_payload
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert some response data
        self.assertEqual(response.data["name"], self.product_payload["name"])
        self.assertEqual(response.data["brand"], self.product_payload["brand"])
        self.assertEqual(response.data["category"], self.product_payload["category"])
        self.assertIn("image", response.data)

        return {"id": response.data["id"], "uid": response.data["uid"]}

    def test_get_product_list(self):
        self.test_create_product()

        # Get product list data and assert response
        response = self.client.get(urlhelpers.get_product_list_create_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert some response data
        checked_data = response.data["results"][0]

        self.assertEqual(checked_data["name"], self.product_payload["name"])
        self.assertEqual(checked_data["brand"], self.product_payload["brand"])
        self.assertEqual(checked_data["category"], self.product_payload["category"])
        self.assertIn("image", checked_data)

    def test_get_product_detail(self):
        uid = self.test_create_product()["uid"]

        # Get product detail data and assert response
        response = self.client.get(urlhelpers.get_product_detail_update_url(uid))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert some response data
        self.assertEqual(response.data["name"], self.product_payload["name"])
        self.assertEqual(response.data["brand"], self.product_payload["brand"])
        self.assertEqual(response.data["category"], self.product_payload["category"])
        self.assertIn("image", response.data)

    def test_update_product(self):
        uid = self.test_create_product()["uid"]
        updated_product_payload = payloads.product_update_payload()

        # Update product data and assert response
        response = self.client.patch(
            urlhelpers.get_product_detail_update_url(uid), updated_product_payload
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert some response data
        self.assertEqual(response.data["name"], updated_product_payload["name"])
        self.assertEqual(response.data["brand"], updated_product_payload["brand"])
        self.assertEqual(response.data["category"], updated_product_payload["category"])
