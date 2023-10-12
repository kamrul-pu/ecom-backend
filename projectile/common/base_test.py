from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from core.models import User
from core.rest.tests import urlhelpers, payloads


class BaseTest(APITestCase):
    """Create a base test class to use multiple places"""

    def setUp(self):
        # Set up a test client
        self.client = APIClient()

        # Define payload
        self.superuser_payload = payloads.superuser_create_payload()

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
