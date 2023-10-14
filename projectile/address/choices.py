"""Choices for our address app."""
from django.db.models import TextChoices


class AddressStatus(TextChoices):
    DRAFT = "DRAFT", "Draft"
    ACTIVE = "ACTIVE", "Active"
    REMOVED = "REMOVED", "Removed"
