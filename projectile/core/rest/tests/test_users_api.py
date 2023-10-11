from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from core.models import User
from . import payloads, urlhelpers


class UserListCreateAPITest(APITestCase):
    def setUp(self):
        # Set up a test client
        self.client = APIClient()

        # Define some payload
        self.superuser_payload = payloads.superuser_create_payload()
        self.user_payload = payloads.user_create_payload()

        # Create a superuser
        User.objects.create_superuser(
            full_name=self.superuser_payload["full_name"],
            phone_number=self.superuser_payload["phone_number"],
            password=self.superuser_payload["password"],
        )

        # Login user and assert status
        login_data = {
            "phone_number": self.superuser_payload["phone_number"],
            "password": self.superuser_payload["password"],
        }
        self.user_login = self.client.post(urlhelpers.get_token_url(), login_data)
        self.assertEqual(self.user_login.status_code, status.HTTP_200_OK)

        # Set token for user
        self.client.credentials(
            HTTP_AUTHORIZATION="Bearer " + self.user_login.data["access"],
        )

    def test_create_user(self):
        # Create user and assert response
        response = self.client.post(
            urlhelpers.get_user_list_create_url(), self.user_payload
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert some response data
        self.assertEqual(
            response.data["phone_number"], self.user_payload["phone_number"]
        )
        self.assertEqual(response.data["email"], self.user_payload["email"])
        self.assertEqual(response.data["full_name"], self.user_payload["full_name"])

        return response.data["uid"]

    def test_get_user_list(self):
        self.test_create_user()

        # Get user list data and assert response
        response = self.client.get(urlhelpers.get_user_list_create_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert some response data
        checked_data = response.data["results"][0]

        self.assertEqual(
            checked_data["phone_number"], self.user_payload["phone_number"]
        )
        self.assertEqual(checked_data["email"], self.user_payload["email"])
        self.assertEqual(checked_data["full_name"], self.user_payload["full_name"])

    def test_get_user_detail(self):
        uid = self.test_create_user()

        # Get user detail data and assert response
        response = self.client.get(urlhelpers.get_user_detail_update_url(uid))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert some response data
        self.assertEqual(
            response.data["phone_number"], self.user_payload["phone_number"]
        )
        self.assertEqual(response.data["email"], self.user_payload["email"])
        self.assertEqual(response.data["full_name"], self.user_payload["full_name"])

    def test_update_user(self):
        uid = self.test_create_user()
        updated_user_payload = payloads.user_update_payload()

        # Update user data and assert response
        response = self.client.patch(
            urlhelpers.get_user_detail_update_url(uid), updated_user_payload
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert some response data
        self.assertEqual(
            response.data["phone_number"], updated_user_payload["phone_number"]
        )
        self.assertEqual(response.data["email"], updated_user_payload["email"])
        self.assertEqual(response.data["full_name"], updated_user_payload["full_name"])
