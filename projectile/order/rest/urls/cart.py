"""Urls mappings for customer cart."""

from django.urls import path

from order.rest.views.cart import (
    CustomerCartList,
    UpdateCart,
)

urlpatterns = [
    path("", CustomerCartList.as_view(), name="customer-cart"),
    path("/update", UpdateCart.as_view(), name="cart-update"),
]
