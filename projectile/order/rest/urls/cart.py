"""Urls mappings for customer cart."""

from django.urls import path

from order.rest.views.cart import (
    CustomerCart,
)

urlpatterns = [
    path("", CustomerCart.as_view(), name="customer-cart"),
]
