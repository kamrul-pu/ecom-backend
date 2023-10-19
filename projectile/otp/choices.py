from django.db import models


class OtpType(models.TextChoices):
    PASSWORD_RESET = "PASSWORD_RESET", "Password Reset"
    PHONE_NUMBER_RESET = "PHONE_NUMBER_RESET", "Phone Number Reset"
    OTHER = "OTHER", "Other"
