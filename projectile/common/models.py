"""Common Models for our app"""

import uuid
from django.db import models

from common.choices import Status


class BaseModelWithUID(models.Model):
    uid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        db_index=True,
        unique=True,
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        db_index=True,
        default=Status.ACTIVE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def get_all_actives(self):
        return self.__class__.objects.filter(status=Status.ACTIVE).order_by("-pk")
