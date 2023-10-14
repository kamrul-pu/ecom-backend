from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models

from .choices import AddressStatus
from common.models import BaseModelWithUID, NameLocationBaseModel


class Division(NameLocationBaseModel):
    def __str__(self):
        return self.name


class District(NameLocationBaseModel):
    division = models.ForeignKey(
        Division, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.name


class Upazila(NameLocationBaseModel):
    """
    this is also police station
    """

    district = models.ForeignKey(District, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("name", "district", "division")


class Address(BaseModelWithUID):
    label = models.CharField(max_length=255, blank=True)
    house_street = models.CharField(
        verbose_name="House and street", max_length=255, blank=True
    )
    upazila = models.ForeignKey(
        Upazila, on_delete=models.SET_NULL, null=True, blank=True
    )
    division = models.ForeignKey(
        Division, on_delete=models.SET_NULL, null=True, blank=True
    )
    district = models.ForeignKey(
        District, on_delete=models.SET_NULL, null=True, blank=True
    )
    country = models.CharField(
        verbose_name="Country name", max_length=255, blank=True, default="Bangladesh"
    )
    latitude = models.DecimalField(
        max_digits=20, decimal_places=15, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=20, decimal_places=15, null=True, blank=True
    )
    user = models.ForeignKey(
        "core.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user_address",
    )

    def __str__(self):
        return f"Country: {self.country}"

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Address"
