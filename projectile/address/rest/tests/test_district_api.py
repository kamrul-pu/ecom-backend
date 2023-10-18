from rest_framework import status

from common.base_test import BaseTest
from . import urlhelpers, payloads


class DistrictApiTest(BaseTest):
    """Test case for district api"""

    def setUp(self):
        super().setUp()

        # Define payload
        self.district_payload = payloads.district_create_payload()

    def test_create_district(self):
        # Create district and assert response
        response = self.client.post(
            urlhelpers.get_district_list_create_url(), self.district_payload
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert some response data
        self.assertEqual(response.data["name"], self.district_payload["name"])
        self.assertEqual(response.data["division"], self.district_payload["division"])
        self.assertIn("bengali_name", response.data)
        self.assertIn("latitude", response.data)

        return {"id": response.data["id"], "uid": response.data["uid"]}

    def test_get_district_list(self):
        self.test_create_district()

        # Get district list data and assert response
        response = self.client.get(urlhelpers.get_district_list_create_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert some response data
        checked_data = response.data["results"][0]

        self.assertEqual(checked_data["name"], self.district_payload["name"])
        self.assertEqual(checked_data["division"], self.district_payload["division"])
        self.assertIn("bengali_name", checked_data)
        self.assertIn("latitude", checked_data)

    def test_get_district_detail(self):
        uid = self.test_create_district()["uid"]

        # Get district detail data and assert response
        response = self.client.get(urlhelpers.get_district_detail_update_url(uid))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert some response data
        self.assertEqual(response.data["name"], self.district_payload["name"])
        self.assertEqual(response.data["division"], self.district_payload["division"])
        self.assertIn("bengali_name", response.data)
        self.assertIn("latitude", response.data)

    def test_update_district(self):
        uid = self.test_create_district()["uid"]
        updated_district_payload = payloads.district_update_payload()

        # Update district data and assert response
        response = self.client.patch(
            urlhelpers.get_district_detail_update_url(uid), updated_district_payload
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert some response data
        self.assertEqual(response.data["name"], updated_district_payload["name"])
        self.assertEqual(
            response.data["division"], updated_district_payload["division"]
        )
        self.assertIn("bengali_name", response.data)
        self.assertIn("latitude", response.data)
