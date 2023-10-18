from rest_framework import status

from common.base_test import BaseTest
from . import urlhelpers, payloads


class AddressApiTest(BaseTest):
    """Test case for address api"""

    def setUp(self):
        super().setUp()

        # Define payload
        self.address_payload = payloads.address_create_payload()

    def test_create_address(self):
        # Create address and assert response
        response = self.client.post(
            urlhelpers.get_address_list_create_url(), self.address_payload
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert some response data
        self.assertEqual(response.data["label"], self.address_payload["label"])
        self.assertEqual(
            response.data["house_street"], self.address_payload["house_street"]
        )
        self.assertEqual(response.data["division"], self.address_payload["division"])

        return {"id": response.data["id"], "uid": response.data["uid"]}

    def test_get_address_list(self):
        self.test_create_address()

        # Get address list data and assert response
        response = self.client.get(urlhelpers.get_address_list_create_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert some response data
        checked_data = response.data["results"][0]

        self.assertEqual(checked_data["label"], self.address_payload["label"])
        self.assertEqual(
            checked_data["house_street"], self.address_payload["house_street"]
        )
        self.assertEqual(checked_data["division"], self.address_payload["division"])

    def test_get_address_detail(self):
        uid = self.test_create_address()["uid"]

        # Get address detail data and assert response
        response = self.client.get(urlhelpers.get_address_detail_update_url(uid))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert some response data
        self.assertEqual(response.data["label"], self.address_payload["label"])
        self.assertEqual(
            response.data["house_street"], self.address_payload["house_street"]
        )
        self.assertEqual(response.data["division"], self.address_payload["division"])

    def test_update_address(self):
        uid = self.test_create_address()["uid"]
        updated_address_payload = payloads.address_update_payload()

        # Update address data and assert response
        response = self.client.patch(
            urlhelpers.get_address_detail_update_url(uid), updated_address_payload
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert some response data
        self.assertEqual(response.data["label"], updated_address_payload["label"])
        self.assertEqual(
            response.data["house_street"], updated_address_payload["house_street"]
        )
        self.assertEqual(response.data["upazila"], updated_address_payload["upazila"])

    def test_update_customer_address(self):
        self.test_create_address()
        updated_address_payload = payloads.address_update_payload()

        # Update customer address data and assert response
        response = self.client.patch(
            urlhelpers.get_customer_address_update(), updated_address_payload
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert some response data
        self.assertEqual(response.data["label"], updated_address_payload["label"])
        self.assertEqual(
            response.data["house_street"], updated_address_payload["house_street"]
        )
        self.assertEqual(response.data["upazila"], updated_address_payload["upazila"])
