"""Urls mappings for customer cart."""

from django.urls import path

from order.rest.views.cart import (
    CustomerCart,
    UpdateCart,
)

urlpatterns = [
    path("", CustomerCart.as_view(), name="customer-cart"),
    path("/create", UpdateCart.as_view(), name="cart-update"),
]
